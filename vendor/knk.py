#
# knk.py
#
# This script holds functions for the vendor Wernerco (Weather Guard)
#
# Initial version - 03/24/2021 - Jason Grimes
#

from datetime import datetime
import pandas as pd
import unidecode

# Main vendor processing function
def do_knk(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    long_desc = "Description"

    # Process all sheets and label descriptions
    jobsite_pandas = vendor_pandas["JOBSITE"]
    van_pandas = vendor_pandas["VAN"]
    truck_pandas = vendor_pandas["TRUCK"]

    jobsite_pandas[long_desc] = jobsite_pandas[long_desc].apply(lambda x: "(JOBSITE) " + x)
    van_pandas[long_desc] = van_pandas[long_desc].apply(lambda x: "(VAN) " + x)
    truck_pandas[long_desc] = truck_pandas[long_desc].apply(lambda x: "(TRUCK) " + x)

    # Add group code
    sheetlen = len(jobsite_pandas.axes[0])
    new_column = list("2" * sheetlen)
    jobsite_pandas["Group Code"] = new_column
    new_column = list("j" * sheetlen)
    jobsite_pandas["type"] = new_column

    sheetlen = len(van_pandas.axes[0])
    new_column = list("1" * sheetlen)
    van_pandas["Group Code"] = new_column

    sheetlen = len(truck_pandas.axes[0])
    new_column = list("1" * sheetlen)
    truck_pandas["Group Code"] = new_column

    # Concat all sheets into one data frame
    frames = [jobsite_pandas, van_pandas, truck_pandas]
    vendor_pandas = pd.concat(frames)
    vendor_pandas = vendor_pandas[(vendor_pandas["Trade Price"] != 0)]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["SKU"].apply(lambda x: x[5:])
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "KNK" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["Trade Price"].replace("$", "")
    vendor_pandas["P1"] = vendor_pandas["P1"].replace(",", "")

    vendor_pandas["P5"] = vendor_pandas["Customer Price"].replace("$", "")
    vendor_pandas["P5"] = vendor_pandas["P5"].replace(",", "")

    vendor_pandas["P3"] = vendor_pandas["P1"] * tech_cal["P3"]
    vendor_pandas["P2"] = vendor_pandas["P1"] * tech_cal["P2"]
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]

    for index, item in enumerate(vendor_pandas["type"]):
        if item == "j":
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index]
            vendor_pandas["P3"][index] = vendor_pandas["P1"][index]
            vendor_pandas["P4"][index] = vendor_pandas["P1"][index]
        if vendor_pandas["P1"][index] == vendor_pandas["P5"][index] and item != "j":
            vendor_pandas["P1"][index] = vendor_pandas["P5"][index] / .6336
            vendor_pandas["P3"][index] = vendor_pandas["P1"][index] * tech_cal["P3"]
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index] * tech_cal["P2"]
            vendor_pandas["P4"][index] = vendor_pandas["P1"][index] * tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight"].replace("","0").astype(float)

    return vendor_pandas
