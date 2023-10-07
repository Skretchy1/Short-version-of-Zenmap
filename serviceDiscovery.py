from helpers import getServices, ip_checkv4
import socket

def serviceScan(timeout=1, host="www.google.com"):
	services = getServices()
	f = ip_checkv4(host)

	rtn = "results for: " + host + "\n"

	for port, service in services.items():
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(timeout)  # set a timeout of 3 seconds for the connection attempt
			if f:
				result = sock.connect_ex((host, port))
			else:
				result = sock.connect_ex((socket.gethostbyname(host), port))
			if result == 0:
				rtn += f"{service} is running" + "\n"
			sock.close()
		except Exception as e:
			rtn += f"An error occurred while checking {service}: {e}" + "\n"
	return rtn