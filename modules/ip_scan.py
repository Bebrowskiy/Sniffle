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
            "CONN. TYPE": data.get("connection_type"),
            "CONTINENT NAME": data.get("continent_name"),
            "COUNTRY": data.get("country_name_official"),
            "COUNTRY CODE": data.get("country_code3"),
            "CALLING CODE": data.get("calling_code"),
            "COUNTRY TLD": data.get("country_tld"),
            "STATE": data.get("state_prov"),
            "STATE CODE": data.get("state_code"),
            "DISTRICT": data.get("district"),
            "CITY": data.get("city"),
            "ZIP CODE": data.get("zipcode"),
            "LATITUDE": data.get("latitude"),
            "LONGITUDE": data.get("longitude"),
            "ISP": data.get("isp"),
            "ORGANIZATION": data.get("organization"),
            "TIME ZONE": data.get("time_zone").get("name"),
            "OFFSET": data.get("time_zone").get("offset"),
            "CURRENT TIME": data.get("time_zone").get("current_time"),
            "CURRENT TIME UNIX": data.get("time_zone").get("current_time_unix"),
            "LOCATION": f"https://www.openstreetmap.org/?mlat={data.get("latitude")}&mlon={data.get("longitude")}"
        }

        logging.info(f"Scanning {ip}: {data}")

        return output_result

    except Exception as e:
        return {"error": {e}}
