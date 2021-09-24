#
# uws.py
#
# This script holds functions for the vendor UWS United Welding Supplies
#
# Initial version - 05/28/2021 - Jason Grimes
#

from datetime import datetime
import pandas as pd
import unidecode

# Main vendor processing function
def do_uws(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # vendor_pandas = vendor_pandas[(vendor_pandas["MAP Retail"] != "") | (vendor_pandas["MAP Retail"] != "#N/A")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "UWS" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"]

    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    # Create new Status/NewPart columns
    # vendor_pandas['Part Number'] = vendor_pandas['Item'].astype(str)
    # vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "UWS" + x)
    
    # Create new description columns
    # vendor_pandas["Desc1"] = vendor_pandas["Description"].astype(str)
    # vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    # vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    # vendor_pandas["Desc2"] = vendor_pandas["Desc1"]

    # vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])
    # vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    # vendor_pandas["LIST"] = vendor_pandas["LIST"].astype(str)
    # vendor_pandas["LIST"] = vendor_pandas["LIST"].str.replace("$", "")
    # vendor_pandas["P1"] = vendor_pandas["LIST"].str.replace(",", "").astype(float)

    # vendor_pandas["MAP"] = vendor_pandas["MAP"].astype(str)
    # vendor_pandas["MAP"] = vendor_pandas["MAP"].str.replace("$", "")
    # vendor_pandas["P2"] = vendor_pandas["MAP"].str.replace(",", "").astype(float)

    # vendor_pandas["Jobber"] = vendor_pandas["Jobber"].astype(str)
    # vendor_pandas["Jobber"] = vendor_pandas["Jobber"].str.replace("$", "")
    # vendor_pandas["P3"] = vendor_pandas["Jobber"].str.replace(",", "").astype(float)

    # vendor_pandas["Price"] = vendor_pandas["Price"].astype(str)
    # vendor_pandas["Price"] = vendor_pandas["Price"].str.replace("$", "")
    # vendor_pandas["P5"] = vendor_pandas["Price"].str.replace(",", "").astype(float)

    # vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P5"]

    # Set dimensions and status
    # len_pandas = len(vendor_pandas.axes[0])
    # new_column = list("0" * len_pandas)

    # vendor_pandas["Weight"] = new_column
    # vendor_pandas["Length"] = new_column
    # vendor_pandas["Width"] = new_column
    # vendor_pandas["Height"] = new_column

    return vendor_pandas

