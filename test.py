import collections as col

coins_list =['BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BTC', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'BNB', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'ETH', 'LTC', 'BTC', 'BNB', 'BDL', 'BEE', 'BELA', 'BELA', 'BELA', 'BELA', 'BELA', 'BELA', 'BELA', 'BELA', 'BELA', 'BIS', 'BDL', 'BEE', 'BELA', 'BELA', 'BELA', 'BELA', 'BELA', 'BEE', 'BDL', 'BDL', 'BDL', 'BDL', 'BDL', 'BEE', 'BELA', 'BET', 'BFT', 'BFT', 'BFT', 'BFT', 'BEE', 'BEE', 'BEE', 'BEE', 'BEE', 'BTC', 'BTC']
print(coins_list)

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
    
        


top_coins(coins_list)



