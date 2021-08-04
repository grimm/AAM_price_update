#
# west.py
#
# This script holds functions for the vendor Western
#
# Initial version - 02/01/2021 - Jason Grimes
#

from datetime import datetime
import csv

# Main vendor processing function
def do_west(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    long_desc = "DESCRIPTION"
    short_desc = "DESCRIPTION 2 "

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["PN"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WEST" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].astype(str) + " " + vendor_pandas[short_desc].astype(str)

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["LIST PRICE"].replace("$","").replace(",", "").astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"] * tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P1"] * tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["P1"] * tech_cal["P5"]

    # Set dimensions and status
    # Get length of dataframe and create new dimension columns
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas
