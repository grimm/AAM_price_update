#! /usr/bin/python3
# 
# conv_price.py
#
# This script converts a vendor parts Excel file to a specially formated CSV file so it
# can be imported into the FACS system.
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
import os
from sys import platform

# Import helper functions
import vendor_func as ven
import run_vendor as run
import vendor_sheet as sheet

# Define the supported vendors and load yaml calculation and groups files
Vendors = ["aci", "adu", "airl", "and", "anz", "amp", "ampm", "aor", "arb", "arcl", "ard",
           "baja", "bak", "bap", "best", "big", "bigm", "bkr", "brm", "btr", "bush", "buy",
           "carr", "cbp", "cipa", "cog", "crg", "curt", "deck", "dez", "eccon", "eccot", "ele",
           "ext", "ffi", "fia", "fil", "fire", "fpm", "gor", "gorm", "hus", "kar", "kc", "kln",
           "knk", "knkm", "knn", "kso", "lift", "lnd", "luv", "mas", "mass", "mba", "mrw",
           "myp", "nfa", "nitro", "odr", "ovs", "par", "piaa", "prime", "protec", "put", "qf",
           "rch", "rcs", "rdl", "rfn", "rgr", "rig", "rlg", "rnl", "road", "rrk", "trm", "rsp",
           "rtx", "rug", "sb", "scs", "sls", "snow", "stlc", "tech", "tfi", "tft", "tim",
           "t-rex", "trux", "truxm", "und", "uws", "uwsb", "ven", "vms", "warn", "wes", "west",
           "yak", "zll"]
vendor_cal = {}
product_groups = {}

vnum = str(len(Vendors))
epilog = "The following " + vnum + " Vendor product codes are supported: "
epilog = epilog + ", ".join(Vendors)

with open('vendor_cal.yaml') as f:
    vendor_cal = yaml.load(f, Loader=yaml.FullLoader)

with open('product_groups.yaml', encoding='utf8') as f:
    product_groups = yaml.load(f, Loader=yaml.FullLoader)

# Parse command line options
parser = argparse.ArgumentParser(description='Convert pricing Excel file to a CSV formated file', epilog = epilog)
parser.add_argument('file', help='Excel file')
parser.add_argument('vendor', help='Vendor Product Code')
parser.add_argument('-d', help='Process all parts as discontinued', action="store_true")
parser.add_argument('-n', help='Do new calculation', action="store_true")
parser.description = "The mass vendor is used to import data from the FACS mass report"
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
if vname == "ECCOT" or vname == "ECCON":
    vname = "ECCO"
if vname == "AMPM":
    vname = "AMP"
if vname == "KNKM":
    vname = "KNK"
if vname == "UWSB":
    vname = "UWS"
if vname == "TRUXM":
    vname = "TRUX"
    
titan_csv_file = vname + "_UPDATE_TTE_" + date + ".csv"
nelson_csv_file = vname + "_UPDATE_NTE_" + date + ".csv"

# Load vendor file using pandas
skiprow, sheet_name, multisheet, csvfile = sheet.set_excel(args.vendor)

if sheet_name == "" and csvfile == 0 and not multisheet: # no sheet name
    vendor_pandas = pd.read_excel(args.file, keep_default_na=False, skiprows=skiprow)

elif not sheet_name == "":   # read a specific sheet out of the Excel file
    vendor_pandas = pd.read_excel(args.file, keep_default_na=False, skiprows=skiprow, sheet_name=sheet_name)

elif multisheet:             # Load multiple sheets, these get put into a dictionary
    vendor_pandas = pd.read_excel(args.file, keep_default_na=False, skiprows=skiprow, sheet_name= multisheet)
elif csvfile == 1:           # Load CSV file instead of Excel
    vendor_pandas = pd.read_csv(args.file, keep_default_na=False)

# Create CSV file dictionary
# --------------------------
# Run vendor function and set columns
new_pandas, titan_columns, nelson_columns = run.vendor(vendor_pandas, vendor_cal,
    product_groups, args.vendor, vendor, args.d, args.n)

# Write CSV file
new_pandas.to_csv(titan_csv_file, columns=titan_columns, header=False, index=False, float_format="%.2f", sep="|", quoting=csv.QUOTE_NONE, escapechar='\\')
print("Saved - " + titan_csv_file)
if platform == "linux":
    os.system("unix2dos " + titan_csv_file)

if vendor_cal[args.vendor]["NTE"]:
    new_pandas.to_csv(nelson_csv_file, columns=nelson_columns, header=False, index=False, float_format="%.2f", sep="|", quoting=csv.QUOTE_NONE)
    print("Saved - " + nelson_csv_file)
    if platform == "linux":
        os.system("unix2dos " + nelson_csv_file)

