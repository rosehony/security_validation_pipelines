import requests
import json

def run_zap_scan():
    target = 'https://www.geeksforgeeks.org'

    try:
        response = requests.get(target)
        response.raise_for_status()  # Raise HTTPError for bad responses

        try:
            data = response.json()  # Attempt to parse JSON response
            # Process JSON data as needed
            print("JSON data received successfully.")
        except json.JSONDecodeError as err:
            print(f"JSON Decode Error: {err}")
            print(f"Invalid JSON received: {response.text}")
    except requests.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    run_zap_scan()
