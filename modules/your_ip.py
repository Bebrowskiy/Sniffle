import requests

def get_my_ip():
    resp = requests.get("https://api.ipgeolocation.io/getip")

    data = resp.json()

    return data.get("ip")

ip = get_my_ip()
print(ip)