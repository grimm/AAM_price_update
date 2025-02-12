#
# fire.py
#
# This script holds functions for the vendor Firestone/Ride Rite
#
# Initial version - 06/17/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import pandas as pd
import unidecode
import csv

# Main vendor processing function
def do_fire(vendor_pandas, tech_cal):
    # Remove parts with no pricing
    # print(vendor_pandas.columns)
    vendor_pandas = vendor_pandas[(vendor_pandas["January 1st, 2024 List Price"] != "NA")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["October 2nd, 2023 List Price"] != "October 2nd, 2023 List Price")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Concatinate both sheets for processing
    #vendor_pandas = pd.concat(vendor_pandas, axis=0, ignore_index=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['4-Digit'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "FIRE" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\"', 'in')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\'', 'ft')

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["January 1st, 2024 List Price"].replace("$","").replace(",","")
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["January 1st, 2024 Jobber Price"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    # Calculate Titan's price 36% off of Jobber
    # vendor_pandas["P5"] = vendor_pandas["Titan Truck (36.0%)"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["P3"] * 0.64
    # Add 1%
    vendor_pandas["P5"] = vendor_pandas["P5"] * 1.01

    vendor_pandas["P2"] = vendor_pandas["MAP [USD]"].replace("$","").replace(",","")
    for index, item in enumerate(vendor_pandas["P2"]):
        # print(item)
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P5"][index] / tech_cal["P2"]
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)

    # Set dimensions and status
    # Make sure that measurement values are correct
    vendor_pandas["Weight"] = vendor_pandas["Gross Wgt [lbs]"].replace("n/a", "0")
    vendor_pandas["Weight"] = vendor_pandas["Weight"].replace("TBD", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Weight"]
    vendor_pandas["Width"] = vendor_pandas["Weight"]
    vendor_pandas["Height"] = vendor_pandas["Weight"]

    for index, item in enumerate(vendor_pandas["Box Dim              (L\" X W\" X H\")"].astype(str)):
        vendor_pandas["Length"][index] = 0
        vendor_pandas["Width"][index] = 0
        vendor_pandas["Height"][index] = 0

        if not item == "":
            if item.count('x') == 2:
                length, width, height = item.split("x")
            elif item.count('X') == 2:
                length, width, height = item.split("X")
            else:
                length, width, height = ["0", "0", "0"]

            vendor_pandas["Length"][index] = length
            vendor_pandas["Width"][index] = width
            vendor_pandas["Height"][index] = height

    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)

    return vendor_pandas

