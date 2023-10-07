import socket
import requests

class SiteBody:
	# DOESN'T WORK!!!!
	def getContentByIp(self, ip):
		addr = socket.gethostbyaddr(ip)
		r = requests.get(addr)
		print(r.request)

	def getContentByHost(self, host):
		r = requests.get(host)
		print(r.content)

if __name__ == "__main__":
	SiteBody().getContentByHost("https://www.google.com")

