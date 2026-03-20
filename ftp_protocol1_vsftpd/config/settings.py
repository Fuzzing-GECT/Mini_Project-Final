ALPHABET = [

# Authentication
"USER anonymous",
"PASS guest",

# Session
"QUIT",
"NOOP",
"SYST",


# Directory navigation
"PWD",
"CWD /",
"CDUP",

# File operations
"DELE data/delete_me.txt",
"MKD newdir",
"RMD newdir",

# Rename
"RNFR data/test.txt",
"RNTO renamed.txt",

# Transfer settings
"TYPE I",
"TYPE A",

# Data connection
"PASV",
"PORT 127,0,0,1,7,138",

# Data transfer
"LIST",
"NLST",
"RETR data/test.txt",
"STOR upload.txt",
"APPE upload.txt",
#
# Control
"ABOR",
"REST 0",

"MODE",
"STRU"
]
TARGET_IP = "127.0.0.1"
TARGET_PORT = 21
