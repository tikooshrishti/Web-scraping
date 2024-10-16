import pandas as pd
from bs4 import BeautifulSoup
import requests

Product_name = []
Prices = []
Reviews = []

for i in range(2,11):
    url = "https://www.amazon.in/s?k=laptops+under+35000"
    source = requests.get(url)
    # print(source)

    soup = BeautifulSoup(source.text,"lxml")
    # print(soup)

    names = soup.find_all("div", class_="a-section a-spacing-none puis-padding-right-small s-title-instructions-style")
    print(names)

    for i in names:
        name = i.text
        Product_name.append(name)
    # print(len(Product_name))

    prices = soup.find_all("div", class_="a-row a-size-base a-color-base")

    for i in prices:
        name = i.text
        Prices.append(name)
    # print(len(Prices))

    review = soup.find_all("div", class_="a-row a-size-small")

    for i in review:
        name = i.text
        Reviews.append(name)
    # print(len(Reviews))

df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Reviews": Reviews})
# print(df)

df.to_csv("D:/Laptops_under_35000")








# while True:
#     np = soup.find("a", class_ = "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator").get("href")
#     cnp = "https://www.amazon.in" + np
#     print(cnp)

        # url = cnp
        # source = requests.get(url)
        # soup = BeautifulSoup(source.text,"lxml")