#
# bush.py
#
# This script holds functions for the vendor Bush Master
#
# Initial version - 02/25/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_bush(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "BUSH" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["PF Desc"] + " " + vendor_pandas["Product Class"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["MAP"].astype(float)
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == 0:
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index]

    vendor_pandas["P5"] = vendor_pandas["P3"] * 0.7 * 0.9
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column
    vendor_pandas["Weight"] = new_column

    return vendor_pandas

