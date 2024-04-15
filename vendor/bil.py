#
# bil.py
#
# This script holds functions for the vendor Bilstein
#
# Initial version - 3/6/2024 - Jason Grimes
#

import pandas as pd

# Main vendor processing function
def do_bil(vendor_pandas, tech_cal):
    # Copy Part # column to NewPart column and modify to add TIM
    print(vendor_pandas.columns)
    vendor_pandas["Part Number"] = vendor_pandas["PartNumber"]
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "BIL" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc2"] = vendor_pandas["Description 2"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].replace("”", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].replace("\'", "FT")
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].replace("”", "IN")
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].replace("\'", "FT")

    # Convert dollar amounts to float
    vendor_pandas["P1"] = vendor_pandas["MSRP"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["US MAP"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Titan Truck Current Pricing 3-1-24"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P3"]

    # Set dimensions and status
    # vendor_pandas["Weight"] = vendor_pandas["Shipping Weight (Lbs.)"].replace("", "0")
    # vendor_pandas["Length"] = vendor_pandas["BOX \n(L)      (inches)"].replace("", "0")
    # vendor_pandas["Width"] = vendor_pandas["BOX \n(D)  (inches)"].replace("", "0")
    # vendor_pandas["Height"] = vendor_pandas["BOX\n(H) (inches)"].replace("", "0")

    return vendor_pandas
