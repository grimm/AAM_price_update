#
# yak.py
#
# This script holds functions for the vendor Yakima
#
# Initial version - 11/9/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import pandas as pd

# Main vendor processing function
def do_yak(vendor_pandas, tech_cal):
    # Fix Whsl column name
    vendor_pandas["Part Info"]["Whsl"] = vendor_pandas["Part Info"]["WHSL"]

    # Concat all sheet into one frame
    frames = []
    sheets = ["Part Info", "Replacement Part Info"]

    for sheet in sheets:
        frames.append(vendor_pandas[sheet])

    vendor_pandas = pd.concat(frames)

    # Remove in rows with no data
    # vendor_pandas = vendor_pandas[(vendor_pandas["Titan Price"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP"] != "n/a")]
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part #'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "YAK" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].replace("n/a", "0").astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    # vendor_pandas["P5"] = vendor_pandas["Titan Price"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Whsl"]
    vendor_pandas["P5"] = vendor_pandas["P5"] * tech_cal["P5"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    vendor_pandas["P3"] = vendor_pandas["P3"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["P5"].astype(float)

    # Set dimensions
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    # vendor_pandas["Weight"] = new_column
    # vendor_pandas["Length"] = new_column
    # vendor_pandas["Width"] = new_column
    # vendor_pandas["Height"] = new_column

    vendor_pandas["Weight"] = vendor_pandas["Ship Weight (lbs)"]
    vendor_pandas["Length"] = vendor_pandas["Length\n(in)"]
    vendor_pandas["Width"] = vendor_pandas["Width\n(in)"]
    vendor_pandas["Height"] = vendor_pandas["Height\n(in)"]

    return vendor_pandas

