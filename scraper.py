import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
indeedURL = "https://au.indeed.com/?r=us"
authURL = "https://auth0.com/docs/authenticate/protocols/openid-connect-protocol"
page = requests.get(URL)
# print(page.text)
# print(page.cookies)
# print(page.raw)
soup = BeautifulSoup(page.content, "html.parser")