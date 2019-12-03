#РАбота с вебом и пишем простейший веб сервер
import socket

sock = socket.socket()

try:
    sock.bind(('',80))
    print("Using port 80")
except OSError:
    sock.bind(('', 8080))
    print("Using port 8080")
    
sock.listen(5)

conn, addr = sock.accept()
print("Connected", addr, "\n")

data = conn.recv(8192)
msg = data.decode()

print(msg)

name = msg.split()[1][1:]
if name == "": name = "www2.html"

print(name)

resp = """HTTP/1.1 200 OK
Server:SelfMadeServer v0.0.1

"""
try:
    with open(name , 'r', encoding="utf-8") as file:
        resp += file.read()
except FileNotFoundError:
    resp += """HTTP/1.1 404 OK
Server:SelfMadeServer v0.0.1
"""

conn.send(resp.encode())

conn.close()