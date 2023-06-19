#
# xan.py
#
# This script holds functions for the vendor Xantrex
#
# Initial version - 3/7/2023 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_xan(vendor_pandas, tech_cal):
    # Remove blank items
    # vendor_pandas = vendor_pandas[(vendor_pandas["MSRP/List"] != "")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["ITEM#"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "XAN" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Item Description"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas['P1'] = vendor_pandas['MSRP'].astype(float)
    vendor_pandas["P5"] = vendor_pandas["USD"].astype(float)

    # vendor_pandas["P2"] = vendor_pandas["P1"]
    # vendor_pandas["P3"] = vendor_pandas["P1"]
    # vendor_pandas["P4"] = vendor_pandas["P1"]

    vendor_pandas["P2"] = "P5/.65"
    vendor_pandas["P3"] = "P5/.7"
    vendor_pandas["P4"] = "P5/.7"

    return vendor_pandas
