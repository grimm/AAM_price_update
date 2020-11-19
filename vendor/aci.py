#
# aci.py
#
# This script holds functions for the vendor Agricover
#
# Initial version - 11/11/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_aci(vendor_pandas, prod_group, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "ACI" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Brand"] + " " + vendor_pandas["Product Line"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Long Description"]
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.replace('\"', 'in')
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.replace('\'', 'ft')
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].replace("$", "").replace(",", "")
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    vendor_pandas["P3"] = vendor_pandas["Jobber"].replace("$", "").replace(",", "")
    vendor_pandas["P3"] = vendor_pandas["P3"].replace("-", "0").astype(float)
    vendor_pandas["P3"] = vendor_pandas["P3"].astype(float)

    vendor_pandas["P5"] = vendor_pandas["Customer Price"]

    vendor_pandas["Customer Price"] = vendor_pandas["Customer Price"].replace("$", "").replace(",", "")
    vendor_pandas["Customer Price"] = vendor_pandas["Customer Price"].replace("-", "0")
    vendor_pandas["Customer Price"] = vendor_pandas["Customer Price"].astype(float)

    vendor_pandas["MAP"] = vendor_pandas["MAP"].replace("-", "0").astype(float)
    vendor_pandas["P2"] = vendor_pandas["P3"].astype(float)

    for index, item in enumerate(vendor_pandas["MAP"]):
        #print(index)
        if item == 0:
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index] / tech_cal["P2"]
        else:
            vendor_pandas["P2"][index] = item

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P2"]

    # Replace missing Jobber prices with MSRP
    for index, item in enumerate(vendor_pandas["MSRP"]):
        #print(index)
        if vendor_pandas["P3"][index] == 0.0:
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index]
            vendor_pandas["P3"][index] = vendor_pandas["P1"][index]
            vendor_pandas["P4"][index] = vendor_pandas["P1"][index]
            vendor_pandas["P5"][index] = vendor_pandas["Customer Price"][index]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Ship Weight"].replace("-", "0")
    vendor_pandas["Weight"] = vendor_pandas["Weight"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("-", "0")
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("-", "0")
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("-", "0")
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    # Set product groups
    vendor_pandas["Group"] = vendor_pandas["NewPart"]
    for index, item in enumerate(vendor_pandas["Brand"]):
        vendor_pandas["Group"][index] = 99999
        for key, value in prod_group.items():
            if item == key:
                vendor_pandas["Group"][index] = value
        if vendor_pandas["Group"][index] == 99999:
            print("******* Warning - " + item + " not found in product groups!")

    return vendor_pandas

