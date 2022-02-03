#
# ele.py
#
# This script holds functions for the vendor Element
#
# Initial version - 01/31/2022 - Jason Grimes
#
from datetime import datetime
import unidecode

# Main vendor processing function
def do_ele(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove blank items
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Net Pricing - Call")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # vendor_pandas["NewPart"] = new_column
    vendor_pandas["Part Number"] = vendor_pandas["Part Number"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "ELE" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc] + " " + vendor_pandas["Application"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("''", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Unilateral Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Unilateral Wholesale"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"]

    return vendor_pandas

