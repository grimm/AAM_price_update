#
# buy.py
#
# This script holds functions for the vendor Buyers Products
#
# Initial version - 02/18/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_buy(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    long_desc = "Description"

    # Strip out parts with no pricing
    vendor_pandas = vendor_pandas[(vendor_pandas["ListPrice"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Amount01"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    vendor_pandas = vendor_pandas[(vendor_pandas["ItemPartNumber"].str[:2] != "16")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['ItemPartNumber'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "BUY" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["ListPrice"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Amount01"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P5"] / tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight (lbs)"].replace('', '0').astype(float)

    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Length"] = new_column
    vendor_pandas["Height"] = new_column
    vendor_pandas["Width"] = new_column


    return vendor_pandas

