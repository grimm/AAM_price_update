#
# yak.py
#
# This script holds functions for the vendor Yakima
#
# Initial version - 11/9/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_yak(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part #'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "YAK" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc2"] = vendor_pandas["Product Category"]
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas[" RT"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP"].astype(float)
    vendor_pandas["P5"] = vendor_pandas[" WHSL"] * tech_cal["P5"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Ship Weight (lbs)"].replace('TBD', '0').astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length (in)"].replace('TBD', '0').astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width (in)"].replace('TBD ', '0')
    vendor_pandas["Width"] = vendor_pandas["Width"].replace('TBD', '0').astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height (in)"].replace('TBD', '0').astype(float)

    return vendor_pandas

