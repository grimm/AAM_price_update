#
# wig.py
#
# This script holds functions for the vendor Hellwig
#
# Initial version - 03/15/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_wig(vendor_pandas, tech_cal):
    # Remove blank parts
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['P/N'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WIG" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description 2"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\"', 'in')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\'', 'ft')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["JOBBER"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["NET"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P1"] * tech_cal["P2"]

    vendor_pandas["P4"] = vendor_pandas["MAP"]
    for index, item in enumerate(vendor_pandas["P4"]):
        if item == "N/A":
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]
        else:
            vendor_pandas["P4"][index] = item
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight (lbs)"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length (in)"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width (in)"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height (in)"].astype(float)

    return vendor_pandas

