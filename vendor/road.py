#
# road.py
#
# This script holds functions for the vendor RoadMaster
#
# Initial version - 02/10/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_road(vendor_pandas, tech_cal):
    # Filter out all rows that have no prices
    vendor_pandas = vendor_pandas[(vendor_pandas["Retail"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Retail"] != "0")]

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["Name"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "ROAD" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas['P1'] = vendor_pandas['Retail'].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P3"] = vendor_pandas["P1"]
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["P5"] = vendor_pandas["DEALER"].astype(float)

    # Set dimensions and status
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas
