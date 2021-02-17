#
# odr.py
#
# This script holds functions for the vendor Odor
#
# Initial version - 02/12/2021 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_odr(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove promotional items
    vendor_pandas = vendor_pandas[~(vendor_pandas[short_desc] == "removed")]

    # Create new Status/NewPart columns
    vendor_pandas['NewPart'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "ODR" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc] + " " + vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P3"] = vendor_pandas["Jobber"].replace('[\$,)]','', regex=True)
    vendor_pandas["P3"] = vendor_pandas["P3"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(str)
    vendor_pandas["P1"] = vendor_pandas["P1"].replace('[\$,)]','', regex=True)
    vendor_pandas["P1"] = vendor_pandas["P1"].replace('n/a','0')
    vendor_pandas["P1"] = vendor_pandas["P1"].apply(lambda x: str(x).replace('/ea',''))
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    # Replace missing values in P1
    for index, item in enumerate(vendor_pandas["P1"]):
        if item == 0:
            vendor_pandas["P1"][index] = vendor_pandas["P3"][index]

    vendor_pandas["P2"] = vendor_pandas["MAP Retail"].replace('[\$,)]','', regex=True)
    vendor_pandas["P2"] = vendor_pandas["P2"].replace('n/a','0')

    # Replace missing values in P2
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == '' or item == '0':
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index]

    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0")
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0")

    return vendor_pandas

