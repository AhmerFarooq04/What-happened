import pandas as pd
import requests
import yfinance as yf
from googlesearch import search

stock = input("what stock do you want to analyze? ")
data = yf.download(stock, period="max")
close=data.loc[:,"Close"].copy()
closedf = pd.DataFrame({'price': close})
closedf["yestprice"]= closedf.shift(periods=1)
closedf.dropna(inplace=True)
closedf.drop(closedf.index[-1], inplace=True)
closedf["percentchange"] = closedf[['yestprice', 'price']].pct_change(axis=1)['price'].mul(100)
perc_comp = input("what percent change do you want to compare to? ")
if float(perc_comp) >= 0:
  closedf_grt3 = closedf[closedf['percentchange'] > float(perc_comp)]
else :
  closedf_grt3 = closedf[closedf['percentchange'] < float(perc_comp)]
print(closedf_grt3)
date = input("which day would you like to know about? (Copy the date) ")
query = f"{date} {stock} what happened"
for j in search(query):
  print(j)