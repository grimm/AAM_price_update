#
# rch.py
#
# This script holds functions for the vendor Ranch Hand
#
# Initial version - 01/20/2020 - Jason Grimes
#

from datetime import datetime
import csv

# Main vendor processing function
def do_rch(vendor_pandas, tech_cal):
    # Remove parts with no pricing
    vendor_pandas = vendor_pandas[(vendor_pandas['Jobber'] != "Call for pricing")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["MAP Retail"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP/List"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

	# Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Process part number
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "RCH" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc] + " " + vendor_pandas["Application"]

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Unilateral Wholesale"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    # Replace missing values in P2
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index]

    # Replace missing values in P4
    for index, item in enumerate(vendor_pandas["P4"]):
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]

    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("N/A", "0")
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0").astype(float)

    return vendor_pandas
