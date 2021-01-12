#
# wes.py
#
# This script holds functions for the vendor Westin
#
# Initial version - 1/12/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_wes(vendor_pandas, prod_group, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part#'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WES" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Product"] + " " + vendor_pandas["Application Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber Price"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Net Line Price"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P3"]
    for index, item in enumerate(vendor_pandas["MAP Retail"]):
        #print(index)
        if item == 0:
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index] * tech_cal["P2"]
        else:
            vendor_pandas["P2"][index] = item

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Wt"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["L"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["W"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["H"].replace(" ", "0").replace("", "0").astype(float)

    # Set product groups
    vendor_pandas["Group"] = vendor_pandas["NewPart"]
    for index, item in enumerate(vendor_pandas["Product"]):
        vendor_pandas["Group"][index] = 99999
        for key, value in prod_group.items():
            if item == key:
                vendor_pandas["Group"][index] = value
        if vendor_pandas["Group"][index] == 99999:
            print("******* Warning - " + item + " not found in product groups!")
            # print(item)

    return vendor_pandas

