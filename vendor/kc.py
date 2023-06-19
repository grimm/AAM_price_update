#
# kc.py
#
# This script holds functions for the vendor KC Hilights
#
# Initial version - 07/30/2021 - Jason Grimes
#

import unidecode

# Main vendor processing function
def do_kc(vendor_pandas, tech_cal):
    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["SKU"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "KC" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["PRODUCT NAME"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")
    
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["UPCOMING MAP"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["UPCOMING DIR FIXED COST"]

    vendor_pandas["P2"] = vendor_pandas["P1"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P1"].astype(float)

    for index, item in enumerate(vendor_pandas["P5"]):
        if item == "":
            vendor_pandas["P5"][index] = (vendor_pandas["P1"][index] * tech_cal["P5"])
    vendor_pandas["P5"] = vendor_pandas["P5"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["BOX 1 WT (LBS)"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["BOX 1 L"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["BOX 1 H"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["BOX 1 W"].replace("", "0").astype(float)

    return vendor_pandas
