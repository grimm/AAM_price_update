#
# rfn.py
#
# This script holds functions for the vendor Roofnest
#
# Initial version - 5/10/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_rfn(vendor_pandas, tech_cal, new_cal):
    if not new_cal:
        # Remove rows with no data
        vendor_pandas = vendor_pandas[(vendor_pandas["MAP Price"] != "")]
        vendor_pandas = vendor_pandas.reset_index(drop=True)

        # Create new Status/NewPart columns
        vendor_pandas["Part Number"] = vendor_pandas["SKU"].astype(str)
        vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "RFN" + x)

    # Create new description columns
    if not new_cal:
        vendor_pandas["Desc1"] = vendor_pandas["DESCRIPTION"].astype(str)
    else:
        vendor_pandas["Desc1"] = vendor_pandas["description"].astype(str)

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    if not new_cal:
        # Create all price fields
        vendor_pandas["P1"] = vendor_pandas["MAP Price"].astype(float)
        vendor_pandas["P2"] = vendor_pandas["P1"]
        vendor_pandas["P3"] = vendor_pandas["P1"]
        vendor_pandas["P4"] = vendor_pandas["P1"]
        vendor_pandas["P5"] = vendor_pandas["QTY 30"].astype(float)

    # Set dimensions and status
    len_pandas = len(vendor_pandas.axes[0])
    vendor_pandas["Weight"] = list("0" * len_pandas)
    vendor_pandas["Length"] = list("0" * len_pandas)
    vendor_pandas["Height"] = list("0" * len_pandas)
    vendor_pandas["Width"] = list("0" * len_pandas)

    return vendor_pandas

