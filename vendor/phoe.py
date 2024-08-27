#
# phoe.py
#
# This script holds functions for the vendor Phoenix.
#
# Initial version - 08/01/2024 - Jason Grimes
#

from datetime import datetime
import unidecode
import pandas as pd

# Main vendor processing function
def do_phoe(vendor_pandas, tech_cal):
    # Remove rows with no pricing
    vendor_pandas = vendor_pandas[(vendor_pandas["Unit Price"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create part number columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].str.strip()
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "PHOE" + x)
     
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"].str.replace("\?", "")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["Unit Price"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P5"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    return vendor_pandas

