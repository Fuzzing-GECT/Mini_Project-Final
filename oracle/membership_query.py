import socket
import time
from config import HOST, PORT

def membership_query(sequence):
    time.sleep(0.01)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((HOST, PORT))
        sock.recv(1024)

        outputs = []
        alive = True

        for cmd in sequence:
            if not alive:
                outputs.append("OFF")
                continue

            try:
                sock.sendall((cmd + "\r\n").encode())
                data = sock.recv(1024)

                if not data:
                   alive = False
                   outputs.append("OFF")
                else:
                    data = data.decode()
                    status_code = data.split()[0]
                    outputs.append(status_code)
            except:
                alive = False
                outputs.append("OFF")

        sock.close()
        return outputs

    except:
        return ["OFF"] * len(sequence)