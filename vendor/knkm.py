#
# knkm.py
#
# This script holds functions for the vendor Wernerco (Weather Guard) manufacturer file
#
# Initial version - 06/30/2021 - Jason Grimes
#

from datetime import datetime
import pandas as pd
import unidecode

# Main vendor processing function
def do_knkm(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    long_desc = "DESCRIPTION"

    # Drop all rows with no price
    vendor_pandas = vendor_pandas[(vendor_pandas["New Trade"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["PART NUMBER"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "KNK" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["New Trade"].replace("$", "")
    vendor_pandas["P1"] = vendor_pandas["P1"].replace(",", "")

    vendor_pandas["P5"] = vendor_pandas["Select\nTier 1"].replace("$", "")
    vendor_pandas["P5"] = vendor_pandas["P5"].replace(",", "")

    vendor_pandas["P3"] = vendor_pandas["P1"] * tech_cal["P3"]
    vendor_pandas["P2"] = vendor_pandas["P1"] * tech_cal["P2"]
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight (Lbs)"].replace("","0")
    vendor_pandas["Weight"] = vendor_pandas["Weight"].replace("undefined","0").astype(float)

    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)
    vendor_pandas["Group Code"] = new_column

    return vendor_pandas
