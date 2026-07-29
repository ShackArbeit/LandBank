import numpy as np
import pandas as pd

def clean_customers(df):
    required = {'age', 'income', 'city'}
    if not required.issubset(df.columns):
         raise ValueError('缺少必要欄位') 
    
    result = df.copy()  # 👈 修正：複製整個 DataFrame，而非集合
    
    # 1. 補齊年齡缺失值（用中位數）
    result['age'] = result['age'].fillna(result['age'].median())
    
    # 2. 補齊城市缺失值（填入 UNKNOWN）
    result['city'] = result['city'].fillna('UNKNOWN')
    
    # 3. 刪除收入為空的整列資料
    result = result.dropna(subset=['income'])
    
    return result.reset_index(drop=True)  # 👈 修正：拼字 Truie -> True
data = {
    'age': [20.0, np.nan, 40.0, 30.0],     # 索引 1 缺失年齡（有效年齡中位數為 30）
    'income': [50000, 60000, np.nan, 70000], # 索引 2 缺失收入（應被刪除）
    'city': ['Taipei', 'Kaohsiung', 'Tainan', np.nan] # 索引 3 缺失城市（應補 UNKNOWN）
}

df_test = pd.DataFrame(data)
print("--- 原始測試資料 ---")
print(df_test)