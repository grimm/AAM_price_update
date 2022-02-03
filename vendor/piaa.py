#
# piaa.py
#
# This script holds functions for the vendor PIAA
#
# Initial version - 11/19/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_piaa(vendor_pandas, tech_cal):
    # Remove parts with no pricing
    # vendor_pandas = vendor_pandas.drop(vendor_pandas[(vendor_pandas['MSRP/List'] == "") & (vendor_pandas['Unilateral Retail'] == "")].index).reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['PIAA Part #'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "PIAA" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Product Description (Detailed)"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\"', 'in')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\'', 'ft')

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Revised 2022 Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["NET PRICE"]

    vendor_pandas["P1"] = vendor_pandas["P3"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P3"] / tech_cal["P2"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    # Make sure that measurement values are correct
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Height"] = new_column
    vendor_pandas["Width"] = new_column

    # Set product groups
    vendor_pandas["Group"] = new_column

    return vendor_pandas

