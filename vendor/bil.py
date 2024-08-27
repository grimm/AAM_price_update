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
    # print(vendor_pandas.columns)
    # vendor_pandas["Part Number"] = vendor_pandas["Part \nNumber"]
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "BIL" + x)
    
    # Create new description columns
    # vendor_pandas["Desc1"] = vendor_pandas["Description"]
    # vendor_pandas["Desc2"] = vendor_pandas["Description 2"]
    vendor_pandas["Desc1"] = vendor_pandas["Part Type"] + " " + vendor_pandas["Series"] + " " + vendor_pandas["Brand"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    # vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].replace("”", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].replace("\'", "FT")
    # vendor_pandas["Desc2"] = vendor_pandas["Desc2"].replace("”", "IN")
    # vendor_pandas["Desc2"] = vendor_pandas["Desc2"].replace("\'", "FT")
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Convert dollar amounts to float
    vendor_pandas["P1"] = vendor_pandas[" MSRP "].astype(float)
    vendor_pandas["P3"] = vendor_pandas["US MAP"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Titan Truck Current Pricing 7-1-24"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P3"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight\n(Pounds)"].replace("", "0")
    vendor_pandas["Length"] = vendor_pandas["Length\n(IN)"].replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["Width\n(IN)"].replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["Height\n(IN)"].replace("", "0")

    return vendor_pandas
