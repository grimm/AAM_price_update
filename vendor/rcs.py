#
# rcs.py
#
# This script holds functions for the vendor Rough Country Suspension
#
# Initial version - 05/03/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_rcs(vendor_pandas, tech_cal):
    # Remove clothing
    vendor_pandas = vendor_pandas[(vendor_pandas["sku"].str[:2] != "84")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['sku'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "RCS" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["title"].replace("\|", "", regex=True)

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["cost"].astype(float)
    vendor_pandas["P1"] = vendor_pandas["price"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Measurements
    vendor_pandas["Length"] = vendor_pandas["length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["height"].replace("", "0").astype(float)
    vendor_pandas["Weight"] = vendor_pandas["weight"].replace("", "0").astype(float)

    # Group codes
    vendor_pandas["Group Code"] = vendor_pandas["P1"]
    for index, item in enumerate(vendor_pandas["category"]):
        if item == "Wheels":
            vendor_pandas["Group Code"][index] = 1
        else:
            vendor_pandas["Group Code"][index] = 0
    vendor_pandas["Group Code"] = vendor_pandas["Group Code"].astype(int)

    return vendor_pandas

