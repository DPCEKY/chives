import datetime
import os
from .dfWriterBase import *
from .dfWriterDaily import *
from .dfWriterInfo import *
from .dfWriterOption import *
from .historical.wallstreet import Stock, Call, Put
import yfinance as yf
from time import sleep
import re

#  run outside the root dir

stock_names = [
  "fb",
  "goog",
  "aapl",
  "baba",
  "amzn",
  "msft",
  "tsla",
  "nio",
  "nflx",
  "pins",
  "snap",
  "uber",
  "lyft",
  "xpev",
  "twtr",
  "pdd",
  "bili",
  "ba",
  "snow",
  "crm",
  "abnb",
]


def get_last_friday_at_16(back_n_day=0):
  current_time = datetime.datetime.now()

  # get friday, one week ago, at 16 o'clock
  last_friday = (
    current_time.date()
    - datetime.timedelta(days=current_time.weekday())
    + datetime.timedelta(days=(4 - back_n_day), weeks=-1)
  )
  last_friday_at_16 = datetime.datetime.combine(last_friday, datetime.time(16))

  # if today is also friday, and after 16 o'clock, change to the current date
  one_week = datetime.timedelta(weeks=1)
  if current_time - last_friday_at_16 >= one_week:
    last_friday_at_16 += one_week
  return last_friday_at_16


def get_options(stock_name, df_writer, date, path):

  stock = yf.Ticker(stock_name)
  missed_options = []

  try:
    option_dates = stock.options
  except:
    print("connection jam. server returned error. sleep 3s and retry..")
    sleep(3)
    get_options(stock_name, df_writer, date, path)

  if len(option_dates) <= 0:
    print("cannot get option chain date. return..")
    return

  next_option_date = stock.options[0]

  options = stock.option_chain(next_option_date)
  calls_prices = list(options.calls.strike)
  puts_prices = list(options.puts.strike)

  for option_type in ["c", "p"]:
    prices = calls_prices if option_type == "c" else puts_prices
    for price in prices:
      price_str = str(int(price * 1000))
      price_symbol = "0" * (8 - len(price_str)) + price_str
      option_symbol = stock_name + date + option_type + price_symbol

      for i in range(2):
        option = yf.Ticker(option_symbol)
        df = option.history(period="max")
        if df.shape[0] <= 0:
          sleep(0.5)
        else:
          break

      if df.shape[0] <= 0:
        missed_options.append(option_symbol)
        continue

      df_writer.writeDfTo(path + option_type + "/", df, option_symbol)
      sleep(0.2)

  return missed_options


dfb = dfWriterOption()

# retrun the missed ones as yahoo limits requests in a certain peroid of time
missed_options = []

for stock_name in stock_names:
  date = get_last_friday_at_16().strftime("%Y%m%d")[2:]

  path = os.getcwd() + "/chives/datahut/data/option/" + stock_name + "/" + date + "/"

  missed_options_symbol = get_options(stock_name, dfb, date, path)

  missed_options.extend(missed_options_symbol)
