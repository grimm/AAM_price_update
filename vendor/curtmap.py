#
# curtmap.py
#
# This script holds functions for the vendor Curt Manufacturing but just process the map
#
# Initial version - 03/02/2022 - Jason Grimes
#

from datetime import datetime
import csv
import re

# Main vendor processing function
def do_curtmap(vendor_pandas, tech_cal):
    # Filter out all parts that are 5 digits long (not kitted SKU)
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas = vendor_pandas[(vendor_pandas["Part Number"].str.len() == 5)]

    # Filter out any part that has emailed for cost
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Emailed for Cost")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Life Cycle Status Code"] != "Discontinued")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Get length of dataframe and create new NewPart column
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("A" * len_pandas)

    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "CURT" + x)
    
    # Create all price fields
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(str)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas.index = range(len(vendor_pandas.index))
    
    for index, item in enumerate(vendor_pandas["MAP Retail"]):
        #print(index)
        if item == "Removed" or item == "0" or item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P5"][index] / tech_cal["P2"]
        else:
            vendor_pandas["P2"][index] = item

    return vendor_pandas
