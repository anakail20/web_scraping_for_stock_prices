################################ IMPORTING LIBRARIES ################################


import pandas as pd
import requests
from bs4 import BeautifulSoup


## Creating a get request to the website and store the page object in a variable

page  = requests.get("https://www.fool.com/investing/top-stocks-to-buy.aspx")
page


## View the HTML page 
page.content


## Create a soup object and parse the page content to it
soup = BeautifulSoup(page.content, 'html.parser')


## View the page content 
print(soup.prettify()) # now the HTML text is readable, which will help us identify the tags that contain data we want


## Even though it is readable, it is not easy to interact with,so we will use Google Chrome’s developer tools to identify the tags that contain the data we want to scrape

# https://www.fool.com/investing/top-stocks-to-buy.aspx  <- this is the website
# Next, locate the Stocks section of the website
# Our main goal is to scrape the list of stocks and build a dataset from it. So now let’s right-click the Stocks section and select ‘inspect’

## We isolate the Stocks section of the webpage and create a subset of our page content and store it in a variable


stocks = soup.find(class_='related-tickers')
stocks


## At the stocks object we will earch for all the tags with the class name ‘ticker-text-wrap’ and create a list with it
stock_picks = stocks.find_all(class_='ticker-text-wrap')
stock_picks # Now we have all the stocks and the information on each stock stored in a list, this will allow us to loop through the list and extract information on each stock

## We will build our dataset , firstly get all the company names of each stock and store it in a list
# Get stock names
stock_names = []
for stock in stock_picks:
    stock_names.append(stock.h3.get_text())

stock_names

stock_names=stock_names[:-3]

## Extract the stock symbols 
# Get stock symbol
stock_symbol = []
for stock in stock_picks:
    stock_symbol.append(stock.a.span.get_text())


## We want all the arrays to have the same lenght so that we delete 3 rows ( something is wrong with the data here)
stock_symbol=stock_symbol[:-3] # we should not do that but it is nessecary to proceed


## Extract the price of each stock
# Get Current Price
# current_price = []
# for stock in stock_picks:
#     price = stock.h4.h4.get_text()
#     current_price.append(price.strip())

current_price_class= stocks.find_all(class_='current-price')
current_price = []

for stock in current_price_class:
    price = stock.get_text()
    current_price.append(price.strip())



## Search for the price change amount to get the price change values 
price_change = stocks.find_all(class_='price-change-amount')
# Get Change Price
change_price = []
for change in price_change:
    price = change.get_text()
    change_price.append(price.strip())

change_price


## Search for the percentage of price change
percent_change = stocks.find_all(class_='price-change-percent')
# Get Change Percent
change_pct = []
for pct in percent_change:
    price = pct.get_text()
    change_pct.append(price.strip())

change_pct


## Create a dictionary from all of our lists

data = {'Symbol':stock_symbol, 'Company':stock_names, 'Price':current_price, 'PriceChange':change_price, 'PercentChange':change_pct}
    
    
## Create the data frame
df = pd.DataFrame(data)
