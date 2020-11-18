#
# ard.py
#
# This script holds functions for the vendor Airaid
#
# Note: To get the Excel file to work you must remove the first line so the header
#       imports correctly.
#
# Initial version - 10/01/2020 - Jason Grimes
#
from datetime import datetime

# Main vendor processing function
def do_ard(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Remove promotional items
    vendor_pandas = vendor_pandas[~((vendor_pandas["Jobber"] == vendor_pandas["AAM Cost"]) | (vendor_pandas["MSRP/List"] == vendor_pandas["AAM Cost"]))]
    vendor_pandas = vendor_pandas[~(vendor_pandas[short_desc] == "AIRAID Trucker Hat")]

    # Get length of dataframe and create new Status/NewPart columns
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("A" * len_pandas)

    vendor_pandas["NewPart"] = new_column
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "ARD" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc]
    vendor_pandas["Desc2"] = vendor_pandas[short_desc]

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"]
    vendor_pandas["P2"] = vendor_pandas["P3"] / tech_cal["P2"]
    vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"]
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Weight - IN POUNDS"]
    vendor_pandas["Status"] = new_column

    # Write out discontinued parts
    #------------------------------
    date = datetime.today().strftime('%m-%d-%y')
    discon_file = "ARD_Discontinued_" + date + ".csv"

    #           new_part   part          descriptions       P1    P2    P3    P4    P5
    columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5",
               "Length", "Width", "Height", "Weight", "Status"]

    # Separate out the discontinued parts from the others
    discon_pandas = vendor_pandas[vendor_pandas[short_desc].str.match("Discontinued")]
    update_pandas = vendor_pandas[~vendor_pandas[short_desc].isin(discon_pandas[short_desc])]

    # Set status field
    len_pandas = len(discon_pandas.axes[0])
    new_column = list("D" * len_pandas)
    discon_pandas["Status"] = new_column

    discon_pandas.to_csv(discon_file, columns=columns, header=False, index=False, float_format="%.2f", sep="|")
    print("Saved - " + discon_file + " discontinued parts file.")

    return update_pandas

