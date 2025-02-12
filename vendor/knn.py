#
# knn.py
#
# This script holds functions for the vendor K & N
#
# Initial version - 10/19/2020 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_knn(vendor_pandas, tech_cal):
    # Put really long header text in some vars
    short_desc = "Short Description (20 Characters or Less)"
    long_desc = "Long Description 100 Characters or less WITHOUT application information"

    # Get length of dataframe and create new NewPart column
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("A" * len_pandas)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "KNN" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas[short_desc] + " " + vendor_pandas[long_desc]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))

    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].str.upper()

    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: x[30:60])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MSRP/List"]
    vendor_pandas["P3"] = vendor_pandas["Jobber"]
    vendor_pandas["P5"] = vendor_pandas["AAM Cost"]

    vendor_pandas["P2"] = vendor_pandas["AAM Cost"]
    for index, item in enumerate(vendor_pandas["MAP Retail"]):
        #print(index)
        if item == "":
            vendor_pandas["P2"][index] = vendor_pandas["P3"][index] / tech_cal["P2"]
        else:
            vendor_pandas["P2"][index] = item

    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]
    vendor_pandas["Status"] = new_column

    # Set dimensions and status
    lname = "Weight - IN POUNDS"
    vendor_pandas[lname] = vendor_pandas[lname].astype(str)
    vendor_pandas[lname] = vendor_pandas[lname].str.replace('TBD', '0')
    vendor_pandas["Weight"] = vendor_pandas[lname].astype(float)

    vendor_pandas["Length"] = vendor_pandas[lname].astype(str)
    vendor_pandas["Length"] = vendor_pandas["Length"].str.replace('TBD', '0')
    vendor_pandas["Length"] = vendor_pandas["Length"].astype(float)

    vendor_pandas["Width"] = vendor_pandas[lname].astype(str)
    vendor_pandas["Width"] = vendor_pandas["Width"].str.replace('TBD', '0')
    vendor_pandas["Width"] = vendor_pandas["Width"].astype(float)

    vendor_pandas["Height"] = vendor_pandas[lname].astype(str)
    vendor_pandas["Height"] = vendor_pandas["Height"].str.replace('TBD', '0')
    vendor_pandas["Height"] = vendor_pandas["Height"].astype(float)

    # Write out discontinued parts
    #------------------------------
    date = datetime.today().strftime('%m-%d-%y')
    discon_file = "KNN_Discontinued_" + date + ".csv"

    #           new_part   part          descriptions       P1    P2    P3    P4    P5
    columns = ["NewPart", "Part Number", "Desc1", "Desc2", "P1", "P2", "P3", "P4", "P5",
               "Length", "Width", "Height", "Weight", "Status"]

    # Separate out the discontinued parts from the others
    discon_pandas = vendor_pandas[vendor_pandas[short_desc].str.contains("Discontinued|To Be Discontinued")]
    update_pandas = vendor_pandas[~vendor_pandas[short_desc].isin(discon_pandas[short_desc])]

    # Set status field
    len_pandas = len(discon_pandas.axes[0])
    new_column = list("D" * len_pandas)
    discon_pandas["Status"] = new_column

    discon_pandas.to_csv(discon_file, columns=columns, header=False, index=False, float_format="%.2f", sep="|", quoting=csv.QUOTE_NONE)
    print("Saved - " + discon_file + " discontinued parts file.")

    return update_pandas

