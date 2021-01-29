# Compare contract files
#
# IMS235 report
#
# Import modules
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import argparse
import os.path
from os import path
from datetime import datetime

# Parse command line options
parser = argparse.ArgumentParser(description='Compare contract files')
parser.add_argument('file1', help='First file')
parser.add_argument('file2', help='Second file')
args = parser.parse_args()

# Check to see if contract Excel files exists
if not path.isfile(args.file1):
    print("First file \"" + args.file1 + "\" does not exist!")
    exit(-1)

if not path.isfile(args.file2):
    print("Second file \"" + args.file2 + "\" does not exist!")
    exit(-1)

file1_pd = pd.read_excel(args.file1)
file2_pd = pd.read_excel(args.file2)

for index, item in enumerate(file1_pd["Customer Number"]):
  cont_num1 = file1_pd["Contract Number"][index]
  prod_code1 = file1_pd["PROD CODE   "][index]
  price1 = file1_pd["Price Formula #1"][index]

  for index2, item2 in enumerate(file2_pd["Customer"]):
    cont_num2 = file2_pd["Contract"][index2]
    prod_code2 = file2_pd["Product"][index2]
    price2 = file2_pd["Price"][index]

    if (item == item2) and (cont_num1 == cont_num2) and (prod_code1 == prod_code2):
      if not price1 == price2:
        print(item, cont_num1, prod_code1, price1, price2)
      break
