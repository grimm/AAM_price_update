#
# egr.py
#
# This script holds functions for the vendor EGR
#
# Initial version - 3/1/2023 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_egr(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"
    # long_desc = "Product Line"

    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    # vendor_pandas['Part Number'] = vendor_pandas['Part No.'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "EGR" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Unilateral Retail"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Unilateral Wholesale"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    for index, item in enumerate(vendor_pandas["P2"]):
     if item == "":
         vendor_pandas["P2"][index] = vendor_pandas["P1"][index]
     else:
         vendor_pandas["P2"][index] = item

    for index, item in enumerate(vendor_pandas["P4"]):
     if item == "":
         vendor_pandas["P4"][index] = vendor_pandas["P3"][index]
     else:
         vendor_pandas["P4"][index] = item

    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)

    # Set dimensions and status
    lname = "Weight - IN POUNDS"
    # lname = "Weight (Lb)"
    vendor_pandas[lname] = vendor_pandas[lname].astype(str)
    vendor_pandas[lname] = vendor_pandas[lname].str.replace('TBD', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].replace("", "0")
    vendor_pandas["Weight"] = vendor_pandas["Weight"].str.replace("½", ".5").astype(float)

    return vendor_pandas

