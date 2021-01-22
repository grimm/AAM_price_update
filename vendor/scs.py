#
# scs.py
#
# This script holds functions for the vendor Scosche
#
# Initial version - 01/21/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv
import pandas as pd

# Main vendor processing function
def do_scs(vendor_pandas, tech_cal):
    # Remove promotional displays
    short_desc = "Short Description (20 Characters or Less)"
    vendor_pandas = vendor_pandas[~(vendor_pandas[short_desc].str.contains("Display"))]
    vendor_pandas = vendor_pandas[~(vendor_pandas[short_desc].str.contains("Banner"))]

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "SCS" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"]

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)

    vendor_pandas["P5"] = vendor_pandas["AAM Cost"]
    for index, item in enumerate(vendor_pandas["P5"]):
        if item == "":
            vendor_pandas["P5"][index] = vendor_pandas["P3"][index]
    vendor_pandas["P5"] = vendor_pandas["P5"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    for index, item in enumerate(vendor_pandas["P1"]):
        if item == "":
            vendor_pandas["P1"][index] = vendor_pandas["P3"][index]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
            
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index]
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
            
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    return vendor_pandas

