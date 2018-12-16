from bs4 import BeautifulSoup
import requests

source = "https://www.ryanair.com/gb/en/cheap-flights/?from=SXF&out-from-date=2018-12-03&out-to-date=2019-03-" \
         "03&budget=150"

# fetch the content from url
page_response = requests.get(source, timeout=5)

# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where price is stored
containers = page_content.findAll("div", {"class": "list-card"})


for container in containers:

    container.find('span', "ng-class")








