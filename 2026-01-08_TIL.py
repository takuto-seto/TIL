sales_data = [
    {"item": "りんご", "price": 150, "category": "fruit"},
    {"item": "テレビ", "price": 50000, "category": "electronics"},
    {"item": "バナナ", "price": 200, "category": "fruit"},
    {"item": "洗濯機", "price": 80000, "category": "electronics"},
]

def group_by_category(data):
    result = {}

    try:

        for item_list in data:
            cat = item_list["category"]
            name = item_list["item"]

            if cat not in result:
                result[cat] = []

            result[cat].append(name)

        return result
        
    except Exception as e:
        return "errorが発生"
    
print(group_by_category(sales_data))