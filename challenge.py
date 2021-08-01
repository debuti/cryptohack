#!/usr/bin/env python3
from pwn import *
import json
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode(encoding, encoded):
    if encoding == "base64":
        return base64.b64decode(encoded).decode('utf-8')
    elif encoding == "hex":
        return bytearray.fromhex(encoded).decode('utf-8')
    elif encoding == "rot13":
        return codecs.decode(encoded, 'rot_13')
    elif encoding == "bigint":
        return long_to_bytes(int(encoded,16)).decode('utf-8')
    elif encoding == "utf-8":
        return "".join([chr(b) for b in encoded])


received = json_recv()

while not "flag" in received:
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    decoded = decode(received["type"], received["encoded"])

    json_send({"decoded": decoded})

    received = json_recv()
