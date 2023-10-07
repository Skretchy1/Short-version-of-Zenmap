import socket
from fake_useragent import UserAgent
import ssl


	# Checks if a given cookie has the "Secure" and "HttpOnly" tags set
def scan(host):
		ua = UserAgent().chrome
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		target = socket.gethostbyname(host)  # Converts address to ip
		t_port = 443
		sock.connect((target, t_port))
		context = ssl.create_default_context()
		sock = context.wrap_socket(sock, server_hostname=host)  # Wraps socket with TLS

		request = f"GET / HTTP/1.1\r\nHost: {host} \r\nUser-Agent: {ua}\r\nConnection: keep-alive \r\n\r\n"
		sock.send(request.encode())
		ret = sock.recv(4096)
		res = ret.decode().split("\n")

		rtn = ""
		rtn += "(Scanning cookies for " + host + ")\n"
		for line in res:
			if "set-cookie:" in line.lower():
				cookieName = line[11:].split("=")[0]
				print('[-]' + cookieName + ":")
				rtn +=  '[-]' + cookieName + ":" +"\n"
				if "; secure" in line.lower():
					print('   - Secure tag set')
					rtn += '   - Secure tag set' +"\n"
				if "; secure" not in line.lower():
					print('   - Secure tag not set.')
					rtn += '   - Secure tag not set' +"\n"
				if "; httponly" in line.lower():
					print('   - HttpOnly tag set')
					rtn += '   - HttpOnly tag set' +"\n"
				if "; httponly" not in line.lower():
					print('   - HttpOnly tag not set')
					rtn += '   - HttpOnly tag not set' +"\n"

		return rtn

# if __name__ == "__main__":
# 	HTTPCookies().checkCookies("www.wikipedia.org")



	
