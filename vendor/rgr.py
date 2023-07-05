#
# rgr.py
#
# This script holds functions for the vendor Rugged Ridge
#
# Initial version - 07/08/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import re

# Main vendor processing function
def do_rgr(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Process part number
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "RGR" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].astype(str)
    # vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("|", "-")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    for index, item in enumerate(vendor_pandas["MAP Retail"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index] * tech_cal["P2"]
        else:
            vendor_pandas["P2"][index] = item
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)

    for index, item in enumerate(vendor_pandas["P1"]):
        if item == "":
            vendor_pandas["P1"][index] = vendor_pandas["P2"][index]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"]

    # Make sure that measurement values are correct
    vendor_pandas["Weight"] = vendor_pandas["Weight"].replace("", "0")
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0")

    return vendor_pandas
