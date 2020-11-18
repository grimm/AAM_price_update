#
# adu.py
#
# This script holds functions for the vendor Air Design Products.
#
# Initial version - 11/13/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_adu(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['NewPart'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "ADU" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Part Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["Retail Price"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["Jobber Price"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P3"]
    vendor_pandas["P5"] = vendor_pandas["WD Price"].astype(float)

    # Set dimensions
    vendor_pandas["Weight"] = vendor_pandas["Weight (lb.)"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length (in.)"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height (in.)"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width (in.)"].astype(float)

    return vendor_pandas

