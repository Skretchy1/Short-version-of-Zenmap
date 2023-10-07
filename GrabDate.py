import socket
from fake_useragent import UserAgent
import ssl

h = "www.google.com"
ua = UserAgent().chrome
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = socket.gethostbyname(h)  # Converts address to ip
t_port = 443
sock.connect((target, t_port))
context = ssl.create_default_context()
sock = context.wrap_socket(sock, server_hostname=h)  # Wraps socket with TLS

request = f"GET / HTTP/1.1\r\nHost: {h} \r\nUser-Agent: {ua}\r\nConnection: keep-alive \r\n\r\n"
sock.send(request.encode())
ret = sock.recv(4096)
print('[+]' + ret.decode())

# TODO extract date instead of printing everything