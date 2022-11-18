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
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove blank items
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Net Pricing - Call")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Call for Pricing")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # vendor_pandas["NewPart"] = new_column
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "RDL" + x)
    
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
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"]

    return vendor_pandas

