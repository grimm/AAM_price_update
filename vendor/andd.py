#
# andd.py
#
# This script holds functions for the vendor Anderson
#
# Initial version - 06/02/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_and(vendor_pandas, tech_cal):
    # Remove blank rows
    vendor_pandas = vendor_pandas[(vendor_pandas["Description"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Units"] == 1)]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['SKU'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "AND" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["RETAIL"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["MAP"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Dealer Price"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P3"]
    vendor_pandas["P4"] = vendor_pandas["P3"]

    return vendor_pandas

