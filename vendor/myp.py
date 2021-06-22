#
# myp.py
#
# This script holds functions for the vendor Meyer Products
#
# Initial version - 06/22/2021 - Jason Grimes
#

from datetime import datetime
import pandas as pd
import unidecode
import csv

# Main vendor processing function
def do_myp(vendor_pandas, tech_cal):
    # Set price codes to pull out MYS parts
    mys_codes = ["MS", "MSP", "SAC1", "SS", "SSP", "US"]

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['PART NUMBER'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "MYP" + x)

    # Change part number prefix for MYS parts
    for index, code in enumerate(vendor_pandas["PRICE CODE"]):
        if code in mys_codes:
            vendor_pandas["NewPart"][index] = vendor_pandas["NewPart"][index].replace("MYP", "MYS")
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["DESCRIPTION"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"]

    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["LIST PRICE"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"] * tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["Level 3"].astype(float)

    # Set dimensions and status
    len_pandas = len(vendor_pandas.axes[0])
    print(len_pandas)
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = vendor_pandas["Weight (lbs.)"].astype(float)
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas
