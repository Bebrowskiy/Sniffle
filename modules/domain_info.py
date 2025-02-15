import whois
import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(filename="logs/logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    domain = input("\033[1;34mEnter domain (e.g. google.com): \033[0m")

    try:
        # Get domain information
        domain_info = whois.whois(domain)

        if isinstance(domain_info, dict) and domain_info and domain_info.get('domain_name') != None:
            # Beautiful output formatting
            output = f"\n\033[1;34m{'='*40}\033[0m\n"
            output += f"\033[1;32mDomain Information: {domain_info.get('domain_name', 'Unknown')}\033[0m\n"
            output += f"\033[1;34m{'='*40}\033[0m\n"

            # Dates
            if domain_info.get('creation_date'):
                creation_dates = ', '.join(str(date.date()) for date in domain_info['creation_date'])
                output += f"\033[1;36m├─ Creation Date:\033[0m {creation_dates}\n"
    
            if domain_info.get('updated_date'):
                updated_dates = ', '.join(str(date.date()) for date in domain_info['updated_date'])
                output += f"\033[1;36m├─ Updated Date:\033[0m {updated_dates}\n"
    
            if domain_info.get('expiration_date'):
                expiration_dates = ', '.join(str(date.date()) for date in domain_info['expiration_date'])
                output += f"\033[1;36m├─ Expiration Date:\033[0m {expiration_dates}\n"

            # Registrar
            output += f"\n\033[1;34m{'-'*40}\033[0m\n"
            output += f"\033[1;33mRegistrar:\033[0m {domain_info.get('registrar', 'Unknown')}\n"
            output += f"\033[1;33mRegistrar's Website:\033[0m {domain_info.get('registrar_url', 'Unknown')}\n"

            # DNS Servers
            if domain_info.get('name_servers'):
                output += "\n\033[1;34mDNS Servers:\033[0m\n"
                for ns in domain_info['name_servers']:
                    output += f"   ├─ {ns}\n"

            # Contacts
            if domain_info.get('emails'):
                output += "\n\033[1;34mContacts:\033[0m\n"
                for email in domain_info['emails']:
                    output += f"   ├─ {email}\n"

            # Organization
            output += f"\n\033[1;34m{'='*40}\033[0m\n"
            output += f"\033[1;33mOrganization:\033[0m {domain_info.get('org', 'Unknown')}\n"
            output += f"\033[1;34m{'='*40}\033[0m\n"

            # Log result
            logging.info(f"Domain: {domain} - {domain_info}")
            print(output)

        else:
            print(f"\033[1;31mSniffle didn't find anything! The domain might not exist or could be specified incorrectly.\033[0m")

    except Exception as e:
        print(f"\033[1;31mAn error occurred while retrieving domain information: {e}\033[0m")
        logging.error(f"Error scanning domain {domain}: {e}")
