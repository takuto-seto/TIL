# "price" が抜けているデータや、空のデータを入れたデータ
broken_sales_data = [
    {"item": "りんご", "price": 150, "category": "fruit"},
    {"item": "不明な商品", "category": "fruit"}, # priceがない！
    {"item": "バナナ", "price": 200, "category": "fruit"},
]

def get_category_total_safe(data, category_name):
    total = 0
    for row in data:
        if row.get("category") == category_name:
            # ここで price があるかチェックしてから足したい
            # ヒント：row.get("price", 0) を使うと、なければ 0 を返してくれます
            total += row.get("price", 0)
    return total

print(f"安全な集計結果: {get_category_total_safe(broken_sales_data, 'fruit')}")