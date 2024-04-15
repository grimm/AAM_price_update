#
# rdl.py
#
# This script holds functions for the vendor ReadyLift
#
# Initial version - 09/01/2021 - Jason Grimes
#
from datetime import datetime
import unidecode

# Main vendor processing function
def do_rdl(vendor_pandas, tech_cal):
    # Remove blank items
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Net Pricing - Call")]
    # vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Call for Pricing")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # vendor_pandas["NewPart"] = new_column
    print(vendor_pandas.columns)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "RDL" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("''", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P2"] = vendor_pandas["US Retail MAP"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber USD"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Titan Cost with co-op included in price"].astype(float)
    # calculate coop
    vendor_pandas["P5"] = vendor_pandas["P5"] / 0.95

    vendor_pandas["P1"] = vendor_pandas["P2"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    return vendor_pandas

