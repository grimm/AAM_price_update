#
# rtx.py
#
# This script holds functions for the vendor Retrax (Applied Products)
#
# Initial version - 5/03/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_rtx(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "RTX" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc] + " " + vendor_pandas["Application"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["MAP Wholesale / MSP"]
    for index, item in enumerate(vendor_pandas["P4"]):
        if item == "N/A":
            vendor_pandas["P4"][index] = vendor_pandas["P3"][index]
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)
    
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)
    
    return vendor_pandas

