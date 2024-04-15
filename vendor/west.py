#
# west.py
#
# This script holds functions for the vendor Western
#
# Initial version - 02/01/2021 - Jason Grimes
#

from datetime import datetime
import csv
import unidecode
import pandas as pd

# Main vendor processing function
def do_west(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    long_desc = "DESCRIPTION"
    short_desc = "DESCRIPTION 2"

    # Process all sheets
    # frames = []
    # if "2024 Western Inseason Master P" in vendor_pandas.keys() and not vendor_pandas["2024 Western Inseason Master P"].empty:
    #   truck_pandas = vendor_pandas["2024 Western Inseason Master P"]

    #   sheetlen = len(truck_pandas.axes[0])
    #   new_column = list("1" * sheetlen)
    #   truck_pandas["Group_Code"] = new_column

    #   frames.append(truck_pandas)

    # if "Non-Truck" in vendor_pandas.keys() and not vendor_pandas["Non-Truck"].empty:
    #   nontruck_pandas = vendor_pandas["Non-Truck"]
      
    #   sheetlen = len(nontruck_pandas.axes[0])
    #   new_column = list("2" * sheetlen)
    #   nontruck_pandas["Group_Code"] = new_column

    #   # Fix group codes for 40% parts
    #   for index, item in enumerate(nontruck_pandas["DISCOUNT"]):
    #      if item == 0.4:
    #          nontruck_pandas["Group_Code"][index] = "1"

    #   frames.append(nontruck_pandas)

    # Concat all sheets into one data frame
    # vendor_pandas = pd.concat(frames)

    # Remove blank items
    vendor_pandas = vendor_pandas[(vendor_pandas["LIST PRICE"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["PN"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WEST" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].astype(str) + " " + vendor_pandas[short_desc].astype(str)

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace(r"|","-")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")
    
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["LIST PRICE"].replace("$","").replace(",", "").astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"] * tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P1"] * tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["NET PRICE"].replace("$","").replace(",", "").astype(float)

    # Fix 0% discount parts
    for index, item in enumerate(vendor_pandas["DISCOUNT"]):
      if item == 0.0:
        vendor_pandas["P2"][index] = vendor_pandas["P1"][index]
        vendor_pandas["P3"][index] = vendor_pandas["P1"][index]
        vendor_pandas["P4"][index] = vendor_pandas["P1"][index]
        # vendor_pandas["Group_Code"][index] = "0"

    # Set dimensions and status
    # Get length of dataframe and create new dimension columns
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas
