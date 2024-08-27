#
# wes.py
#
# This script holds functions for the vendor Westin
#
# Initial version - 1/12/2021 - Jason Grimes
#
#
#  ALSO UPDATE SUPERWINCH AT THE SAME TIME!!!!!!
#  Add a -n to the command line to specifically process SuperWinch parts
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_wes(vendor_pandas, prod_group, tech_cal, new_cal):
    # Remove N/A parts
    vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "N/A")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Jobber"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Set text to pull out display parts
    bad_parts = ["Display", "Sample", "Catalog", "Guide", "Brochure", "Public", "Profile", "display", "Banner"]

    # Remove displays and pricing quote rows
    vendor_pandas = vendor_pandas[(vendor_pandas["MSRP/List"] != "0.00")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "Emailed for Cost")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "emailed for Cost")]
    vendor_pandas = vendor_pandas[(vendor_pandas["AAM Cost"] != "emailed Mike S for Cost")]
    vendor_pandas = vendor_pandas[~vendor_pandas[long_desc].str.contains('|'.join(bad_parts))]
    vendor_pandas = vendor_pandas[~vendor_pandas[short_desc].str.contains('|'.join(bad_parts))]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "WES" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")
    
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["MAP Retail"]
    for index, item in enumerate(vendor_pandas["P2"]):
        #print(index)
        if new_cal == 1:
            print(vendor_pandas["P1"][index])
            print(vendor_pandas["P2"][index])
            print(vendor_pandas["P3"][index])
            if vendor_pandas["P1"][index] == "" and vendor_pandas["P2"][index] == "":
                print("Got to 1")
                vendor_pandas["P1"][index] = vendor_pandas["P3"][index]
                vendor_pandas["P2"][index] = vendor_pandas["P3"][index]

            if vendor_pandas["P1"][index] != "" and vendor_pandas["P2"][index] == "":
                print("Got to 2")
                vendor_pandas["P2"][index] = vendor_pandas["P1"][index]

            elif vendor_pandas["P1"][index] == "" and vendor_pandas["P2"][index] != "":
                print("Got to 3")
                vendor_pandas["P1"][index] = vendor_pandas["P2"][index]

            # if vendor_pandas["P1"][index] == "":
            #     vendor_pandas["P1"][index] = vendor_pandas["P3"][index]

        else:
          if item == "":
              vendor_pandas["P2"][index] = vendor_pandas["P1"][index] * tech_cal["P2"]
          else:
              vendor_pandas["P2"][index] = item

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P2"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Length"] = vendor_pandas["Length"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Width"] = vendor_pandas["Weight"].replace(" ", "0").replace("", "0").astype(float)
    vendor_pandas["Height"] = vendor_pandas["Height"].replace(" ", "0").replace("", "0").astype(float)

    # Set product groups
    vendor_pandas["Group Code"] = vendor_pandas["NewPart"]
    for index, item in enumerate(vendor_pandas[short_desc]):
        if new_cal == 1:
          vendor_pandas["Group Code"][index] = 1
        else:
          vendor_pandas["Group Code"][index] = 99999
          for key, value in prod_group.items():
              if item == key or vendor_pandas[long_desc][index] == key:
                  vendor_pandas["Group Code"][index] = value
          if vendor_pandas["Group Code"][index] == 99999:
              print(item)

    return vendor_pandas

