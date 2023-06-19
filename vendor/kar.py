#
# kar.py
#
# This script holds functions for the vendor Kargo Master (Holman)
#
# Initial version - 12/14/2020 - Jason Grimes
#

from datetime import datetime
import pandas as pd
import unidecode
import csv

# Main vendor processing function
def do_kar(vendor_pandas, tech_cal):
    # Concatinate both sheets for processing
    vendor_pandas = pd.concat(vendor_pandas, axis=0)

    # Remove catalogs
    vendor_pandas = vendor_pandas[(vendor_pandas["Your Cost"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["MAP"] != "#N/A")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)
    
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part #'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "KAR" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Product Description"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace(r'\n', '')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P2"] = vendor_pandas["Trade Price"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Your Cost"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P5"] / tech_cal["P1"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # vendor_pandas["Including Surcharge"] = vendor_pandas["Including Surcharge"].str.replace("$", "")
    # vendor_pandas["Including Surcharge"] = vendor_pandas["Including Surcharge"].str.replace(",", "")
    # vendor_pandas["Including Surcharge"] = vendor_pandas["Including Surcharge"].str.replace("-", "0")

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight"].replace("", "0")
    vendor_pandas["Weight"] = vendor_pandas["Weight"].astype(float)

    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas

