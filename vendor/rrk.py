#
# rrk.py
#
# This script holds functions for the vendor Rhino Rack
#
# Initial version - 02/19/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_rrk(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "RRK" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc] + " " + vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["P1"] * tech_cal["P5"]
    vendor_pandas["P4"] = (vendor_pandas["P5"] / tech_cal["P4"]).astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace('', '0').astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace('', '0').astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace('', '0').astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace('', '0').astype(float)

    return vendor_pandas

