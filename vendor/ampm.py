#
# amp.py
#
# This script holds functions for the vendor AMP Research
#
# Initial version - 12/28/2020 - Jason Grimes
#
from datetime import datetime
import pandas as pd
import unidecode

# Main vendor processing function
def do_ampm(vendor_pandas, tech_cal):
    # Concatinate all sheets for processing
    # vendor_pandas = pd.concat(vendor_pandas, axis=0, ignore_index=True)
    
    # Put really long header text in some vars
    # short_desc = "Generic Description "
    short_desc = "class desc"

    # Remove discontinued items
    # vendor_pandas = vendor_pandas[(vendor_pandas["Old Part Numbers"] == "")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Get length of dataframe and create new Status/NewPart columns
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("A" * len_pandas)

    vendor_pandas["Part Number"] = vendor_pandas["item"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "AMP" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].replace("$", "")
    vendor_pandas["P1"] = vendor_pandas["P1"].replace("", "0").astype(float)

    vendor_pandas["P3"] = vendor_pandas["Jobber"].replace("$", "")
    vendor_pandas["P3"] = vendor_pandas["P3"].replace("", "0").astype(float)

    vendor_pandas["P2"] = vendor_pandas["Unilateral"].replace("$", "")
    vendor_pandas["P2"] = vendor_pandas["P2"].replace("", "0").astype(float)

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"]


    # Set dimensions
    # vendor_pandas["Weight"] = vendor_pandas["WGT (lbs)"]
    # vendor_pandas["Height"] = vendor_pandas["H (in)"]
    # vendor_pandas["Length"] = vendor_pandas["L (in)"]
    # vendor_pandas["Width"] = vendor_pandas["W (in)"].replace("a", "0").astype(float)

    return vendor_pandas

