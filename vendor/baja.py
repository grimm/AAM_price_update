#
# baja.py
#
# This script holds functions for the vendor Baja Designs
#
# Initial version - 01/25/2021 - Jason Grimes
#

import unidecode

# Main vendor processing function
def do_baja(vendor_pandas, tech_cal):
    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["mfg_original_sku"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "BAJA" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["title"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["list_price"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["map_price"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["P2"]
    vendor_pandas["P4"] = vendor_pandas["2a_pricing"].astype(float)
    vendor_pandas["P5"] = (vendor_pandas["P1"] * 0.56) / tech_cal["P5"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["weight"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["dim_length"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["dim_height"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["dim_width"].astype(float)

    return vendor_pandas
