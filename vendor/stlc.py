#
# stlc.py
#
# This script holds functions for the vendor Steelcraft
#
# Initial version - 08/06/2021 - Jason Grimes
#

from datetime import datetime
import re
import unidecode

# Main vendor processing function
def do_stlc(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Filter out all install kit parts
    vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    vendor_pandas["Part Number"] = vendor_pandas["Part Number"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "STLC" + x)
    
    # Create new description columns and replace quotes
    vendor_pandas["Desc1"] = vendor_pandas[long_desc] + " " + vendor_pandas["Application"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace(r"|","-")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]
    vendor_pandas["P1"] = vendor_pandas["P4"] / tech_cal["P1"]

    for index, item in enumerate(vendor_pandas["P2"]):
        #print(index)
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P4"][index] / tech_cal["P2"]

    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("","0")
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("","0")
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("","0")
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("","0")

    return vendor_pandas
