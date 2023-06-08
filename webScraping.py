import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.amazon.in/")
soup = BeautifulSoup(data.content, 'html.parser')
print(soup.prettify())
