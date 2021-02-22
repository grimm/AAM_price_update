#
# sb.py
#
# This script holds functions for the vendor S&B Filters
#
# Initial version - 02/22/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_sb(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['mfg_original_sku'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "SB" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["title"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["list_price"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["map_price"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P3"]
    vendor_pandas["P5"] = vendor_pandas["25_jobber_pricing"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["weight"].replace('', '0').astype(float)
    vendor_pandas["Length"] = vendor_pandas["dim_length"].replace('', '0').astype(float)
    vendor_pandas["Width"] = vendor_pandas["dim_width"].replace('', '0').astype(float)
    vendor_pandas["Height"] = vendor_pandas["dim_height"].replace('', '0').astype(float)

    return vendor_pandas

