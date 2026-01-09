dirty_data = [
    {"item": "りんご", "price": 150, "category": "Fruit"},      # カテゴリーが大文字混じり
    {"item": "テレビ", "price": "50000", "category": "electronics"}, # 価格が文字列
    {"item": "バナナ", "price": None, "category": "fruit"},     # 価格が欠損（無視する）
    {"item": "壊れた商品", "price": "文字", "category": "etc"}, # 価格が変換不能（無視する）
    {"item": "洗濯機", "price": 80000, "category": "ELECTRONICS"}, # カテゴリーが全部大文字
]


def clean_and_analyze_sales(data):
    result = {}

    try:
            for item_dict in data:
                cat = item_dict["category"].lower()

                try: 
                     price = int(item_dict["price"])
                except (ValueError, TypeError):
                     continue
                
                name = item_dict["item"]

                if cat not in result:
                     result[cat] = {"total_price": 0, "items": []}

                result[cat]["total_price"] += price
                result[cat]["items"].append(name)

            return result
                
    except Exception as e:
        return "error"
    
print(clean_and_analyze_sales(dirty_data))