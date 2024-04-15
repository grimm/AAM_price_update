#! /usr/bin/python3
# 

# Import modules
import pandas as pd
import argparse
import yaml

# Parse command line options
parser = argparse.ArgumentParser(description='Fix TECH groups')
parser.add_argument('file', help='Excel file')
args = parser.parse_args()

# Load excel file
vendor_pandas = pd.read_excel(args.file, keep_default_na=False)

# Load YAML groups file
with open('product_groups.yaml', encoding='utf8') as f:
    product_groups = yaml.load(f, Loader=yaml.FullLoader)

# product_groups = product_groups["tech"]

# Build group codes column (normal)
vendor_pandas["Group"] = vendor_pandas["CODE"]

for index, item in enumerate(vendor_pandas["Part Description"]):
    vendor_pandas["Group"][index] = 99999
    # split apart the description to get the text to compare
    
    for key, value in prod_group["tech"].items():
        if item == key:
            vendor_pandas["Group"][index] = value
        if vendor_pandas["Make"][index] == "Ferrari" or vendor_pandas["Make"][index] == "Bugatti":
            vendor_pandas["Group"][index] = 0
    if vendor_pandas["Group"][index] == 99999:
        # print("******* Warning - " + item + " not found in product groups!")
        # print(item + "*")
        print(item)

