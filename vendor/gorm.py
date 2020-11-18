#
# gorm.py
#
# This script holds functions for the vendor Go Rhino's manufacturer spreadsheets
#
# Initial version - 11/04/2020 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_gorm(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    first_desc = "Product Line"
    second_desc = "Vehicle / Description"

    # Filter out all rows that have no prices
    # vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas = vendor_pandas[(vendor_pandas["Category"] != "")]
    vendor_pandas.index = range(len(vendor_pandas.index))

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part No.'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "GOR" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[first_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc2"] = vendor_pandas[second_desc]
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP"]
    vendor_pandas["P3"] = vendor_pandas["US Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["US Jobber"] * 0.85

    vendor_pandas["P5"] = vendor_pandas["P3"]
    for index, item in enumerate(vendor_pandas["Make"]):
        if item == "Jeep":
            vendor_pandas["P5"][index] = vendor_pandas["P3"][index] * (0.7 * 0.9 * 0.95)
        else:
            vendor_pandas["P5"][index] = vendor_pandas["P3"][index] * (0.7 * 0.9 * 0.95 * 0.945)

    vendor_pandas["P2"] = vendor_pandas["UMAP"].replace('NO', '0').astype(float)
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == 0:
            vendor_pandas["P2"][index] = vendor_pandas["P5"][index] / 0.644

    # Set dimensions and status
    lname = "Weight (Lb)"
    vendor_pandas[lname] = vendor_pandas[lname].astype(str)
    vendor_pandas[lname] = vendor_pandas[lname].str.replace('TBD', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].astype(float)

    vendor_pandas["Length"] = vendor_pandas['Length (In)'].astype(str)
    vendor_pandas["Length"] = vendor_pandas["Length"].str.replace('TBD', '0')
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)

    vendor_pandas["Width"] = vendor_pandas['Width (In)'].astype(str)
    vendor_pandas["Width"] = vendor_pandas["Width"].str.replace('TBD', '0')
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)

    vendor_pandas["Height"] = vendor_pandas['Height (In)'].astype(str)
    vendor_pandas["Height"] = vendor_pandas["Height"].str.replace('TBD', '0')
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    return vendor_pandas

