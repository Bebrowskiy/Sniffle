import requests
import logging
import os
from utils.menu import check_config

# Configuration file check
if check_config():
    exit(1)

from config import IPGEO_API_KEY

# Creating a folder for logs if it does not exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configuring logging
logging.basicConfig(filename="logs/logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to retrieve IP data
def get_ip_info(ip):
    try:
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={IPGEO_API_KEY}&ip={ip}")
        data = response.json()

        # Логирование полученных данных
        logging.info(f"Scanning {ip}: {data}")
        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for {ip}: {e}")
        return {"error": f"Request failed: {e}"}
    except ValueError as e:
        logging.error(f"Value error: {e}")
        return {"error": f"Value error: {e}"}
    except Exception as e:
        logging.error(f"Unexpected error for {ip}: {e}")
        return {"error": f"Unexpected error: {e}"}

# Main function
def main():
    ip = input("\033[1;34mEnter the IP to check (e.g. 22.111.000.99): \033[0m").strip()

    # Getting IP data
    data = get_ip_info(ip)

    if data.get("message"):
        print("\n")
        print(f"\033[1;31m{data.get('message')}\033[0m")
        return

    # Retrieving the data
    ipAdd = data.get("ip")
    conn = data.get("connection_type", "N/A")
    continent = data.get("continent_name", "N/A")
    country = data.get("country_name_official", "N/A")
    countCode = data.get("country_code3", "N/A")
    callingCode = data.get("calling_code", "N/A")
    countryTLD = data.get("country_tld", "N/A")
    state = data.get("state_prov", "N/A")
    stateCode = data.get("state_code", "N/A")
    district = data.get("district", "N/A")
    city = data.get("city", "N/A")
    zipCode = data.get("zipcode", "N/A")
    latitude = data.get("latitude", "N/A")
    longitude = data.get("longitude", "N/A")
    isp = data.get("isp", "N/A")
    organization = data.get("organization", "N/A")
    timeZone = data.get("time_zone").get("name", "N/A")
    offset = data.get("time_zone").get("offset", "N/A")
    currentTime = data.get("time_zone").get("current_time")
    location = f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}"

    # Information output
    print("\033[1;34m╔═══════════════════ INFO ═══════════════════╗\033[0m")
    print(f"\033[1;32m  IP Address: \033[1;36m{ipAdd}\033[0m")
    print("\033[1;34m╚════════════════════════════════════════════╝\033[0m")
    print("\n")
    
    print("\033[1;34m╔═══════════════════ GEOLOCATION ═══════════════════╗\033[0m")
    print(f"\033[1;32m  Continent: \033[0m{continent}")
    print(f"\033[1;32m  Country: \033[0m{country}")
    print(f"\033[1;32m  Country Code: \033[0m{countCode}")
    print(f"\033[1;32m  Calling Code: \033[0m{callingCode}")
    print(f"\033[1;32m  Country TLD: \033[0m{countryTLD}")
    print(f"\033[1;32m  State: \033[0m{state}")
    print(f"\033[1;32m  State Code: \033[0m{stateCode}")
    print(f"\033[1;32m  District: \033[0m{district}")
    print(f"\033[1;32m  City: \033[0m{city}")
    print(f"\033[1;32m  Zip Code: \033[0m{zipCode}")
    print(f"\033[1;32m  Latitude: \033[0m{latitude}")
    print(f"\033[1;32m  Longitude: \033[0m{longitude}")
    print("\033[1;34m╚═══════════════════════════════════════════════════╝\033[0m")
    print("\n")
    
    print("\033[1;34m╔═══════════════════ CONNECTION INFO ═══════════════════╗\033[0m")
    print(f"\033[1;32m  ISP: \033[0m{isp}")
    print(f"\033[1;32m  Organization: \033[0m{organization}")
    print("\033[1;34m╚═══════════════════════════════════════════════════════╝\033[0m")
    print("\n")
    
    print("\033[1;34m╔══════════════════════════ OTHER ══════════════════════════╗\033[0m")
    print(f"\033[1;32m  Time Zone: \033[0m{timeZone}")
    print(f"\033[1;32m  Offset: \033[0m{offset}")
    print(f"\033[1;32m  Current Time: \033[0m{currentTime}")
    print("\033[1;34m╚═══════════════════════════════════════════════════════════╝\033[0m")
    print("\n")
    
    print("\033[1;34m╔═════════════════════════════════ MAP ═════════════════════════════════╗\033[0m")
    print(f"\033[1;32m  Location: \033[0m{location}")
    print("\033[1;34m╚═══════════════════════════════════════════════════════════════════════╝\033[0m")
    
    print("\n\033[1;33mMore information in the logs.\033[0m")
