# direct deposit strategy - revenue = end - start
import json
import os
from .modelBase import *


class dd(modelBase):
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def predict(self, stock_loader, volume=0, include_report=False):
    first_day_info = stock_loader.at(self.start)
    last_day_info = stock_loader.at(self.end)

    first_day_price = (
      first_day_info["Open"]
      + first_day_info["High"]
      + first_day_info["Low"]
      + first_day_info["Close"]
    ) / 4.0

    last_day_price = (
      last_day_info["Open"]
      + last_day_info["High"]
      + last_day_info["Low"]
      + last_day_info["Close"]
    ) / 4.0

    if volume != 0:
      purchase = (volume // first_day_price) * first_day_price
      sell = (volume // first_day_price) * last_day_price

      usage_rate = (purchase / volume) * 100
      earning_rate = (sell / purchase - 1.0) * 100
      adjusted_earning_rate = (sell - purchase) / volume * 100

      if include_report:
        print("\tusage_rate%\t\tER%\t\tAER%")
        print(
          "\t{:<11.2f}\t\t{:<3.2f}\t\t{:<4.2f}".format(
            usage_rate, earning_rate, adjusted_earning_rate
          )
        )

    return first_day_price, last_day_price
