import whois

def main():

    domain = input("Domain (e.g. google.com): ")

    try:
        # Get Domain Info
        domain_info = whois.whois(domain)


        if isinstance(domain_info, dict) and domain_info and domain_info.get('domain_name') != None:

            # Print
            output = f"\nSniffle sniffed out the domain information: {domain_info.get('domain_name', 'Unknown')}\n"
            output += "\n Dates:\n"
    
            if domain_info.get('creation_date'):
                creation_dates = ', '.join(str(date.date()) for date in domain_info['creation_date'])
                output += f"   ├─ Created:       {creation_dates}\n"
    
            if domain_info.get('updated_date'):
                updated_dates = ', '.join(str(date.date()) for date in domain_info['updated_date'])
                output += f"   ├─ Updated:     {updated_dates}\n"
    
            if domain_info.get('expiration_date'):
                expiration_dates = ', '.join(str(date.date()) for date in domain_info['expiration_date'])
                output += f"   ├─ Expires:     {expiration_dates}\n"

            output += "\n Registrar:\n"
            output += f"   ├─ Name:     {domain_info.get('registrar', 'Unknown')}\n"
            output += f"   ├─ Site:         {domain_info.get('registrar_url', 'Unknown')}\n"

            if domain_info.get('name_servers'):
                output += "\n DNS servers:\n"
                for ns in domain_info['name_servers']:
                    output += f"   ├─ {ns}\n"

            if domain_info.get('emails'):
                output += "\n Contacts:\n"
                for email in domain_info['emails']:
                    output += f"   ├─ {email}\n"

            output += f"\n Organization: {domain_info.get('org', 'Unknown')}"

            print(output)
    

        else:
            print("Sniffle didn't smell anything! Perhaps the domain does not exist or it is specified incorrectly.")

    except Exception as e:
        print(f"An error occurred while retrieving domain information: {e}")
