# # "price" が抜けているデータや、空のデータを入れたデータ
# broken_sales_data = [
#     {"item": "りんご", "price": 150, "category": "fruit"},
#     {"item": "不明な商品", "category": "fruit"}, # priceがない！
#     {"item": "バナナ", "price": 200, "category": "fruit"},
# ]

# # def get_category_total_safe(data, category_name):
# #     total = 0
# #     for row in data:
# #         if row.get("category") == category_name:
# #             # ここで price があるかチェックしてから足したい
# #             # ヒント：row.get("price", 0) を使うと、なければ 0 を返してくれます
# #             total += row.get("price", 0)
# #     return total

# # print(f"安全な集計結果: {get_category_total_safe(broken_sales_data, 'fruit')}")

# import pandas as pd

# df = pd.DataFrame(broken_sales_data)
# print(df)


# result = df[df["category"] == "fruit"]["price"].sum()
# print(result)


#例外処理（Exception Handling）

def safe_division():
    try:
        # ユーザーに入力を促す
        num_str = input("数字を入力してください: ")
        number = int(num_str) # ここで「あ」などを入れるとエラーが発生する
        
        result = 100 / number  # 0を入力すると「0除算エラー」が発生する
        print(f"100 ÷ {number} = {result}")
        
    except ValueError:
        # 数字以外が入力された時の処理
        print("エラー：数字以外が入力されました。数値を入れてください。")
        
    except ZeroDivisionError:
        # 0が入力された時の処理
        print("エラー：0で割ることはできません。")
        
    except Exception as e:
        # それ以外の想定外のエラー
        print(f"予期せぬエラーが発生しました: {e}")
    
    finally:
        # エラーが起きても起きなくても実行される（後片付けなど）
        print("処理を終了します。")

safe_division()