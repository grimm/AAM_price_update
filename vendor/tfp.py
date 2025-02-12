#
# tfp.py
#
# This script holds functions for the vendor TFP
#
# Initial version - 03/21/2022 - Jason Grimes
#

from datetime import datetime
import unidecode

# Main vendor processing function
def do_tfp(vendor_pandas, tech_cal):
    # Remove in rows with no data
    vendor_pandas = vendor_pandas[(vendor_pandas["UPC"] != "")]
    vendor_pandas = vendor_pandas[(vendor_pandas["UPC"] != "UPC")]
    vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Put really long header text in some vars
    long_desc = "DESCRIPTION"

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['PART#'].astype(str)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "TFP" + x)
    
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
    vendor_pandas["P3"] = vendor_pandas["JOBBER $"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["MWD $"].astype(float)

    vendor_pandas["P1"] = vendor_pandas["P3"] / tech_cal["P1"]
    vendor_pandas["P2"] = vendor_pandas["P3"] / tech_cal["P2"]
    vendor_pandas["P4"] = vendor_pandas["P3"] * tech_cal["P4"]

    # Get length of dataframe and create new dimension columns
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Width"] = new_column
    vendor_pandas["Height"] = new_column

    return vendor_pandas

