#
# wick.py
#
# This script holds functions for the vendor Wickum Weld
#
# Initial version - 6/10/2024 - Jason Grimes
#
# Copy each sheet and past as values to remove formulas!
#

from datetime import datetime
import unidecode
import pandas as pd
import csv

# Main vendor processing function
def do_wick(vendor_pandas, tech_cal):
    # Fix column names
    vendor_pandas["Cab Racks"]["Description"] = vendor_pandas["Cab Racks"]["Panel Description"]
    vendor_pandas["Cab Racks"]["4-8"] = vendor_pandas["Cab Racks"]["4-8 "]
    vendor_pandas["XBOX Single Lid"]["4-8"] = vendor_pandas["XBOX Single Lid"]["4-8 "]
    vendor_pandas["XBOX Dual Lid"]["4-8"] = vendor_pandas["XBOX Dual Lid"]["4-8 "]
    vendor_pandas["IBOX Box"]["4-8"] = vendor_pandas["IBOX Box"]["4-8 "]

    # Concat all sheets into one frame
    frames = []
    sheets = ["Cab Racks", "Cab Rack Acc", "XBOX Single Lid", "XBOX Dual Lid", "IBOX Box"]

    for sheet in sheets:
        frames.append(vendor_pandas[sheet])

    vendor_pandas = pd.concat(frames)

    # Remove all rows with bad data
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet"] != "Fleet")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet"] != "Fleet ")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet"] != "Call")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet"] != "CALL")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet"] != "Please Call for Quote")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet "] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet "] != "Fleet ")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet "] != "Fleet")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet "] != "Call")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet "] != "CALL")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Fleet "] != "Please Call for Quote")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Item #"] != "36 Feet - Add to any cab rack price with 24” Feet")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Item #"] != "Full Length Feet Add to any cab rack price with 24\" feet")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Item #"] != "Full Length Oval Tie Downs - Add to any cab rack price with 24\" feet")]

    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Item #'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WICK" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["4-8"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P5"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas

