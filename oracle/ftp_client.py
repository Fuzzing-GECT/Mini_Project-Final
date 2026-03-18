# oracle/ftp_client.py

import socket
from config import HOST, PORT

def send_command_sequence(sequence):
    outputs = []

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((HOST, PORT))

        sock.recv(1024)  # Receive initial 220 banner

        alive = True

        for cmd in sequence:
            if not alive:
                outputs.append("OFF")
                continue

            try:
                sock.sendall((cmd + "\r\n").encode())
                response = sock.recv(1024)

                if not response:
                   alive = False
                   outputs.append("OFF")
                else:
                   data = response.decode()
                   status_code = data.split()[0]
                   outputs.append(status_code)

            except:
                alive = False
                outputs.append("OFF")

        sock.close()
        return outputs

    except:
        return ["OFF"] * len(sequence)