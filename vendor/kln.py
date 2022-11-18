#
# kln.py
#
# This script holds functions for the vendor Kleinn
#
# Initial version - 11/23/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv
import pandas as pd

# Main vendor processing function
def do_kln(vendor_pandas, tech_cal):
    long_desc = "DESCRIPTION"

    # Strip out parts with no pricing
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP"] != "TBD")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Jobber/ Map"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Remove discontinued parts
    vendor_pandas = vendor_pandas[~(vendor_pandas[long_desc].str.contains("DISCONTINUED"))]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['MODEL'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "KLN" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].apply(lambda x: unidecode.unidecode(x))
    
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"]

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Jobber/ Map"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["P2"]

    vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Length"] = new_column
    vendor_pandas["Weight"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas

