#
# anz.py
#
# This script holds functions for the vendor ANZO USA
#
# Initial version - 7/29/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_anz(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove parts with no price
    # vendor_pandas = vendor_pandas.drop_duplicates(subset="Part Number")
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas["Part Number"] = vendor_pandas["PART #"]
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str).apply(lambda x: "ANZ" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["DESCRIPTION"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["JOBBER"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP PRICING"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P2"]
    vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # for index, item in enumerate(vendor_pandas["Unilateral Retail"]):
    #     if item == "":
    #         vendor_pandas["P1"][index] = vendor_pandas["P3"][index]
    # vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    # Set dimensions
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    # vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].astype(float)
    # vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)
    # vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)
    # vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    return vendor_pandas

