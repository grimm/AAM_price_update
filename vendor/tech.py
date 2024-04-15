#
# tech.py
#
# This script holds functions for the vendor WeatherTech
#
# Initial version - 9/24/2020 - Jason Grimes
#

import unidecode
import re
import yaml

# Main vendor processing function
def do_tech(vendor_pandas, prod_group, tech_cal, new_cal):
    if not new_cal:
        # Remove promotional stuff (normal)
        vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "Hoodie ")]
        vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "Racing Polo")]
        vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "T-Shirt")]
        vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "Hat ")]
        vendor_pandas = vendor_pandas[(vendor_pandas["Product Group"] != "African Copper Bracelet")]

        vendor_pandas = vendor_pandas[(vendor_pandas["TTK"] != "")]

        vendor_pandas = vendor_pandas.reset_index(drop=True)

        # Copy Part column to NewPart column and modify to add TECH (normal)
        vendor_pandas["NewPart"] = vendor_pandas["Part"].astype(str)
        vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "TECH" + x)
    else:
        # Get part SKUs
        vendor_pandas["Part"] = vendor_pandas["Supplier Part No."].astype(str)
        vendor_pandas["NewPart"] = vendor_pandas["#"].astype(str)

    if not new_cal:
        # Create description 1 (normal)
        # Only concat columns if the Color column has text in it
        vendor_pandas["Desc1"] = vendor_pandas["Product Group"]

        for index, item in enumerate(vendor_pandas["Desc1"]):
            # print(index, vendor_pandas["Color"][index])
            if vendor_pandas["Color"][index] != "NA":
                vendor_pandas["Desc1"][index] = item + "; " + vendor_pandas["Color"][index]

        # Upper case text and trim it to 30 characters
        vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
        
        vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\"", "IN")
        vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace("\'", "FT")

        vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
        vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

        # Create description 2
        # Concat the Make, Model, and Year columns
        vendor_pandas["Desc2"] = vendor_pandas["Make"].astype(str) + " " + vendor_pandas["Model"].astype(str) + " " + vendor_pandas["Year"].astype(str)
        vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.replace("+", "")
        vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[:30]).str.upper()
        vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: unidecode.unidecode(x))

    else:
        # Descriptions (mass update)
        vendor_pandas["Desc1"] = vendor_pandas["Part Description"]
        vendor_pandas["Desc2"] = vendor_pandas["Extra Description"]

    if not new_cal:
        # Create price numbers (normal)
        vendor_pandas["TTK"] = vendor_pandas["TTK"].astype(float)
        vendor_pandas["Surcharge Fee"] = vendor_pandas["Surcharge Fee"].replace("", "0.0").astype(float)
        vendor_pandas["P5"] = vendor_pandas["TTK"] + vendor_pandas["Surcharge Fee"]
        # for index, item in enumerate(vendor_pandas["P5"]):
        #     try:
        #         vendor_pandas["P5"][index] = item + float(tech_sur[vendor_pandas["Part"][index]])
        #     except KeyError:
        #         # print(item)
        #         print(vendor_pandas["Part"][index])
        #         continue

        colnames = list(vendor_pandas.columns)
        if ('MAP or Sug. Ret' in colnames):
            vendor_pandas["P1"] = vendor_pandas["MAP or Sug. Ret"]
        else:
            vendor_pandas["P1"] = vendor_pandas["MAP"]

        if ('JOB' in colnames):
            vendor_pandas["P3"] = vendor_pandas["JOB"]
        else:
            vendor_pandas["P3"] = vendor_pandas["Jobber"]

        vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
        vendor_pandas["P4"] = vendor_pandas["P4"].astype(float)
        vendor_pandas["P3"] = vendor_pandas["P3"].astype(float)
        vendor_pandas["P2"] = vendor_pandas["P1"]
    else:
        # Get prices (mass update)
        vendor_pandas["P1"] = vendor_pandas["Price #1"].astype(float)
        vendor_pandas["P2"] = vendor_pandas["Price #2"].astype(float)
        vendor_pandas["P3"] = vendor_pandas["Price #3"].astype(float)
        vendor_pandas["P4"] = vendor_pandas["Price #4"].astype(float)
        vendor_pandas["P5"] = vendor_pandas["Price #5"].astype(float)

        # run this only once!!!!!!!!!!!!
        for index, item in enumerate(vendor_pandas["P5"]):
            try:
                vendor_pandas["P5"][index] = item + float(tech_sur[vendor_pandas["Part"][index]])
            except KeyError:
                continue

    if not new_cal:
        # Build group codes column (normal)
        vendor_pandas["Group"] = vendor_pandas["Product Group"]
   
        for index, item in enumerate(vendor_pandas["Product Group"]):
            vendor_pandas["Group"][index] = 99999
            for key, value in prod_group["tech"].items():
                if item == key:
                    vendor_pandas["Group"][index] = value
                if vendor_pandas["Make"][index] == "Ferrari" or vendor_pandas["Make"][index] == "Bugatti":
                    vendor_pandas["Group"][index] = 0
            if vendor_pandas["Group"][index] == 99999:
                # print("******* Warning - " + item + " not found in product groups!")
                # print(item + "*")
                print(item)
    else:
        # Get group codes (mass update)
        vendor_pandas["Group"] = vendor_pandas["Code"]

    # Build Nelson cost from the TTK column
    vendor_pandas["NP5"] = vendor_pandas["P5"] # * 1.01

    #if not new_cal:
    #    vendor_pandas["Length"] = vendor_pandas["Length"].apply(lambda x: re.sub("\D", "", str(x)))
    #    vendor_pandas["Width"] = vendor_pandas["Width"].apply(lambda x: re.sub("\D", "", str(x)))
    #    vendor_pandas["Height"] = vendor_pandas["Height"].apply(lambda x: re.sub("\D", "", str(x)))

    vendor_pandas["Length"] = vendor_pandas["Length"].astype(str)
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(str)
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(str)

    vendor_pandas["Length"] = vendor_pandas["Length"].apply(lambda x: x.replace('"',''))
    vendor_pandas["Width"] = vendor_pandas["Width"].apply(lambda x: x.replace('"',''))
    vendor_pandas["Height"] = vendor_pandas["Height"].apply(lambda x: x.replace('"',''))

    return vendor_pandas

