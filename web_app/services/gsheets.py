import pygsheets
import pandas as pd
import collections as col

#authorization
def push_to_sheets(coin1,coin2):
    gc = pygsheets.authorize(service_file='ibt-proj-81e46f86a85f.json')

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
    return coin_list


# def top_coins(input_list):
#     if push_to_sheets:
#         coin_counts = col.Counter(input_list)
#         sorted_counts = sorted(coin_counts.items(),key=lambda x:x[1],reverse=True)
#         top_coin = sorted_counts[0]
#         top_coin_name, top_coin_count = top_coin
#         print("TOP COIN:", top_coin_name, "COUNT:", top_coin_count)
#         top_coin2 = sorted_counts[1]
#         top_coin_name2, top_coin_count2 = top_coin2
#         print("TOP COIN:", top_coin_name2, "COUNT:", top_coin_count2)
#         top_coin3 = sorted_counts[2]
#         top_coin_name3, top_coin_count3 = top_coin3
#         print("TOP COIN:", top_coin_name3, "COUNT:", top_coin_count3)
#         return top_coin_name,top_coin_count,top_coin_name2,top_coin_count2,top_coin_name3,top_coin_count3