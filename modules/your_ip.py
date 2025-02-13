import requests

def get_my_ip():
    resp = requests.get("https://api.ipgeolocation.io/getip")

    data = resp.json()

    return data.get("ip")

def main():
    ip = get_my_ip()
    print("╔══════════════════════════╗")
    print(f"  Your IP: {ip}")
    print("╚══════════════════════════╝")