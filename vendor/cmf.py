#
# cmf.py
#
# This script holds functions for the vendor CM Truck Beds
#
# Initial version - 08/03/2023 - Jason Grimes
#
from datetime import datetime
import unidecode

# Main vendor processing function
def do_cmf(vendor_pandas, tech_cal):
    # Remove blank items
    vendor_pandas = vendor_pandas[(vendor_pandas["Dealer Cost"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Net Pricing - Call")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Call for Pricing")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    vendor_pandas["Part Number"] = vendor_pandas["Part #"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "CM" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("''", "FT")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P5"] = vendor_pandas["Dealer Cost"].astype(float)

    len_pandas = len(vendor_pandas.index)

    new_column = ["P5/0.75"] * len_pandas
    vendor_pandas["P1"] = new_column
    vendor_pandas["P2"] = vendor_pandas["P1"]

    new_column = ["P5/0.8"] * len_pandas
    vendor_pandas["P3"] = new_column

    new_column = ["P5/0.85"] * len_pandas
    vendor_pandas["P4"] = new_column

    new_column = list("0" * len_pandas)
    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Height"] = new_column
    vendor_pandas["Width"] = new_column
    return vendor_pandas

