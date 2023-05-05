import pygsheets
import pandas as pd
#authorization
def push_to_sheets(coin1,coin2):
    gc = pygsheets.authorize(service_file='ibt-proj-81e46f86a85f.json')

    # # Create empty dataframe
    
    # df = pd.DataFrame()

    # # Create a column
    # df['coins'] = []
    # df.append
    

    # #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    # sh = gc.open('Favorite coins')

    # #select the first sheet 
    # wks = sh[0]

    # #update the first sheet with df, starting at cell B2. 
    # wks.set_dataframe(df,(1,1))
    sh = gc.open('Favorite coins')
    user_coins = [coin1,coin2]
    wk1 = sh[0]
    df = wk1.get_as_df()
    print(df)
    coin_list = df['coins'].values.tolist()
    coin_list.extend(user_coins)
    print(coin_list)
    new_df = pd.DataFrame(coin_list)
    new_df.rename(columns={"0":"coins"})
    print(new_df)
    wk1.set_dataframe(new_df,(1,1))
    wk1.update_value('A1','coins')