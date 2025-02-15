import requests

def get_my_ip():
    # Send a request to the API to get the IP
    resp = requests.get("https://api.ipgeolocation.io/getip")
    
    # Извлекаем данные из ответа
    data = resp.json()
    
    return data.get("ip")

def main():
    ip = get_my_ip()
    
    # Structured beautiful output
    print("\033[1;34m╔════════════════════════════════╗\033[0m")
    print(f"\033[1;32m  Your IP Address: \033[1;36m{ip}\033[0m")
    print("\033[1;34m╚════════════════════════════════╝\033[0m")
