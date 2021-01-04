import json
import os
import pandas as pd
from ..datahut.data_loader import data_loader



class exptLoader:
  def __init__(
    self, oe_name="example_expt_0", expt="expt", control="control", test="test"
  ):
    self.expt_cfg = {}
    self.control_cfg = {}
    self.test_cfg = {}
    self.stocks = []

    self.__load_cfg(oe_name, expt, control, test)

  def __load_cfg(self, oe_name, expt, control, test):
    oe_path = os.getcwd() + "/chives/oe/oe_test/" + oe_name + "/"

    if not os.path.exists(oe_path):
      print("empty {} input! return..".format(oe_path))
      return

    # Opening JSON file
    expt_cfg_ptr = open(oe_path + expt + ".json")
    control_cfg_ptr = open(oe_path + control + ".json")
    test_cfg_ptr = open(oe_path + test + ".json")

    # returns JSON object as a dictionary
    self.expt_cfg = json.load(expt_cfg_ptr)
    self.control_cfg = json.load(control_cfg_ptr)
    self.test_cfg = json.load(test_cfg_ptr)

    # Closing file
    expt_cfg_ptr.close()
    control_cfg_ptr.close()
    test_cfg_ptr.close()

    self.__load_data(oe_name, expt, control, test)

    return self.expt_cfg, self.control_cfg, self.test_cfg

  def __load_data(self, oe_name, expt, control, test):
    stocks_cfg = self.expt_cfg["stocks"]
    symbols = []
    for stock in stocks_cfg:
      symbols.append(stock["symbol"])

    load_path = os.path.abspath(os.getcwd() + "/chives/datahut/data/")
    print("[oe_loader] load_path = {}".format(load_path))

    mode = self.expt_cfg["time_range"]["mode"]

    for symbol in symbols:
      stock = data_loader(symbol=symbol, load_path=load_path, mode=mode)
      # print(stock.at("2012-05-21"))
      self.stocks.append(stock)


if __name__ == "__main__":
  expt = exptLoader()

  # data = loader.load_cfg()
  # print(data[0])
  # print("*" * 20)

  # print(data[1])
  # print("*" * 20)
  # print(data[2])

  # print("2020-10" > "2020-11")
  # print("2020-10" <= "2020-11")
  # print("2020-10-31" <= "2020-11")
  # print("2020-10" <= "2020-11-02")

  # print("2020-09-22" > "2020-01-23")
  # print("2020-09-22" <= "2020-01-23")
