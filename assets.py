import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import sqlalchemy as db
from functions import *

'''
main = pd.concat(series_list)
print(main)'''


first, first_prices = create_port(['AAPL', 'MSFT', 'GOOGL'], 'FIRST', '1y')
'''
second = create_port(['AAPL', 'TSLA', 'BILI'], 'SECOND')
portfolios = pd.concat([first, second])
print(portfolios)'''

'''
main = init_port(3, ['AAPL', 'MSFT', 'GOOGL'], 'one')
print(main)'''
print(first)
print(first_prices)

