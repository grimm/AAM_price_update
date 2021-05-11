#
# nitro.py
#
# This script holds functions for the vendor Nitro Gear & Axle
#
# Initial version - 04/21/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_nitro(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['mfg_original_sku'].astype(str)
    # removed prefix, part #s are too long
    # vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "NITRO" + x)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["title"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["w2_pricing"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["map_price"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["list_price"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["w3_pricing"].astype(float)
    # vendor_pandas["P5"] = vendor_pandas["w4_pricing"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["w6_pricing"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["weight"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["dim_length"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["dim_width"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["dim_height"].astype(float)

    return vendor_pandas

