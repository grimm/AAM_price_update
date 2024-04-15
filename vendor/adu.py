#
# adu.py
#
# This script holds functions for the vendor Air Design Products.
#
# Initial version - 11/13/2020 - Jason Grimes
# Updated script for new file format - 04/08/21 - JG
#

from datetime import datetime
import unidecode
import csv
import pandas as pd

# Main vendor processing function
def do_adu(vendor_pandas, tech_cal):
    # Concat all sheet into one frame
    # frames = []
    # sheets = ["SuperBolt Fender Flare Set", "Wide Fender Flare Set", "Smooth Fender Flare Set", "OE Style Fender Flare Set", "Inner Fender Liner Set", "Grilles", "Hood Scoop", "Door Rocker Panels and Moldings", "Tailgate Appliqué", "Tailgate Spoiler", "Roof and Cab Spoiler_Winglets", "Front Bumper Guard", "Fender Vent Set", "Floor Liner Set ", "Off Road Full Kits", "Street Series Full Kits", "Cars and SUV", "Replacement Parts_Hardware"]

    # for sheet in sheets:
    #     frames.append(vendor_pandas[sheet])

    # vendor_pandas = pd.concat(frames)
    # print(vendor_pandas.columns)

    # Remove in progress rows
    # vendor_pandas = vendor_pandas[(vendor_pandas["Box Weight (lbs.)"] <= 8000)]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Air Design Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "ADU" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Long Description (English)"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP / MAP"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Titan"]

    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P3"]

    # Set dimensions
    vendor_pandas["Weight"] = vendor_pandas["Box Weight (lbs.)"].replace("TBD", "0").replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Box Length. (in.)"].replace("TBD", "0").replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Box Height (in.)"].replace("TBD", "0").replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Box Width (in.)"].replace("TBD", "0").replace("", "0").astype(float)

    return vendor_pandas

