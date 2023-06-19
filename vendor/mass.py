#
# mass.py
#
# This script holds functions to import the mass update report FACS IMS200
#
# Initial version - 04/16/2021 - Jason Grimes
#

from datetime import datetime
import unidecode
import csv

# Main vendor processing function
def do_mass(vendor_pandas, tech_cal):
    # Remove parts that are discontinued (WES)
    # vendor_pandas = vendor_pandas[(vendor_pandas["Stat"] != "D")]
    # vendor_pandas = vendor_pandas.reset_index(drop=True)

    # Create new Status/NewPart columns
    vendor_pandas['Part Number'] = vendor_pandas['Supplier Part No.'].astype(str)
    # vendor_pandas["NewPart"] = vendor_pandas["#"].astype(str)

    # FED (Federal Signal)
    vendor_pandas["NewPart"] = vendor_pandas["Part Number"].apply(lambda x: "FED" + x)

    # WES
    # vendor_pandas["NewPart"] = vendor_pandas["Part"].astype(str)

    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["Part Description"]
    vendor_pandas["Desc2"] = vendor_pandas["Extra Description"]

    # WES
    # vendor_pandas["Desc1"] = vendor_pandas["Description"]
    # vendor_pandas["Desc2"] = vendor_pandas["Extra Description"]

    # Create all price fields
    # vendor_pandas["P1"] = vendor_pandas["Price #1"].astype(float)
    # vendor_pandas["P2"] = vendor_pandas["Price #2"].astype(float)
    # vendor_pandas["P3"] = vendor_pandas["Price #3"].astype(float)
    # vendor_pandas["P4"] = vendor_pandas["Price #4"].astype(float)
    # vendor_pandas["P5"] = vendor_pandas["P3"] * tech_cal["P5"] * tech_cal["P6"]
    # Western (WEST) add surcharge (%40)
    # vendor_pandas["P5"] = vendor_pandas["Price #5"] * 1.4

    # Create all price fields (Tech)
    vendor_pandas["P1"] = vendor_pandas["Price #1"].astype(float)
    vendor_pandas["P2"] = vendor_pandas["Price #2"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["Price #3"].astype(float)
    vendor_pandas["P4"] = vendor_pandas["Price #4"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["Price #5"].astype(float)

    # Create all price formulas (KNP)
    # len_pandas = len(vendor_pandas["Part Number"])
    # print(len_pandas)

    # vendor_pandas["P1"] = ["P5/.5"] * len_pandas
    # vendor_pandas["P2"] = ["P5/.6"] * len_pandas
    # vendor_pandas["P3"] = ["P5/.7"] * len_pandas
    # vendor_pandas["P4"] = ["P5/.8"] * len_pandas
    # vendor_pandas["P5"] = ["GC"] * len_pandas

    # Just change P2 for MAP update Pedal Commander (PC)
    # vendor_pandas["P1"] = vendor_pandas["Price #1"].astype(float)
    # vendor_pandas["P2"] = "349.99" * len_pandas
    # vendor_pandas["P3"] = vendor_pandas["Price #3"].astype(float)
    # vendor_pandas["P4"] = vendor_pandas["Price #4"].astype(float)
    # vendor_pandas["P5"] = vendor_pandas["Price #5"].astype(float)

    # ULT price update +15%
    # vendor_pandas["P1"] = vendor_pandas["Price #1"] * 1.15
    # vendor_pandas["P2"] = vendor_pandas["Price #2"] * 1.15
    # vendor_pandas["P3"] = vendor_pandas["Price #3"] * 1.15
    # vendor_pandas["P4"] = vendor_pandas["Price #4"] * 1.15
    # vendor_pandas["P5"] = vendor_pandas["Price #5"] * 1.15

    # Set product status
    # len_pandas = len(vendor_pandas.axes[0])
    # new_column = list("D" * len_pandas)
    # vendor_pandas["Status"] = new_column

    # Set profit number
    len_pandas = len(vendor_pandas.axes[0])
    new_column = list("2" * len_pandas)
    vendor_pandas["Profit"] = new_column

    # for index, item in enumerate(vendor_pandas["Profit"]):
    #     vendor_pandas["Profit"][index] = "FED"

    # Set product group code (Tech)
    # vendor_pandas["Group Code"] = vendor_pandas["Code"].astype(int)

    return vendor_pandas

