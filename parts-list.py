# 
# parts-list.py
#
# This script converts a parts-list Excel file to a specially formated CSV file so it can be imported into
# the FACS system.
#
# 9-23-2020 - Initial Version 1.0  Jason Grimes
#

# Import modules
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import argparse
import os.path
from os import path
from datetime import datetime
import yaml
import csv

# Import helper functions
import vendor_func as ven
import run_vendor as run
import vendor_sheet as sheet

# Define the supported vendors and load yaml calculation and groups files
Vendors = ["aci", "adu", "ard", "baja", "big", "bkr", "buy", "carr", "curt", "deck",
           "eccon", "eccot", "fia", "gor", "gorm", "kar", "knk", "knn", "kso", "nfa",
           "odr", "par", "piaa", "prime", "protec", "rch", "rig", "road", "rrk", "rsp",
           "sb", "scs", "tech", "tim", "trux", "vms", "warn", "wes", "west", "yak"]
vendor_cal = {}
product_groups = {}

vnum = str(len(Vendors))
epilog = "The following " + vnum + " Vendors are supported: "
epilog = epilog + ", ".join(Vendors)

with open('vendor_cal.yaml') as f:
    vendor_cal = yaml.load(f, Loader=yaml.FullLoader)

with open('product_groups.yaml', encoding='utf8') as f:
    product_groups = yaml.load(f, Loader=yaml.FullLoader)

# Parse command line options
parser = argparse.ArgumentParser(description='Convert pricing Excel file to a CSV formated file', epilog = epilog)
parser.add_argument('file', help='Excel file')
parser.add_argument('vendor', help='Vendor name')
args = parser.parse_args()

# Check to see if vendor Excel files exists
if not path.isfile(args.file):
    print("File \"" + args.file + "\" does not exist!")
    exit(-1)

# Check that the specified vendor is supported
if not args.vendor in Vendors:
    print("\"" + args.vendor + "\" is not a supported vendor!")
    exit(-1)

# Import vendor functions
vendor = ven.vendor_func(args.vendor)

# Create CSV output file names
date = datetime.today().strftime('%m-%d-%y')
vname = args.vendor.upper()

if vname == "GORM":
    vname = "GOR"
elif vname == "ECCOT" or vname == "ECCON":
    vname = "ECCO"
    
titan_csv_file = vname + "_UPDATE_TTE_" + date + ".csv"
nelson_csv_file = vname + "_UPDATE_NTE_" + date + ".csv"

# Load vendor file using pandas
skiprow, sheet_name, multisheet, csvfile = sheet.set_excel(args.vendor)

if sheet_name == "" and csvfile == 0: # no sheet name
    vendor_pandas = pd.read_excel(args.file, keep_default_na=False, skiprows=skiprow)

elif not sheet_name == "": # read a specific sheet out of the Excel file
    vendor_pandas = pd.read_excel(args.file, keep_default_na=False, skiprows=skiprow, sheet_name=sheet_name)

elif multisheet == 1:      # Load multiple sheets, these get put into a dictionary
    vendor_pandas = pd.read_excel(args.file, keep_default_na=False, skiprows=skiprow, sheet_name=None)
elif csvfile == 1:         # Load CSV file instead of Excel
    vendor_pandas = pd.read_csv(args.file, keep_default_na=False)

# Create CSV file dictionary
# --------------------------
# Run vendor function and set columns
new_pandas, titan_columns, nelson_columns = run.vendor(vendor_pandas, vendor_cal,
    product_groups, args.vendor, vendor)

# Write CSV file
new_pandas.to_csv(titan_csv_file, columns=titan_columns, header=False, index=False, float_format="%.2f", sep="|", quoting=csv.QUOTE_NONE, escapechar='\\')
print("Saved - " + titan_csv_file)

if vendor_cal[args.vendor]["NTE"]:
    new_pandas.to_csv(nelson_csv_file, columns=nelson_columns, header=False, index=False, float_format="%.2f", sep="|", quoting=csv.QUOTE_NONE)
    print("Saved - " + nelson_csv_file)

