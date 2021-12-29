#
# kln.py
#
# This script holds functions for the vendor Kleinn
#
# Initial version - 11/23/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv
import pandas as pd

# Main vendor processing function
def do_kln(vendor_pandas, tech_cal):
    long_desc = "Long Description (100 Character)"

    # Strip out parts with no pricing
    vendor_pandas = vendor_pandas[(vendor_pandas["List Price "] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["MAP PRICE"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Remove discontinued parts
    vendor_pandas = vendor_pandas[~(vendor_pandas[long_desc].str.contains("DISCONTINUED"))]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "KLN" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"]

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["List Price "].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP PRICE"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber Price "].astype(float)

    vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Shipping Weight"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width "].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    return vendor_pandas

