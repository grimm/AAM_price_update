#
# nfa.py
#
# This script holds functions for the vendor N-FAB.
#
# Initial version - 11/24/2020 - Jason Grimes
#
from datetime import datetime

# Main vendor processing function
def do_nfa(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove non-active items
    # vendor_pandas = vendor_pandas[(vendor_pandas["Active / R&D"] == "Active")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create NewPart column
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "NFA" + x)
    
    # Create new description columns
    vendor_pandas['Desc1']=vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    # trim decription to 30 characters
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["MAP Wholesale / MSP"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P5"][index] / tech_cal["P2"]

    for index, item in enumerate(vendor_pandas["P1"]):
        if item == "":
            vendor_pandas["P1"][index] = vendor_pandas["P2"][index]

    for index, item in enumerate(vendor_pandas["P4"]):
        if item == "":
            vendor_pandas["P4"][index] = vendor_pandas["P5"][index] / tech_cal["P4"]

    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)

    # Set dimensions
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", 0).astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", 0).astype(float)

    return vendor_pandas

