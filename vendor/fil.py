#
# fil.py
#
# This script holds functions for the vendor Fillrite Pumps
#
# Initial version - 02/22/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_fil(vendor_pandas, tech_cal):
    # Remove bad rows
    vendor_pandas = vendor_pandas[(vendor_pandas["NET PRICE\n"] != "Request Pricing")]
    vendor_pandas = vendor_pandas[(vendor_pandas["LIST PRICE"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)
    
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Model'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "FIL" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Product Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["LIST PRICE"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["NET PRICE\n"].astype(float)
    vendor_pandas["P2"] = (vendor_pandas["P5"] / tech_cal["P2"])
    vendor_pandas["P3"] = (vendor_pandas["P5"] / tech_cal["P3"])
    vendor_pandas["P4"] = vendor_pandas["MAP\nUNITED STATES"].replace('', '0').astype(float)

    for index, item in enumerate(vendor_pandas["P4"]):
        if item == 0:
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / 0.8

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["LB"].replace('', '0').replace('N/A', '0').astype(float)

    return vendor_pandas

