#
# pc.py
#
# This script holds functions for the vendor Pedal Commander
#
# Initial version - 02/25/2022 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_pc(vendor_pandas, tech_cal):
    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Part Number'].str.replace(" ", "")
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: x + "-BT")
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Description"]
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: unidecode.unidecode(x))
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\"', 'in')
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.replace('\'', 'ft')

    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Create all price fields
    vendor_pandas["P1"] = vendor_pandas["MAP"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["P1"]
    vendor_pandas["P5"] = vendor_pandas["Cost"].astype(float)

    vendor_pandas["P3"] = vendor_pandas["P5"] / tech_cal["P3"]
    vendor_pandas["P4"] = vendor_pandas["P3"]

    # Set dimensions and status
    # Make sure that measurement values are correct
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("0" * len_pandas)

    vendor_pandas["Weight"] = new_column
    vendor_pandas["Length"] = new_column
    vendor_pandas["Height"] = new_column
    vendor_pandas["Width"] = new_column

    # Set product groups
    vendor_pandas["Group"] = new_column

    return vendor_pandas

