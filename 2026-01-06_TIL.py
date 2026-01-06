import pandas as pd

# 1. 外部から届いた「少し壊れた」生データ
raw_data = [
    {"item": "りんご", "price": 150, "category": "fruit"},
    {"item": "バナナ", "price": "200", "category": "fruit"}, # 文字列で入っている
    {"item": "不明な商品", "price": None, "category": "fruit"}, # None（欠損）
    {"item": "テレビ", "price": 50000, "category": "electronics"},
]

def generate_sales_report(data, target_category):
    try:
        # ステップ1: データをDataFrameに変換
        df = pd.DataFrame(data)
        
        # ステップ2: データクレンジング
        # price列を数値型に変換し、変換できないものは NaN にする
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        # NaN（欠損値）を 0 で埋める
        df["price"] = df["price"].fillna(0)
        
        # ステップ3: フィルタリングと計算
        # target_category に一致する行だけを抽出し、合計を出す
        ### ここを実装してみてください
        category_df = df[df["category"] == target_category]
        total = category_df["price"].sum()
        
        return {
            "category": target_category,
            "total_sales": total,
            "item_count": len(category_df)
        }
        
    except Exception as e:
        return f"レポート作成中に予期せぬエラーが発生しました: {e}"

# --- テスト実行 ---
# 正常な実行
print(f"フルーツのレポート: {generate_sales_report(raw_data, 'fruit')}")

# 異常な入力（リストではなく文字列を渡してみる）
print(f"エラー発生時の挙動: {generate_sales_report('壊れたデータ', 'fruit')}")