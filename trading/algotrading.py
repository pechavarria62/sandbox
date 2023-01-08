import pandas_datareader.data as web

import pandas as pd

import datetime as dt

df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')
df.head()