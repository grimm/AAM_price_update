#
# warn.py
#
# This script holds functions for the vendor KSource
#
# Initial version - 10/29/2020 - Jason Grimes
#

# Note: You must manually un-merge the Description header cell and name the next column
# "Extra"

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_kso(vendor_pandas, tech_cal):
    # Filter out all rows that are just headers/info
    # vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas = vendor_pandas[(vendor_pandas["New Jobber"] != "")]

    # Create new Status/NewPart columns
    vendor_pandas['Part No.'] = vendor_pandas['Part No.'].astype(str)
    vendor_pandas['Part Number'] = vendor_pandas['Part No.']
    vendor_pandas["NewPart"] = vendor_pandas["Part No."].apply(lambda x: "KSO" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["Sugg. Retail"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Sugg. Dealer"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["New Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Wt."].astype(float)

    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas

