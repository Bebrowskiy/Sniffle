import requests
import logging
import os

from utils.menu import check_config

if check_config():
    exit(1)
    
from config import IPGEO_API_KEY

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(filename="logs/logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def get_ip_info(ip):

    try:

        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={IPGEO_API_KEY}&ip={ip}")
        data = response.json()


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

def main():
    ip = input("IP (e.g. 22.111.000.99): ")

    # Get IP Data
    data = get_ip_info(ip)

    if data.get("message"):
        print("\n")
        print(data.get("message"))
        return

    # Data
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

    # Print
    print("╔═══════════════════ INFO ═══════════════════╗")
    print(f" {ipAdd}")
    print("╚════════════════════════════════════════════╝")
    print("\n")
    print("╔═══════════════════ GEOLOCATION ═══════════════════╗")
    print(f" Continent: {continent}")
    print(f" Country: {country}")
    print(f" Country Code: {country}")
    print(f" Calling Code: {callingCode}")
    print(f" Country TLD: {countryTLD}")
    print(f" State: {state}")
    print(f" State Code: {stateCode}")
    print(f" District: {district}")
    print(f" City: {city}")
    print(f" Zip Code: {zipCode}")
    print(f" Latitude: {latitude}")
    print(f" Longitude: {longitude}")
    print("╚═══════════════════════════════════════════════════╝")
    print("\n")
    print("╔═══════════════════ CONN. INFO ═══════════════════╗")
    print(f" ISP: {isp}")
    print(f" Organization: {organization}")
    print("╚══════════════════════════════════════════════════╝")
    print("\n")
    print("╔══════════════════════════ OTHER ══════════════════════════╗")
    print(f" Time Zone: {timeZone}")
    print(f" Offset: {offset}")
    print(f" Current Time: {currentTime}")
    print("╚═══════════════════════════════════════════════════════════╝")
    print("\n")
    print("╔═══════════════════════════ MAP ═══════════════════════════╗")
    print(f" {location}")
    print("╚═══════════════════════════════════════════════════════════╝")
    print("More information in the logs")
