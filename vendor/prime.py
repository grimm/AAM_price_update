#
# prime.py
#
# This script holds functions for the vendor Prime Design
#
# Initial version - 01/13/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv
import pandas as pd

# Main vendor processing function
def do_prime(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Item'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "PRIME" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"]

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["2021 Retail Pricing"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["P1"] - (vendor_pandas["P1"] * 0.4)
    vendor_pandas["P2"] = vendor_pandas["P5"] / 0.7
    vendor_pandas["P3"] = vendor_pandas["P2"]

    # Get length of dataframe and create new P4 column with value of zero
    len_pandas = len(vendor_pandas.axes[0])
    vendor_pandas["P4"] = list("0" * len_pandas)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Unit Weight"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Weight"]
    vendor_pandas["Width"] = vendor_pandas["Weight"]
    vendor_pandas["Height"] = vendor_pandas["Weight"]

    for index, item in enumerate(vendor_pandas["Box Size"]):
        vendor_pandas["Length"][index] = 0
        vendor_pandas["Width"][index] = 0
        vendor_pandas["Height"][index] = 0

        if not item == "":
            if item.count('x') == 2:
                length, width, height = item.split("x")
            elif item.count('X') == 2:
                length, width, height = item.split("X")
            else:
                length, width, height = ["0", "0", "0"]

            vendor_pandas["Length"][index] = length
            vendor_pandas["Width"][index] = width
            vendor_pandas["Height"][index] = height

    return vendor_pandas

