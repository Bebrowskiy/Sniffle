import requests
import logging
import os

from config import IPGEO_API_KEY

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(filename="logs/ip_scan.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def get_ip_info(ip):

    try:

        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={IPGEO_API_KEY}&ip={ip}")
        data = response.json()

        output_result = {
            "IP": data.get("ip"),
            "CONNTYPE": data.get("connection_type"),
            "CONTINENTNAME": data.get("continent_name"),
            "COUNTRY": data.get("country_name_official"),
            "COUNTRYCODE": data.get("country_code3"),
            "CALLINGCODE": data.get("calling_code"),
            "COUNTRYTLD": data.get("country_tld"),
            "STATE": data.get("state_prov"),
            "STATECODE": data.get("state_code"),
            "DISTRICT": data.get("district"),
            "CITY": data.get("city"),
            "ZIPCODE": data.get("zipcode"),
            "LATITUDE": data.get("latitude"),
            "LONGITUDE": data.get("longitude"),
            "ISP": data.get("isp"),
            "ORGANIZATION": data.get("organization"),
            "TIMEZONE": data.get("time_zone").get("name"),
            "OFFSET": data.get("time_zone").get("offset"),
            "CURRENTTIME": data.get("time_zone").get("current_time"),
            "CURRENTTIMEUNIX": data.get("time_zone").get("current_time_unix"),
            "LOCATION": f"https://www.openstreetmap.org/?mlat={data.get("latitude")}&mlon={data.get("longitude")}"
        }

        logging.info(f"Scanning {ip}: {data}")

        return data

    except Exception as e:
        return {"error": {e}}

def main():
    ip = input("IP: ")
    data = get_ip_info(ip)

    # Data
    ipAdd = data.get("ip")
    conn = data.get("connection_type")
    continent = data.get("continent_name")
    country = data.get("country_name_official")
    countCode = data.get("country_code3")
    callingCode = data.get("calling_code")
    countryTLD = data.get("country_tld")
    state = data.get("state_prov")
    stateCode = data.get("state_code")
    district = data.get("district")
    city = data.get("city")
    zipCode = data.get("zipcode")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    isp = data.get("isp")
    organization = data.get("organization")
    timeZone = data.get("time_zone").get("name")
    offset = data.get("time_zone").get("offset")
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
