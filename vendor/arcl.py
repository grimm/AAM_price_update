#
# anz.py
#
# This script holds functions for the vendor Arc Lighting
#
# Initial version - 7/29/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_arcl(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Create new Status/NewPart columns
    # vendor_pandas["Part Number"] = vendor_pandas["SKU"].astype(str)
    vendor_pandas["Part Number"] = vendor_pandas["Part Number"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "ARCL" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["WD"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    # process P1 for missing values
    for index, item in enumerate(vendor_pandas["P1"]):
        if item == "":
            vendor_pandas["P1"][index] = vendor_pandas["P2"][index]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    # process P4 for missing values
    for index, item in enumerate(vendor_pandas["P4"]):
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    # Set dimensions
    # len_pandas = len(vendor_pandas.axes[0])
    # new_column = list("0" * len_pandas)

    # vendor_pandas["Weight"] = new_column
    # vendor_pandas["Length"] = new_column
    # vendor_pandas["Width"] = new_column
    # vendor_pandas["Height"] = new_column

    # Set dimensions
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("/", "0").replace("","0")
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("NA","0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("/", "0").replace("","0")
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("NA", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("/", "0").replace("","0")
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("NA","0").astype(float)

    return vendor_pandas
