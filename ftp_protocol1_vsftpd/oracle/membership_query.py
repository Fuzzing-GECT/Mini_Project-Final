import time
from ftp.client import send_sequence

CLEANUP_CMDS = [
    "DELE upload.txt",
    "DELE test.txt",
    "RMD newdir"
]

def membership_query(sequence):
    #print("MQ:", sequence, flush=True)
    time.sleep(0.02)

    try:
        outputs = send_sequence(sequence)

        # cleanup environment after each query
        try:
            send_sequence(CLEANUP_CMDS)
        except:
            pass

        return outputs

    except:
        return ["OFF"] * len(sequence)
