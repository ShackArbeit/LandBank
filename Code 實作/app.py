def deduplicate_with_log(items):
    seen = set()  # 正確建立空集合
    result = []
    
    print(f"👉 開始處理輸入清單: {items}")
    print("-" * 50)
    
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
            print(f"  [新元素] 放入 '{item}' -> 當前 seen 內容: {seen}")
        else:
            print(f"  [重複了] 偵測到 '{item}' 已存在於 seen 中，跳過不處理！")
            
    print("-" * 50)
    print(f"最終回傳結果 (result): {result}")
    print(f"最終集合內容 (seen)  : {seen}\n")
    return result

# --- 執行測試 1：簡單數字 ---
deduplicate_with_log([1, 2, 2, 3, 1])

# --- 執行測試 2：簡單文字 ---
deduplicate_with_log(["A", "B", "A", "C"])