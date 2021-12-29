#
# knk.py
#
# This script holds functions for the vendor Wernerco (Weather Guard)
#
# Initial version - 03/24/2021 - Jason Grimes
#

from datetime import datetime
import pandas as pd
import unidecode

# Main vendor processing function
def do_knk(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    long_desc = "DESCRIPTION"
    frames = []

    # Process all sheets and label descriptions
    if "Jobsite" in vendor_pandas.keys() and not vendor_pandas["Jobsite"].empty:
      jobsite_pandas = vendor_pandas["Jobsite"]
      jobsite_pandas[long_desc] = jobsite_pandas[long_desc].apply(lambda x: "(Jobsite) " + x)
      sheetlen = len(jobsite_pandas.axes[0])
      new_column = list("2" * sheetlen)
      jobsite_pandas["Group Code"] = new_column

      # Replace missing values in Auth.
      for index, item in enumerate(jobsite_pandas["Auth."]):
          if item == "":
              jobsite_pandas["Auth."][index] = jobsite_pandas["Select\nTier 1"][index]

      jobsite_pandas["Select\nTier 1"] = jobsite_pandas["Auth."]

      # new_column = list("j" * sheetlen)
      # jobsite_pandas["type"] = new_column
      frames.append(jobsite_pandas)

    if "Van" in vendor_pandas.keys() and not vendor_pandas["Van"].empty:
      van_pandas = vendor_pandas["Van"]
      van_pandas["DESCRIPTION"] = van_pandas["DESCRIPTION"].apply(lambda x: "(Van) " + x)
      sheetlen = len(van_pandas.axes[0])
      new_column = list("1" * sheetlen)
      van_pandas["Group Code"] = new_column
      # new_column = list(" " * sheetlen)
      # van_pandas["type"] = new_column
      frames.append(van_pandas)

    if "Truck" in vendor_pandas.keys() and not vendor_pandas["Truck"].empty:
      truck_pandas = vendor_pandas["Truck"]
      truck_pandas[long_desc] = truck_pandas[long_desc].apply(lambda x: "(Truck) " + x)
      sheetlen = len(truck_pandas.axes[0])
      new_column = list("1" * sheetlen)
      truck_pandas["Group Code"] = new_column
      # new_column = list(" " * sheetlen)
      # truck_pandas["type"] = new_column
      frames.append(truck_pandas)

    # Concat all sheets into one data frame
    vendor_pandas = pd.concat(frames)
    vendor_pandas = vendor_pandas[(vendor_pandas["Trade"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["Trade"] != 0)]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Process part number
    vendor_pandas["Part Number"] = vendor_pandas["PART NUMBER"].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"]
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "KNK" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["Trade"]
    vendor_pandas["P1"] = vendor_pandas["P1"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["UAP"]

    # Replace missing values in P2
    for index, item in enumerate(vendor_pandas["P2"]):
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index] * tech_cal["P2"]

    vendor_pandas["P2"] = vendor_pandas["P2"].apply(lambda x: float(x))

    vendor_pandas["P5"] = vendor_pandas["Select\nTier 1"].replace("$", "")
    vendor_pandas["P5"] = vendor_pandas["P5"].replace(",", "").astype(float)

    vendor_pandas["P3"] = vendor_pandas["P1"] * tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]

    # Fix Jobsite values
    for index, item in enumerate(vendor_pandas["Desc1"]):
        if item[0:9] == "(JOBSITE)":
            vendor_pandas["P2"][index] = vendor_pandas["P1"][index]
            vendor_pandas["P3"][index] = vendor_pandas["P1"][index]
            vendor_pandas["P4"][index] = vendor_pandas["P1"][index]

    # for index, item in enumerate(vendor_pandas["type"]):
    #     if item == "j":
    #         vendor_pandas["P2"][index] = vendor_pandas["P1"][index]
    #         vendor_pandas["P3"][index] = vendor_pandas["P1"][index]
    #         vendor_pandas["P4"][index] = vendor_pandas["P1"][index]
    #     if vendor_pandas["P1"][index] == vendor_pandas["P5"][index] and item != "j":
    #         vendor_pandas["P1"][index] = vendor_pandas["P5"][index] / .6336
    #         vendor_pandas["P3"][index] = vendor_pandas["P1"][index] * tech_cal["P3"]
    #         vendor_pandas["P2"][index] = vendor_pandas["P1"][index] * tech_cal["P2"]
    #         vendor_pandas["P4"][index] = vendor_pandas["P1"][index] * tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight (Lbs)"].replace("","0")
    vendor_pandas["Weight"] = vendor_pandas["Weight"].astype(float)

    return vendor_pandas
