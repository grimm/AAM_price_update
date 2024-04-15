#
# arc.py
#
# This script holds functions for the vendor Arctic snow pusher
#
# Initial version - 07/07/2023 - Jason Grimes
#

from datetime import datetime
import unidecode
import pandas as pd

# Main vendor processing function
def do_arc(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    long_desc = "DESCRIPTION"

    # Remove blank items
    # vendor_pandas = vendor_pandas[(vendor_pandas["LIST PRICE"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["WD "] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["WD "] != 0)]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    vendor_pandas["Part Number"] = vendor_pandas["PART #"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "ARC" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["LIST PRICE"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P1"]
    vendor_pandas["P5"] = vendor_pandas["DEALER PRICE"].astype(float)

    # Set dimensions
    len_pandas = len(vendor_pandas)
    new_column = list("0" * len_pandas)
    [float(i) for i in new_column]

    vendor_pandas["Weight"] = pd.Series(new_column)
    vendor_pandas["Length"] = pd.Series(new_column)
    vendor_pandas["Height"] = pd.Series(new_column)
    vendor_pandas["Width"] = pd.Series(new_column)

    return vendor_pandas

