import requests

def check_website(url):
    if not url:
        print("No URL entered. Please try again.")
        return
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is ONLINE ✅")
        else:
            print(f"{url} is reachable but returned status code {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url} is OFFLINE ❌")

if __name__ == "__main__":
    target_url = input("Enter website URL (e.g., https://www.google.com): ").strip()
    check_website(target_url)
