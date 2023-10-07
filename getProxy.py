import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent # install it on your sistem with command py -3 -m pip install fake_useragent
from itertools import islice


def getProxies(n):
	ua = UserAgent()

	headers = {'User-Agent': ua.chrome}
	url = "https://hidemy.name/en/proxy-list/"
	html = requests.get(url, headers=headers).content

	soup = BeautifulSoup(html, features="lxml")
	table = soup.select_one("table:nth-of-type(1)")
	tbody = table.select_one("tbody")

	proxies = []
	for tr in tbody.find_all("tr"):
		ob = []
		for td in tr.find_all("td"):
			ob.append(td.text)
		proxy = {
			"ip": ob[0],
			"port": int(ob[1]),
			"country": ob[2].split(',')[0],
			"speed": int(ob[3].split(' ')[0]),
			"type": ob[4],
			"anonymity": ob[5],
			"last_update": int(ob[6].split(' ')[0])
		}

		proxies.append(proxy)
	proxies = sorted(proxies, key=lambda x: x['speed'])
	proxies = [{**row} for row in proxies if row['anonymity'] != 'no']

	return islice(proxies, n)

# usage: getProxies(num_of_proxies); it will list of proxies in format: {ip:, port:, country:, speed:, type:, anonimity, last_update}
