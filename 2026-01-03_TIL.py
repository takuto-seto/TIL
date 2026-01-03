def two_sum(nums, target):
    # メモ用の辞書を用意
    memo = {}
    
    for i, num in enumerate(nums):
        # 1. 相方（complement）を計算する
        complement = target - num
        
        # 2. もし相方がすでに memo に入っていたら？
        if complement in memo:
            # その相方のインデックスと、今のインデックス i をリストで返す
            return [memo[complement], i]
            pass
        
        # 3. まだ相方が見つかっていなければ、今の数字をメモに保存する
        # memo[数字] = インデックス
        memo[num] = i
        pass

# テスト
print(two_sum([2, 7, 11, 15], 9))  # [0, 1] が出れば正解！
print(two_sum([3, 2, 4], 6))       # [1, 2] が出れば正解！