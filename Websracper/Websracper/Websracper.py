from bs4 import BeautifulSoup
import requests

url = 'http://ethans_fake_twitter_site.surge.sh/?ref=hackernoon.com'

response = requests.get(url, timeout=5)

content = BeautifulSoup(response.content, "html.parser")


print(content)