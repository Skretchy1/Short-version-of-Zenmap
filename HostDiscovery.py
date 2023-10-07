import socket


class HostDiscovery:
	def __init__(self, ip='0.0.0.0', command='discover', mode="normal", ips=None):  # TODO host
		if ips is None:
			ips = ['0.0.0.0']
		self.ports = []
		self.command = command
		self.mode = mode
		self.ip = ip
		self.ips = ips

	@staticmethod
	def _icmp(port, ip, timeout=3):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(timeout)
		try:
			s.connect((ip, port))
			s.shutdown(socket.SHUT_RDWR)
			return True

		except:
			return False

		finally:
			s.close()

	def scan(self, port, ip=None, ips=None):
		if ips is not None:
			for ip in ips:
				if self._ip_checkv4(ip):
					ports = []
					for i in range(21, 65000):
						if self._icmp(i, ip):
							print(f"Port {i} is open on host {ip}")
				# print(f"Host {ip} is {'up' if self._icmp(port, ip) else 'down'}")
				else:
					print(f"{ip} is not in correct IPv4 format")
		elif ip is not None:
			if self._ip_checkv4(ip):
				# print(f"Host {ip} is {'up' if self._icmp(port, ip) else 'down'}")
				ports = [7, 9, 13, 21, 22, 23, 25, 26, 37, 53, 79 - 81, 88, 106, 110, 111, 113, 119, 135, 139, 143,
						 144, 179, 199, 389, 427, 443 - 445, 465, 513, 514, 515, 543, 544, 548, 554, 587, 631, 646, 873,
						 990, 993, 995, 1025, 1026, 1027, 1028, 1029, 1110, 1433, 1720, 1723, 1755, 1900, 2000, 2001,
						 2049, 2121, 2717, 3000, 3128, 3306, 3389, 3986, 4899, 5000, 5009, 5051, 5060, 5101, 5190, 5357,
						 5432, 5631, 5666, 5800, 5900]
				for i in ports:
					if self._icmp(i, ip, 1):
						print(f"Port {i} is open on host {ip}")
			else:
				print(f"{ip} is not in correct IPv4 format")

	@staticmethod
	def _ip_checkv4(ip):
		print(ip)
		parts = ip.split(".")
		if len(parts) < 4 or len(parts) > 4:
			return False
		else:
			while len(parts) == 4:
				a = int(parts[0])
				b = int(parts[1])
				c = int(parts[2])
				d = int(parts[3])
				if a <= 0 or a == 127:
					return False
				elif d == 0:
					return False
				elif a >= 255:
					return False
				elif b >= 255 or b < 0:
					return False
				elif c >= 255 or c < 0:
					return False
				elif d >= 255 or c < 0:
					return False
				else:
					return True


HostDiscovery().scan(ip='192.168.8.105', port=135)
