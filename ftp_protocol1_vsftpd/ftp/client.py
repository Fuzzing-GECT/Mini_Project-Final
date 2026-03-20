import socket
import re
from config.settings import TARGET_IP, TARGET_PORT


DATA_COMMANDS = ["LIST", "NLST", "RETR", "STOR", "APPE"]


def parse_pasv(response):

    m = re.search(r'\((.*?)\)', response)

    if not m:
        return None

    nums = m.group(1).split(",")

    if len(nums) < 6:
        return None

    ip = ".".join(nums[:4])

    port = int(nums[4]) * 256 + int(nums[5])

    return ip, port



def send_sequence(sequence):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    sock.connect((TARGET_IP, TARGET_PORT))

    # read FTP banner
    try:
        sock.recv(1024)
    except:
        pass


    outputs = []
    alive = True

    data_sock = None
    passive_addr = None


    for cmd in sequence:

        if not alive:
            outputs.append("OFF")
            continue

        try:

            sock.sendall((cmd + "\r\n").encode())

            resp = sock.recv(1024).decode(errors="ignore").strip()

            # safer response code extraction
            code = resp.split()[0][:3] if resp else "UNK"

            outputs.append(code)


            # -------- PASV handling --------
            if cmd.startswith("PASV") and code == "227":

                passive_addr = parse_pasv(resp)

                if passive_addr:

                    try:
                        data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        data_sock.settimeout(2)
                        data_sock.connect(passive_addr)
                    except:
                        data_sock = None


            # -------- DATA COMMAND handling --------
            elif cmd.split()[0] in DATA_COMMANDS and data_sock:

                try:
                    while True:
                        data = data_sock.recv(4096)
                        if not data:
                            break
                except:
                    pass

                try:
                    data_sock.close()
                except:
                    pass

                data_sock = None

                # read final completion code (e.g., 226)
                try:
                    resp2 = sock.recv(1024).decode(errors="ignore").strip()
                    if resp2:
                        outputs[-1] = resp2.split()[0][:3]
                except:
                    pass


        except:
            alive = False
            outputs.append("OFF")


    # cleanup data socket if still open
    if data_sock:
        try:
            data_sock.close()
        except:
            pass

    sock.close()

    return outputs
