import subprocess
import re
import logging


logging.basicConfig(filename="logs/logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Function for checking the correctness of the email format
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

# Function to check if the IP format is correct
def is_valid_ip(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    return re.match(pattern, ip) is not None

def search(data, query_type):
    print(f"\n\033[1;34m{'='*50}\033[0m")
    print(f"\033[1;34mSearching for {query_type.capitalize()}: {data}\033[0m")
    print(f"\033[1;34m{'='*50}\033[0m")
    
    try:
        result = subprocess.run(['h8mail', '-t', data, '-q', query_type], capture_output=True, text=True, check=True)
        output = result.stdout
        
        # Filter only the desired information from the output
        if "Not Compromised" in output:
            return f"\033[1;32mStatus for {data}:\n- Not Compromised\033[0m\n{'-'*50}"
        elif "Compromised" in output:
            return f"\033[1;31mStatus for {data}:\n- Compromised\033[0m\n{'-'*50}"
        elif not output.strip():
            return f"\033[1;33mSorry, no results found for {data}. Please check the entered data.\033[0m\n{'-'*50}"
        else:
            return f"\033[1;33mInformation not found for {data}.\033[0m\n{'-'*50}"
    except subprocess.CalledProcessError as e:
        return f"\n\033[1;31mAn error occurred while running the search: {e}\033[0m\n{'='*50}"

# Main function for selecting the search type and calling the corresponding method
def search_data(query_type, data):
    if query_type == 'email':
        if not is_valid_email(data):
            return "\033[1;31mInvalid email format. Please enter a valid email address.\033[0m"
    elif query_type == 'ip':
        if not is_valid_ip(data):
            return "\033[1;31mInvalid IP address format. Please enter a valid IP address.\033[0m"
    elif query_type == 'username':
        # No validation is required for username
        pass
    else:
        return "\033[1;31mInvalid query type! Use 'email', 'username', or 'ip'.\033[0m"
    
    return search(data, query_type)

def main():
    print("\n\033[1;34mWelcome to the Leak Search Tool\033[0m\n")
    
    data = input("\033[1;36m[*] Enter data (email, username, ip): \033[0m").strip()
    query_type = input("\033[1;36m[*] Enter data type (email, username, ip): \033[0m").strip().lower()

    result = search_data(query_type, data)
    
    if result:
        logging.info(f"Leak detection for {data}({query_type}): {result}")
        print(result)
