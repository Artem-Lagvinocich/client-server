import socket

buf = 'ggwp'
guf = buf.encode()
sock = socket.socket()
sock.connect(("127.0.0.1", 9090))
sock.send(guf)
data = sock.recv(1024)
sock.close()

print(data)

a = 'hello'
a = a.encode("utf-8")
print(a)
