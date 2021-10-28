#
# cbp.py
#
# This script holds functions for the vendor Centric
#
# Initial version - 10/25/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_cbp(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber Effective 9/3/2021"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Titan Truck Price"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P5"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["LBS"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    return vendor_pandas

