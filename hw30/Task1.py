import requests
import random

url = ['https://www.google.com/', 'https://www.facebook.com/', 'https://twitter.com/', 'https://www.amazon.com/', 'https://www.apple.com/']
url = random.choice(url)
response = requests.get(url)

status_code = response.status_code
website_name = url.split('//')[1]
html_length = len(response.text)


print(f'Status code: {status_code}')
print(f"Website name: {website_name}")
print(f"HTML length: {html_length}")

