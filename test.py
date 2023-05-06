import collections as col

def top_coins(input_list):
    coin_counts = col.Counter(input_list)
    sorted_counts = sorted(coin_counts.items(),key=lambda x:x[1],reverse=True)
    top_coin = sorted_counts[0]
    top_coin_name, top_coin_count = top_coin
    print("TOP COIN:", top_coin_name, "COUNT:", top_coin_count)
    top_coin2 = sorted_counts[1]
    top_coin_name2, top_coin_count2 = top_coin2
    print("TOP COIN:", top_coin_name2, "COUNT:", top_coin_count2)
    top_coin3 = sorted_counts[2]
    top_coin_name3, top_coin_count3 = top_coin3
    print("TOP COIN:", top_coin_name3, "COUNT:", top_coin_count3)
    return top_coin_name,top_coin_count,top_coin_name2,top_coin_count2,top_coin_name3,top_coin_count3


