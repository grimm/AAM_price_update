#
# rsp.py
#
# This script holds functions for the vendor Race Sport
#
# Initial version - 10/23/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import re

# Main vendor processing function
def do_rsp(vendor_pandas, tech_cal):
	# Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove parts with no pricing
    vendor_pandas = vendor_pandas.drop(vendor_pandas[(vendor_pandas['AAM Cost'] == "") & (vendor_pandas['MSRP/List'] == "")].index)

    # Get length of dataframe and create new NewPart column
    len_pandas = len(vendor_pandas.axes[0])
    vendor_pandas["Status"] = list("A" * len_pandas)

    # This does not work, had to manually remove return from file
    #vendor_pandas[long_desc] = vendor_pandas[long_desc].replace(r'\\r\\n',' ', regex=True)

    # Process part number
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].astype(str)
    for index, item in enumerate(vendor_pandas["NewPart"]):
        if item[:3] == "RSP":
            vendor_pandas["NewPart"][index] = item[3:]
        elif item[:2] == "RS":
            vendor_pandas["NewPart"][index] = item[2:]
        else:
            vendor_pandas["NewPart"][index] = item

    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].str.replace('-', '')
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: x[:20])
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "RSP" + x)
    
    # Create new description columns
        
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P4"] = vendor_pandas["AAM Cost"]
    for index, item in enumerate(vendor_pandas["MAP Wholesale / MSP"]):
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]
        else:
            vendor_pandas["P4"][index] = item

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"]

    # Make sure that measurement values are correct
    vendor_pandas["Weight"] = vendor_pandas["Weight"].replace("", "0")
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0")

    for index, item in enumerate(vendor_pandas["Desc1"]):
        #print(index)
        if re.search("DISCONTINUED", item):
            vendor_pandas["Status"][index] = "D"

    return vendor_pandas
