from dfWriterBase import *
from historical.wallstreet import Stock, Call, Put

dfb = dfWriterBase()
path='../datahut/data/historical/goog/'
s = Stock('goog')
df = s.historical(days_back=40, frequency='d')

dfb.writeDfTo(path, df)