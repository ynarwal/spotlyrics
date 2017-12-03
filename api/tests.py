import requests

send_url = 'http://freegeoip.net/json'
response = requests.get(send_url)
json = response.json()
    
lat = json['latitude']
lon = json['longitude']
print(lat, lon)