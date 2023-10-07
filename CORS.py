import socket
from fake_useragent import UserAgent
import ssl
import codecs


def scan( host):
	ua = UserAgent().chrome
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	target = socket.gethostbyname(host)  # Converts address to ip
	t_port = 443
	sock.connect((target, t_port))
	context = ssl.create_default_context()
	sock = context.wrap_socket(sock, server_hostname=host)  # Wraps socket with TLS

	request = f"OPTIONS / HTTP/1.1\r\nHost: {host} \r\nUser-Agent: {ua}\r\nConnection: keep-alive \r\n\r\n"
	sock.send(request.encode())
	chunks = []

	ret = sock.recv(4096)

	rtn = "(Checking CORS settings for " + host +")\n"

	response = codecs.decode(ret, encoding="utf-8", errors="replace").split("\n")
	for line in response:
		if "Allow:".lower() in line.lower():
			print(line)
			rtn += line +"\n"
		if "Access-Control-Allow-Origin:".lower() in line.lower():
			print(line)
			rtn += line +"\n"
		if "Access-Control-Allow-Methods:".lower() in line.lower():
			print(line)
			rtn += line +"\n"
		if "Access-Control-Allow-Headers:".lower() in line.lower():
			print(line)
			rtn += line +"\n"

	return rtn
