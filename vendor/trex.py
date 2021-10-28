#
# t-rex.py
#
# This script holds functions for the vendor T-Rex Grilles
#
# Initial version - 10/28/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_trex(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "T-REX" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc] + " " + vendor_pandas["Application"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Unilateral Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Unilateral Wholesale"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    # for index, item in enumerate(vendor_pandas["P1"]):
    #     if item == "" or item =="n/a":
    #         vendor_pandas["P1"][index] = vendor_pandas["P3"][index]


    # for index, item in enumerate(vendor_pandas["MAP Retail"]):
        #print(index)
    #     if item == "":
    #         vendor_pandas["P2"][index] = vendor_pandas["P3"][index]

    # for index, item in enumerate(vendor_pandas["P2"]):
    #     if item == "" or item =="n/a":
    #         vendor_pandas["P2"][index] = vendor_pandas["P3"][index]

    # for index, item in enumerate(vendor_pandas["MAP Wholesale / MSP"]):
        #print(index)
    #     if item == "":
    #         vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]
            # new Calculation
            # vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P6"]
    # vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)
    # vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
    # vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)

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

    return vendor_pandas

