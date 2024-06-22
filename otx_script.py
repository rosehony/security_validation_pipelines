import requests
import sys

def fetch_otx_data(api_key):
    headers = {
        'X-OTX-API-KEY': api_key
    }
    response = requests.get('https://otx.alienvault.com/api/v1/indicators', headers=headers)
    if response.status_code == 200:
        indicators = response.json()
        for indicator in indicators['results']:
            print(indicator)
    else:
        raise Exception("Failed to fetch data from OTX")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 otx_script.py <api_key>")
        sys.exit(1)
    api_key = sys.argv[1]
    fetch_otx_data(api_key)
