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
    vendor_pandas = vendor_pandas[(vendor_pandas["Active / R&D"] == "Active")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create NewPart column
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "NFA" + x)
    
    # Create new description columns
    vendor_pandas['Desc1']=vendor_pandas['Master Category'] + ' ' + vendor_pandas['Sub Category'] + ' ' + vendor_pandas['Color / Finish'] + ' ' + vendor_pandas["Description 1"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    # trim decription to 30 characters
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["7/30/2021 List  (jobber +25%)"]
    vendor_pandas["P2"] = vendor_pandas["7/30/2021 MAP (jobber +5%)"]
    vendor_pandas["P3"] = vendor_pandas["7/30/2021 Jobber"]
    vendor_pandas["P5"] = vendor_pandas["7/30/2021 MSP (Jobber -18%)"]
    vendor_pandas["P4"] = vendor_pandas["P3"]

    for index, item in enumerate(vendor_pandas["P1"]):
        if vendor_pandas["P1"][index] == 0:
            vendor_pandas["P1"][index] = vendor_pandas["P3"][index] / 0.75
        if vendor_pandas["P2"][index] == 0:
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index] / 0.95
        if vendor_pandas["P5"][index] == 0:
            vendor_pandas["P5"][index] = vendor_pandas["P3"][index] * 0.72

    # Set dimensions
    vendor_pandas["Weight"] = vendor_pandas["Weight (LBS)"]
    vendor_pandas["Length"] = vendor_pandas["Length (Inches)"]
    vendor_pandas["Width"] = vendor_pandas["Width (Inches)"]
    vendor_pandas["Height"] = vendor_pandas["Height (Inches)"]

    return vendor_pandas

