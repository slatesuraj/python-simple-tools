import argparse
import requests

class URLShortener:
    def __init__(self, api_key):
        self.api_key = api_key

    def shorten_url(self, long_url):
        url = f"https://api.tinyurl.com/dev/api-create.php?url={long_url}&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            short_url = response.text.strip()
            print(f"Short URL: {short_url}")
        else:
            print(f"Error: Unable to shorten the URL. {response.text}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='URL Shortener CLI')
    parser.add_argument('api_key', help='TinyURL API key')
    parser.add_argument('long_url', help='Long URL to be shortened')

    args = parser.parse_args()

    url_shortener = URLShortener(args.api_key)
    url_shortener.shorten_url(args.long_url)
