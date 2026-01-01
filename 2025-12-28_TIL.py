def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]  # これまでの最安値を記録
    profit = 0             # 最大利益を記録
    
    for i in range(1, len(prices)):
        # 1. もし「今日(prices[i])売った時の利益」が、
        #    これまでの「profit」より大きければ更新する
        #    利益 = 今日の価格 - min_price

        if prices[i] - min_price > profit:
            profit = prices[i] - min_price

        # 2. もし「今日(prices[i])の価格」が、
        #    これまでの「min_price」より安ければ更新する
        if prices[i] < min_price:
            min_price = prices[i]

            
    return profit

# テストデータ
prices = [7, 1, 5, 3, 6, 4]
print(f"最大利益: {max_profit(prices)}") # 5 が出れば正解！

# よりスッキリする書き方↓
# for i in range(1, len(prices)):
#     # 利益を「今の利益」と「今日売った時の利益」の大きい方で更新
#     profit = max(profit, prices[i] - min_price)
    
#     # 最安値を「今の最安値」と「今日の価格」の小さい方で更新
#     min_price = min(min_price, prices[i])