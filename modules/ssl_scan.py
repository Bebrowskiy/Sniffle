import ssl
import socket
from datetime import datetime, timezone
import logging


logging.basicConfig(filename="logs/logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")


def get_ssl_certificate(hostname: str, port: int = 443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return cert, None
    except Exception as e:
        return None, str(e)

def analyze_ssl_certificate(hostname: str):
    cert, error = get_ssl_certificate(hostname)
    if not cert:
        print(f"\n\033[1;31m[ERROR]\033[0m Could not retrieve certificate: {error}\n")
        return
    
    subject = dict(x[0] for x in cert.get('subject', []))
    issuer = dict(x[0] for x in cert.get('issuer', []))
    valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y GMT").replace(tzinfo=timezone.utc)
    valid_until = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y GMT").replace(tzinfo=timezone.utc)
    signature_algorithm = cert.get('signatureAlgorithm', 'Unknown')
    current_time = datetime.now(timezone.utc)

    print("\n\033[1;34m========================================\033[0m")
    print(f"\033[1;34m  Analyzing SSL Certificate for {hostname}\033[0m")
    print("\033[1;34m========================================\033[0m\n")
    print(f"\033[1;32m  Subject:\033[0m {subject.get('commonName', 'Unknown')}")
    print(f"\033[1;32m  Issuer:\033[0m {issuer.get('commonName', 'Unknown')}")
    print(f"\033[1;32m  Valid From:\033[0m {valid_from}")
    print(f"\033[1;32m  Valid Until:\033[0m {valid_until}")
    print(f"\033[1;32m  Signature Algorithm:\033[0m {signature_algorithm}\n")
    
    if current_time < valid_until:
        print("\033[1;32m[INFO] The certificate is still valid.\033[0m\n")
    else:
        print("\033[1;31m[WARNING] The certificate has expired!\033[0m\n")
    logging.info(f"Scanning SSL {hostname}: {cert}")

def main():
    domain = input("Enter the domain to check SSL certificate (e.g., google.com): ").strip()
    analyze_ssl_certificate(domain)
