import requests

def run_zap_scan():
    target = 'https://www.digtoon.com'

    try:
        response = requests.get(target)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Check if the response content is HTML
        if 'text/html' in response.headers.get('Content-Type', ''):
            print("HTML content received successfully.")
            # Process HTML content as needed
        else:
            print("Received content is not HTML.")

    except requests.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    run_zap_scan()
