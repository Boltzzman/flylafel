from bs4 import BeautifulSoup
import requests

source = "https://www.skatedeluxe.com/en/skateboard-decks?brand_id=509"

# fetch the content from url
page_response = requests.get(source, timeout=5)

# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where price is stored
containers = page_content.findAll("div", {"class": "listing-product"})


for container in containers:

    brand = container.findAll("div", {"class": "listing-product-manufacturer"})

    print(brand)







