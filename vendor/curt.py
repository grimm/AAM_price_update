#
# curt.py
#
# This script holds functions for the vendor Curt Manufacturing
#
# Initial version - 10/13/2020 - Jason Grimes
#                   10/28/2020 - Fixed issue with descriptions that started with a quote
#

from datetime import datetime
import csv
import re

# Main vendor processing function
def do_curt(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Filter out all parts that are 5 digits long (not kitted SKU)
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas = vendor_pandas[(vendor_pandas["Part Number"].str.len() == 5)]

    # Get length of dataframe and create new NewPart column
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("A" * len_pandas)

    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "CURT" + x)
    
    # Create new description columns and replace quotes
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].str.replace('\"', 'in')
    vendor_pandas["Desc2"] = vendor_pandas[long_desc].str.replace('\"', 'in')

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"]

    vendor_pandas["P2"] = vendor_pandas["AAM Cost"]
    vendor_pandas["MAP Retail"] = vendor_pandas["MAP Retail"].astype(str)

    vendor_pandas.index = range(len(vendor_pandas.index))
    
    for index, item in enumerate(vendor_pandas["MAP Retail"]):
        #print(index)
        if item == "Removed" or item == "0" or item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P5"][index] / tech_cal["P2"]
        else:
            vendor_pandas["P2"][index] = item

    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"]
    vendor_pandas["Status"] = new_column

    # Check for discontinued parts
    for index, item in enumerate(vendor_pandas[short_desc]):
        # print(index)
        if re.search("Discontinued", item):
            # print(item)
            vendor_pandas["Status"][index] = "D"


    return vendor_pandas
