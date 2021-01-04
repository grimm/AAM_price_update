#
# protec.py
#
# This script holds functions for the vendor ProTec.
#
# Initial version - 11/23/2020 - Jason Grimes
#

import pandas as pd
from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_protec(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['NewPart'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "PROTEC" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["10% OFF"].astype(float)
    vendor_pandas["P1"] = vendor_pandas["MSRP"]
    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions
    # len_pandas = len(vendor_pandas)
    # new_column = list("0" * len_pandas)
    # [float(i) for i in new_column]

    # vendor_pandas["Weight"] = pd.Series(new_column)
    # vendor_pandas["Length"] = pd.Series(new_column)
    # vendor_pandas["Height"] = pd.Series(new_column)
    # vendor_pandas["Width"] = pd.Series(new_column)

    return vendor_pandas

