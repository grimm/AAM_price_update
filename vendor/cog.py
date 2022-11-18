#
# cog.py
#
# This script holds functions for the vendor Cognito
#
# Initial version - 01/12/2022 - Jason Grimes
#

import unidecode

# Main vendor processing function
def do_cog(vendor_pandas, vend_cal):
    # Create new part numbers
    vendor_pandas["Part Number"] = vendor_pandas["sku"].apply(lambda x: x[:-5])
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "COG" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["title"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Get P pricing
    vendor_pandas["P1"] = vendor_pandas["list_price"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["map_price"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["tier_4_pricing"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P3"]
    vendor_pandas["P4"] = vendor_pandas["P3"]

    # Get fitment
    vendor_pandas["Weight"] = vendor_pandas["weight"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["dim_length"].astype(str)
    vendor_pandas["Width"] = vendor_pandas["dim_width"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["dim_height"].astype(float)

    return vendor_pandas
