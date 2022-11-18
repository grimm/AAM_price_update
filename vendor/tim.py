#
# tim.py
#
# This script holds functions for the vendor Timbren
#
# Initial version - 9/24/2020 - Jason Grimes
#

# Main vendor processing function
def do_tim(vendor_pandas, tech_cal):
    # Remove junk in the file
    vendor_pandas = vendor_pandas.head(-2)
    
    # Copy Part # column to NewPart column and modify to add TIM
    vendor_pandas["NewPart"] = vendor_pandas["PART #"]
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "TIM" + x)
    
    # Create new description columns
    vendor_pandas["Desc1"] = vendor_pandas["PRODUCT DESCRIPTION"]

    # Create description 1 and 2
    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc2"] = vendor_pandas["Desc1"].apply(lambda x: x[30:60])
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])

    # Convert dollar amounts to float
    vendor_pandas["P1"] = vendor_pandas["USD List"].replace( '[$]','', regex=True ).replace( '[,]','', regex=True ).astype(float)
    vendor_pandas["P2"] = vendor_pandas["USD MAP"].astype(float)
    vendor_pandas["P3"] = vendor_pandas["USD JOBBER"].astype(float)
    vendor_pandas["P5"] = vendor_pandas["USD J - 31%"].astype(float)

    # Create P2 and P4 by calculation
    vendor_pandas["P4"] = vendor_pandas["P5"] / tech_cal["P4"]

    # Set dimensions and status
    vendor_pandas["Weight"] = vendor_pandas["Shipping Weight (Lbs.)"].replace("", "0")
    vendor_pandas["Length"] = vendor_pandas["BOX \n(L)      (inches)"].replace("", "0")
    vendor_pandas["Width"] = vendor_pandas["BOX \n(D)  (inches)"].replace("", "0")
    vendor_pandas["Height"] = vendor_pandas["BOX\n(H) (inches)"].replace("", "0")

    return vendor_pandas
