#
# dom.py
#
# This script holds functions for the vendor Dometic Outdoor
#
# Initial version - 04/05/2022 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_dom(vendor_pandas, group_code, tech_cal):
    # Remove in rows with no data
    # vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"


    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "DOM" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\"', 'in')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\'', 'ft')

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P3"]

    for index, item in enumerate(vendor_pandas["P1"]):
        if item == "": 
            vendor_pandas["P1"] = vendor_pandas["P3"]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["Group Code"] = vendor_pandas["P1"].astype(int)

    # Setup group codes
    for index, item in enumerate(vendor_pandas["P5"]):
        test = item / vendor_pandas["P3"][index]
        # print(test)
        if test >= 0.8:
            vendor_pandas["Group Code"][index] = 0
        else:
            vendor_pandas["Group Code"][index] = 1

    # Find specific SKUs from product_groups.yaml file and set group code
    for index, item in enumerate(vendor_pandas["NewPart"]):
      for key, value in group_code.items():
        if item == key:
          vendor_pandas["Group Code"][index] = value

    # Get length of dataframe and create new dimension columns
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Width"].replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace("", "0").astype(float)

    return vendor_pandas

