# Sniffle 🐾


Sniffle is a set of OSINT tools that helps you collect useful information about domains, IP addresses, and other data. It's all gathered in one place with a playful and simple interface.

---

## 🚀 Main functions

- **IP Address Verification**: Get information about the location, owner and status of an IP address.
- **Domain Search**: Find out who registered the domain, its status and other details.
- **CLI Interface**: Easy user interaction and visual information.

---

## 📂 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sniffle.git
cd sniffle
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a configuration file

Rename the config_template.py file to config.py and fill it with your API keys.

## 🧭 How to use?

### 1. Run the script
```bash
python sniffle.py
```

### 2. Select the desired module and follow the instructions

## 🌍 Example output

#### For IP address:

```yaml
╔═══════════════════ INFO ═══════════════════╗
 8.8.8.8
╚════════════════════════════════════════════╝


╔═══════════════════ GEOLOCATION ═══════════════════╗
 Continent: North America
 Country: United States of America
 Country Code: United States of America
 Calling Code: +1
 Country TLD: .us
 State: California
 State Code: US-CA
 District: Santa Clara
 City: Mountain View
 Zip Code: 94043-1351
 Latitude: 37.42240
 Longitude: -122.08421
╚═══════════════════════════════════════════════════╝


╔═══════════════════CONN. INFO═══════════════════╗
 ISP: Google LLC
 Organization: Google LLC
╚════════════════════════════════════════════════╝


╔══════════════════════════OTHER══════════════════════════╗
 Time Zone: America/Los_Angeles
 Offset: -8
 Current Time: 2025-02-13 02:00:35.884-0800
╚═════════════════════════════════════════════════════════╝


╔═══════════════════════════MAP═══════════════════════════╗
 https://www.openstreetmap.org/?mlat=37.42240&mlon=-122.08421
╚═════════════════════════════════════════════════════════╝
```

### For the domain:

```yaml
 Dates:
   ├─ Created:     2005-02-15
   ├─ Updated:     2025-01-14
   ├─ Expires:     2026-02-15

 Registrar:
   ├─ Name:     MarkMonitor, Inc.
   ├─ Site:         http://www.markmonitor.com

 DNS servers:
   ├─ NS1.GOOGLE.COM
   ├─ NS2.GOOGLE.COM
   ├─ NS3.GOOGLE.COM
   ├─ NS4.GOOGLE.COM

 Contacts:
   ├─ abusecomplaints@markmonitor.com
   ├─ whoisrequest@markmonitor.com

 Organization: Google LLC
 ```

## 🔧 Requirements

- Python 3.7+
- Libraries:
  - `requests`.
  - `colorama`
  - and others specified in `requirements.txt`

### 📄 License

This project is distributed under the MIT license. See the [LICENSE](site) file for details.

## ✨ Support
If you like this project, don't forget to leave ⭐ on GitHub! Thank you for using Sniffle!

*PS: The project is in active development, and I would be glad to see people willing to help in its further development!*