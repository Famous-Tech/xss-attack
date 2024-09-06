import json
import requests

def load_sites(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def test_xss(url, payload):
    try:
        response = requests.get(url, params={'input': payload})
        if payload in response.text:
            print(f"XSS vulnerability detected on {url} with payload: {payload}")
        else:
            print(f"No XSS vulnerability detected on {url}.")
    except requests.RequestException as e:
        print(f"Error testing {url}: {e}")

def main():
    sites_file = 'sites.json'
    payload = "<script>alert('m pako gen playload😓')</script>"
    sites = load_sites(sites_file)

    for site in sites:
        test_xss(site, payload)

if __name__ == "__main__":
    main()
