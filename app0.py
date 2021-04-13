from bs4 import BeautifulSoup

from requests_html import HTMLSession
session = HTMLSession()
# <span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">₹&nbsp;3,699.00</span>
request = session.get("https://www.amazon.in/Chairs-Delta-Chair-Umbrella-Office/dp/B07GJYBFW1/ref=sr_1_5?dchild=1&keywords=chair+computer&qid=1595944003&sr=8-5")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice" , "class" : "a-size-medium a-color-price priceBlockBuyingPriceString"})
price_with_symbol =element.text.strip()
price = price_with_symbol[2:]
new_price = price[0]+price[2:]
cost = float(new_price)
if(cost<4000):
    print("you should buy it")
    print("current price is {}".format(price_with_symbol))
else:
    print("expensive")


