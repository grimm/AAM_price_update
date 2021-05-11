#
# trux.py
#
# This script holds functions for the vendor Truxedo
#
# Initial version - 1/20/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_trux(vendor_pandas, prod_group, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "TRUX" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc] + " " + vendor_pandas["Application"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    for index, item in enumerate(vendor_pandas["P1"]):
        if item == "" or item =="n/a":
            vendor_pandas["P1"][index] = vendor_pandas["P3"][index]

    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    for index, item in enumerate(vendor_pandas["MAP Retail"]):
        #print(index)
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index]

    vendor_pandas["P2"] = vendor_pandas["P2"]
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "" or item =="n/a":
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index]


    vendor_pandas["P4"] = vendor_pandas["MAP Wholesale / MSP"]
    for index, item in enumerate(vendor_pandas["MAP Wholesale / MSP"]):
        #print(index)
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(str).apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(str).apply(lambda x: x.strip('"'))
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)

    vendor_pandas["Height"] = vendor_pandas["Height"].astype(str).apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(str).apply(lambda x: x.strip('"'))
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    vendor_pandas["Width"] = vendor_pandas["Width"].astype(str).apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(str).apply(lambda x: x.strip('"'))
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)

    # Set product groups
    vendor_pandas["Group Code"] = vendor_pandas["NewPart"]
    for index, item in enumerate(vendor_pandas[long_desc]):
        vendor_pandas["Group Code"][index] = 99999
        for key, value in prod_group.items():
            if item == key:
                vendor_pandas["Group Code"][index] = value
        if vendor_pandas["Group Code"][index] == 99999:
            # print("******* Warning - " + item + " not found in product groups!")
            print(item)

    return vendor_pandas

