#
# piaa.py
#
# This script holds functions for the vendor PIAA
#
# Initial version - 11/19/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_piaa(vendor_pandas, prod_group, tech_cal):
    # Remove parts with no pricing
    vendor_pandas = vendor_pandas.drop(vendor_pandas[(vendor_pandas['MSRP/List'] == "") & (vendor_pandas['Unilateral Retail'] == "")].index).reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "PIAA" + x)
    
    # Create new description columns
    long_desc = "Long Description 100 Characters or less WITHOUT application information"
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\"', 'in')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\'', 'ft')

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Unilateral Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Unilateral Wholesale"].astype(float)
    vendor_pandas["P5"] = (vendor_pandas["P3"] * tech_cal["P5"]).astype(float)

    # Set dimensions and status
    # Make sure that measurement values are correct
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0")
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0")

    vendor_pandas["Weight"] = vendor_pandas["Weight"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    # Set product groups
    short_desc = "Short Description (20 Characters or Less)"
    vendor_pandas["Group"] = vendor_pandas["NewPart"]
    for index, item in enumerate(vendor_pandas[short_desc]):
        vendor_pandas["Group"][index] = 99999
        for key, value in prod_group.items():
            if item == key:
                vendor_pandas["Group"][index] = value
        if vendor_pandas["Group"][index] == 99999:
            print("******* Warning - " + item + " not found in product groups!")

    return vendor_pandas

