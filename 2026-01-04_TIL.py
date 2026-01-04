# 「指定されたカテゴリー」の合計売上金額を計算する関数の作成

# APIから返ってきた想定のデータ
sales_data = [
    {"item": "りんご", "price": 150, "category": "fruit"},
    {"item": "テレビ", "price": 50000, "category": "electronics"},
    {"item": "バナナ", "price": 200, "category": "fruit"},
    {"item": "洗濯機", "price": 80000, "category": "electronics"},
    {"item": "メロン", "price": 2000, "category": "fruit"},
]

def get_category_total(data, category_name):
    # # ここにロジックを書いてください
    total = 0

    # for item_dict in data:
    #     if  item_dict["category"] == category_name:
    #         total += item_dict["price"]

    # return total

    #リスト内包表記
    return sum(item["price"] for item in data if item["category"] == category_name)

# テスト
print(get_category_total(sales_data, "fruit"))       # 2350 が出れば正解！
print(get_category_total(sales_data, "electronics")) # 130000 が出れば正解！