#
# nitro.py
#
# This script holds functions for the vendor Nitro Gear & Axle
#
# Initial version - 04/21/2021 - Jason Grimes
#
# NOTE: If they have a price increase, need to notify Jared.
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_nitro(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    # removed prefix, part #s are too long
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "NIT" + x)
    # vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Long Description 100 Characters or less WITHOUT application information"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Member to Member Cost"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P2"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    return vendor_pandas

