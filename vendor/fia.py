#
# fia.py
#
# This script holds functions for the vendor FIA
#
# Initial version - 10/14/2020 - Jason Grimes
#

from datetime import datetime
import csv

# Main vendor processing function
def do_fia(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Process part number
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].str.replace(' ', '')
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "FIA" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc2"] = vendor_pandas[long_desc]

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"]
    vendor_pandas["P2"] = vendor_pandas["P3"] / tech_cal["P2"]
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"]

    # Make sure that measurement values are correct
    vendor_pandas = vendor_pandas.replace("N/A", "0")

    return vendor_pandas
