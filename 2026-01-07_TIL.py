sales_data = [
    {"item": "A", "price": 100},
    {"item": "B", "price": 200},
    {"item": "C", "price": 300},
]

sales_data_2 = [
    {"item": "A", "price": 100},
    {"item": "B", "price": 0},
    {"item": "C", "price": 300},
]

def summarize_sales(data):
    try:
        total = 0
        count = 0

        for item in data:
            if item["price"] > 0:
                total += item["price"]
                count += 1
        
        avg = total / count if count > 0 else 0

        return {"total_amount": total, "average_price": avg, "item_count": count}
            

    except ZeroDivisionError:
        return "ZeroDivisionError"
    
    except Exception as e:
        return "その他のerror"
    
#正常系テスト
print(summarize_sales(sales_data))

#異常系テスト

print(summarize_sales(sales_data_2))