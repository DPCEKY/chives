#!/usr/bin/python

import sys
from .oeLoader import oeLoader


class oeExecutor:
  def __init__(
    self, oe_name="example_expt_0", expt="expt", control="control", test="test"
  ):
    # self.oe_name = oe_name
    # self.expt = expt
    # self.control = control
    # self.test = test

    self.expt = oeLoader(oe_name, expt, control, test)

  def execute(self):
    control_models = self.expt.control_models

    print("*" * 20)
    print("*" * 20)
    for name in control_models:
      print("model name = {}".format(name))

      model = control_models[name]
      
      # take first stock only for now
      stock_name = self.expt.expt_cfg["stocks"][0]["symbol"]
      stock = self.expt.stocks[stock_name]
      volume = self.expt.expt_cfg["volume"]
      include_report = self.expt.expt_cfg["include_report"]
      model.predict(stock, volume, include_report)

    print("*" * 20)
    print("*" * 20)

    return


if __name__ == "__main__":

  expt_name = "example_expt_0"
  test_arm = "test"

  param_num = len(sys.argv)
  if param_num > 1:
    expt_name = sys.argv[1]
  if param_num > 2:
    test_arm = sys.argv[2]

  oe_executor = oeExecutor(oe_name=expt_name, test=test_arm)
  oe_executor.execute()
