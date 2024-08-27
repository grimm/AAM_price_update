#
# tfi.py
#
# This script holds functions for the vendor Fisher Snow Plows
#
# Initial version - 08/15/2024 - Jason Grimes
#
# Initial fixes that have to happen to the input files
#
# Fisher_Preseason_Truck_Equipment_Price_Manual_-_NET.xlsx file
#
# A lot of manual work needs to be done on the input files.  There are two files (Truck and Non-Truck) that need to be 
# merged and processed before you can import it with the script.  Go through all of the tabs in both files and do a select
# all, then paste back the data as values.  This will remove all formulas so they don't mess things up later.  Then make
# sure that all of the rows before the header row count to 7.  If there are less instert more, if more, delete rows until
# there are just 7.  Some of the data cells have been merged vertically, these need to be unmerged and the content of the top
# cell needs to be copied to the other cells bellow.  Rename all of the "NET %" headers to "NET" so they all end up in the 
# correct column.  Rename all "MODEL" headers to "DESCRIPTION" so they end up in the correct column.  Rename all "Part" and
# "PART#" to "PART".  Make sure all headers are uppercase.  
#
# Remove any sheet tabs that are not needed, like the cover pages, etc.  Now move the remaining tabs over to one spreadsheet
# file.  I usually move the non-truck tabs over to the truck file.  Now you can import the truck file into the script to 
# convert it to a CSV file.
#

from datetime import datetime
import pandas as pd
import unidecode

# Main vendor processing function
def do_fish(vendor_pandas, tech_cal):
    # concatinate all dataframes
    frames = []
    sheets = ["BLADE-ATTACHMENT", "MOUNT KITS", "MOUNT KITS 2", "ELECTRICAL", "PLOW ACCESSORIES PG. 1", "PLOW ACCESSORIES PG. 2", "CUTTING EDGES", "TAILGATE SPREADERS", "HOPPER SPREADERS & PREWET", "SPREADER ACCESSORIES", "SIDEWALKS", "Plows - HD UTV", "Plows - MD UTV", "Plows -Subcompact Tractor", "Plows - Skid Steer", "Plows - Tractor", "Skid and Tractor Plow Accs", "Pusher Plows", "Hopper Spreaders", "Tailgate Spreaders (2)", "Drop Spreaders", "Sidewalk Management", "Additional Accessories"]

    for sheet in sheets:
        frames.append(vendor_pandas[sheet])

    vendor_pandas = pd.concat(frames)

    # temp_pandas = pd.DataFrame()
    # for dataf in vendor_pandas:
    #     print(dataf[2])
    #     pd.merge(temp_pandas, dataf[2])
    # vendor_pandas = temp_pandas

    # Remove in rows with no data
    vendor_pandas = vendor_pandas[(vendor_pandas["PART"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["PART"] != "PART")]
    vendor_pandas = vendor_pandas[(vendor_pandas["DESCRIPTION"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["LIST"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["LIST"] != "LIST")]
    vendor_pandas = vendor_pandas[(vendor_pandas["LIST"] != "List")]
    vendor_pandas = vendor_pandas[(vendor_pandas["NET"] != "Net")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Put really long header text in some vars
    long_desc = "DESCRIPTION"

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['PART'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "FISH" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[long_desc].astype(str)
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\"', 'in')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\'', 'ft')

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["LIST"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["NET"].astype(float)

    vendor_pandas["P2"] = vendor_pandas["P1"] * tech_cal["P2"]
    vendor_pandas["P3"] = vendor_pandas["P1"] * tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P1"] * tech_cal["P4"]
    # print(vendor_pandas["JOBBER"])

    # Get length of dataframe and create new dimension columns
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas

