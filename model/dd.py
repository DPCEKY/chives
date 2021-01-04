# direct deposit strategy - revenue = end - start
import json
import os
from .modelBase import *


class dd(modelBase):
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def predict(self, stock_loader):
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

    return first_day_price, last_day_price