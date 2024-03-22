# automating tempo time registration
import requests 
from bs4 import BeautifulSoup

URL = "https://crayon-group.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-app#!/my-work/week?type=TIME"

# making GET request to see if we get valid response i.e. 200
page = requests.get(URL)

# forwarding the page content into parsing the html
soup = BeautifulSoup(page.content, "html.parser")

print(page.content) # you will receive raw content
