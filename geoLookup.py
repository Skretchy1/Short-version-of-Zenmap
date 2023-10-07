from helpers import getServices, ip_checkv4
import requests
import json
from fake_useragent import UserAgent
import socket


def geolocation(host):
	ua = UserAgent()
	f = ip_checkv4(host)
	rtn = "(Running Geolocation)\n"
	if f == False:
		host = socket.gethostbyname(host)
	headers = {'User-Agent': ua.chrome}
	url = f"http://www.geoplugin.net/json.gp?ip={host}"
	r = requests.get(url, headers=headers).content
	try:
		response = json.loads(r)
		if response["geoplugin_status"] <300:
			data = f"""
Succesfully retrieved geolocational information about {host}
Continent: {response['geoplugin_continentName']}
Country: {response['geoplugin_countryName']}
City: {response['geoplugin_city']}
Timezone: {response['geoplugin_timezone']}
Latitude: {response['geoplugin_latitude']}
Longitude: {response['geoplugin_longitude']}
"""
			# print(data)
			rtn += data + "\n"
		else:
			# print(f"Look-up returned response code {response['geoplugin_status']}")
			rtn += f"Look-up returned response code {response['geoplugin_status']}" + "\n"
	except Exception as e:
		print(f"Error occured: {e}\n{r}")
		rtn += f"Error occured: {e}\n{r}" + "\n"

	return rtn
