#
# tim.py
#
# This script holds functions for the vendor tim
#
# Initial version - 9/24/2020 - Jason Grimes
#

# Main vendor processing function
def do_tim(vendor_pandas, vend_cal):
    # Remove junk at the end of the dataframe
    vendor_pandas = vendor_pandas.head(-2)
    
    # Remove CRs from header
    vendor_pandas.columns=vendor_pandas.columns.str.replace('\n','')

    # Copy Part # column to NewPart column and modify to add TIM
    vendor_pandas.loc[:,"NewPart"] = vendor_pandas["PART #"]
    vendor_pandas["NewPart"] = vendor_pandas["NewPart"].apply(lambda x: "TIM" + x)
    
    # Create new description columns
    vendor_pandas.loc[:,"Desc1"] = vendor_pandas["Description"]
    vendor_pandas.loc[:,"Desc2"] = vendor_pandas["Description"]

    # Create description 1 and 2
    # Upper case text and trim it to 30 characters
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].str.upper()
    vendor_pandas["Desc1"] = vendor_pandas["Desc1"].apply(lambda x: x[:30])
    vendor_pandas["Desc2"] = vendor_pandas["Desc2"].apply(lambda x: "")

    # Convert dollar amounts to float
    vendor_pandas["US $           J - 31%"] = vendor_pandas["US $           J - 31%"].replace( '[$]','', regex=True ).replace( '[,]','', regex=True ).astype(float)

    # Create P2 and P4 by calculation
    vendor_pandas["P4"] = vendor_pandas["US $           J - 31%"] / vend_cal["P4"]

    # Check to see if a MAP column exists, if not then P3/vend_cal
    if vend_cal["main"] in vendor_pandas.columns:
        vendor_pandas["P2"] = vendor_pandas[vend_cal["main"]].astype(float)
    else:
        vendor_pandas["P2"] = vendor_pandas[vend_cal["US $ JOBBER"]].astype(float) / vend_cal["P2"]

    return vendor_pandas
