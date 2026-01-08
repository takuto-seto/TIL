# sales_data = [
#     {"item": "りんご", "price": 150, "category": "fruit"},
#     {"item": "テレビ", "price": 50000, "category": "electronics"},
#     {"item": "バナナ", "price": 200, "category": "fruit"},
#     {"item": "洗濯機", "price": 80000, "category": "electronics"},
# ]

# def group_by_category(data):
#     result = {}

#     try:

#         for item_list in data:
#             cat = item_list["category"]
#             name = item_list["item"]

#             if cat not in result:
#                 result[cat] = []

#             result[cat].append(name)

#         return result
        
#     except Exception as e:
#         return "errorが発生"
    
# print(group_by_category(sales_data))



# 今回の入力データ
sales_data = [
    {"item": "りんご", "price": 150, "category": "fruit"},
    {"item": "テレビ", "price": 50000, "category": "electronics"},
    {"item": "バナナ", "price": 200, "category": "fruit"},
]

def analyze_sales_deep(data):
    result = {}

    try:
        for item_dict in data:
            cat = item_dict["category"]
            name = item_dict["item"]
            price = item_dict["price"]

            if cat not in result:
                result[cat] = {"total_price": 0, "items": []}
            
            result[cat]["total_price"] += price

            result[cat]["items"].append(name)
                
        
        return result



    except Exception as e:
        return "error"
    

print(analyze_sales_deep(sales_data))

# --- 期待される出力（イメージ） ---
# {
#   "fruit": {
#       "total_price": 350,
#       "items": ["りんご", "バナナ"]
#   },
#   "electronics": {
#       "total_price": 50000,
#       "items": ["テレビ"]
#   }
# }