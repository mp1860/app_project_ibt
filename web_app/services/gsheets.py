import pygsheets
import pandas as pd
#authorization
def push_to_sheets(coin1,coin2):
    gc = pygsheets.authorize(service_file='google-credentials.json')

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['coins'] = [coin1, coin2]

    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open('products')

    #select the first sheet 
    wks = sh[0]

    #update the first sheet with df, starting at cell B2. 
    wks.set_dataframe(df,(1,1))

    print(coin1,coin2)