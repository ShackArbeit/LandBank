# SVM 支援向量機（Support Vector Machine）

## 1. SVM 是什麼？

SVM（Support Vector Machine，支援向量機）是一種**監督式學習演算法**，主要用於：

- 分類（Classification）
- 迴歸（Regression，稱為 SVR）
- 異常偵測（One-Class SVM）

核心概念：

> 找出一條能將不同類別分開，且類別間隔（Margin）最大的最佳決策邊界。

---

## 2. 圖解原理

### 2.1 尋找分類邊界

假設有兩類資料：

```text
Y 軸
↑

│  🔵  🔵
│ 🔵 🔵
│
│          🔴
│       🔴 🔴
│
└────────────────→ X 軸
```

可以畫出很多條分隔線，但 SVM 不只要求「分得開」，而是要找：

> 距離兩邊最近資料點都最遠的那條線。

---

### 2.2 Hyperplane：超平面

SVM 的決策邊界稱為 **Hyperplane（超平面）**。

| 特徵維度 | 決策邊界 |
|---|---|
| 2 維 | 一條線 |
| 3 維 | 一個平面 |
| N 維 | 超平面 |

數學形式：

```text
wᵀx + b = 0
```

分類方式：

```text
wᵀx + b > 0  →  類別 +1
wᵀx + b < 0  →  類別 -1
```

---

### 2.3 Margin：最大間隔

SVM 希望決策邊界與兩側最近資料點之間的距離最大。

```text
🔵 🔵
   🔵

----------------  Margin 邊界
        ↑
        │
========│========  Hyperplane
        │
        ↓
----------------  Margin 邊界

   🔴
🔴 🔴
```

可以把它想像成：

```text
🔵 類別       高速公路       🔴 類別

🔵 🔵       |         |      🔴 🔴
            | Margin  |
            |         |
```

SVM 的目標就是讓這條「高速公路」越寬越好。

---

### 2.4 Support Vector：支援向量

距離決策邊界最近的資料點稱為：

> Support Vectors（支援向量）

```text
🔵 🔵
    🔵  ← Support Vector

---------------- Margin

======== Hyperplane ========

---------------- Margin

    🔴  ← Support Vector
🔴 🔴
```

這些點真正決定了決策邊界的位置。

即使移動遠處的資料點，決策邊界可能不變；但移動 Support Vector，整條邊界可能改變。

---

## 3. Hard Margin 與 Soft Margin

### Hard Margin

要求所有資料都完全正確分類：

```text
🔵 🔵 🔵

────────────

🔴 🔴 🔴
```

適合完全線性可分的資料，但對離群值非常敏感。

---

### Soft Margin

允許少量資料分類錯誤，以提升泛化能力：

```text
🔵 🔵 🔵

       🔴  ← 允許少量分錯

────────────

🔴 🔴 🔴
```

實務上多數情況使用 Soft Margin。

---

## 4. C 參數

`C` 控制錯誤懲罰程度。

### C 很大

```text
錯誤懲罰大
→ 模型盡量不分錯
→ Margin 變小
→ 模型較複雜
→ 容易 Overfitting
```

### C 很小

```text
容許部分錯誤
→ Margin 變大
→ 模型較簡單
→ 泛化能力可能較好
```

| C | 容錯 | Margin | 風險 |
|---|---|---|---|
| 大 | 低 | 小 | Overfitting |
| 小 | 高 | 大 | Underfitting |

---

## 5. Kernel Trick：核技巧

如果資料無法用直線分開：

```text
      🔵 🔵
   🔵       🔵

      🔴 🔴

   🔵       🔵
      🔵 🔵
```

SVM 可以透過 Kernel 將資料映射到更高維空間，使資料變得線性可分。

```text
原始低維空間
      ↓
Kernel 映射
      ↓
高維空間
      ↓
使用超平面分類
```

常見 Kernel：

| Kernel | 適用情境 |
|---|---|
| Linear | 線性資料、文字分類、高維稀疏資料 |
| Polynomial | 多項式關係 |
| RBF | 複雜非線性資料 |
| Sigmoid | 類似神經元的轉換 |

---

## 6. Gamma 參數

`Gamma` 主要用於 RBF Kernel，控制單一資料點的影響範圍。

### Gamma 大

```text
影響範圍小
→ 重視局部資料
→ 邊界較複雜
→ 容易 Overfitting
```

### Gamma 小

```text
影響範圍大
→ 邊界較平滑
→ 可能 Underfitting
```

| Gamma | 影響範圍 | 決策邊界 | 風險 |
|---|---|---|---|
| 大 | 小 | 複雜 | Overfitting |
| 小 | 大 | 平滑 | Underfitting |

記憶方式：

```text
C      → 控制分類錯誤懲罰
Gamma  → 控制單一資料點影響範圍
```

---

## 7. SVM 屬於哪一種機器學習？

```text
Machine Learning
│
├── Supervised Learning
│   ├── Classification
│   │   └── SVC
│   └── Regression
│       └── SVR
│
└── Outlier Detection
    └── One-Class SVM
```

SVM 主要屬於：

> 監督式學習（Supervised Learning）

最常見用途是：

> 分類（Classification）

---

## 8. 實務應用

### 銀行信用風險

```text
客戶資料
├── 收入
├── 負債比
├── 信用分數
└── 還款紀錄
        ↓
       SVM
        ↓
低風險 / 高風險
```

### 異常交易偵測

```text
交易金額、時間、地點、裝置、頻率
                  ↓
            One-Class SVM
                  ↓
              正常 / 可疑
```

### 文字分類

```text
Email 文字
   ↓
TF-IDF
   ↓
Linear SVM
   ↓
垃圾郵件 / 正常郵件
```

其他常見應用：

- 手寫數字辨識
- 影像分類
- 腫瘤良性／惡性判斷
- 文件分類
- 生物資訊分析

---

## 9. 優缺點

### 優點

- 適合高維資料
- 在小型與中型資料集表現良好
- 可透過 Kernel 處理非線性問題
- Maximum Margin 通常有不錯的泛化能力
- 模型主要由 Support Vectors 決定

### 缺點

- 大型資料集訓練速度慢
- 對 `C`、`Gamma`、Kernel 選擇敏感
- 模型不容易解釋
- 通常需要做特徵標準化
- Kernel SVM 在大量資料下成本高

---

## 10. 與其他演算法比較

| 演算法 | 核心概念 |
|---|---|
| Logistic Regression | 預測機率 |
| K-NN | 尋找最近鄰居 |
| Decision Tree | 建立判斷規則 |
| Random Forest | 多棵樹投票 |
| SVM | 尋找最大間隔邊界 |

快速記憶：

```text
Logistic Regression → 找機率
K-NN                → 找鄰居
Decision Tree       → 找規則
Random Forest       → 多數決
SVM                 → 找最寬的分界線
```

---

## 11. Python 簡單範例

目標：根據「月收入」與「負債比」判斷客戶信用風險。

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# X = [月收入, 負債比]
X = np.array([
    [30000, 70],
    [35000, 65],
    [40000, 60],
    [45000, 55],
    [60000, 30],
    [70000, 25],
    [80000, 20],
    [90000, 15]
])

# 0 = 高風險，1 = 低風險
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# 建立 Pipeline：
# 1. StandardScaler 標準化
# 2. Linear SVM 分類
model = make_pipeline(
    StandardScaler(),
    SVC(kernel="linear", C=1)
)

# 訓練模型
model.fit(X, y)

# 新客戶：[月收入 65000，負債比 35%]
new_customer = np.array([[65000, 35]])

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("低風險客戶")
else:
    print("高風險客戶")
```

預期輸出：

```text
低風險客戶
```

---

## 12. 為什麼要標準化？

原始特徵尺度差異很大：

```text
月收入：30000 ～ 90000
負債比：15 ～ 70
```

如果不標準化，收入可能因數值較大而主導模型。

`StandardScaler` 會將特徵轉換成大致：

```text
平均值 = 0
標準差 = 1
```

因此 SVM、K-NN 等與距離或幾何關係有關的模型，通常都應先進行特徵標準化。

---

## 13. 考試必背重點

| 關鍵字 | 重點 |
|---|---|
| 類型 | 監督式學習 |
| 主要用途 | 分類 |
| 核心目標 | Maximum Margin |
| 決策邊界 | Hyperplane |
| 關鍵資料點 | Support Vectors |
| 非線性處理 | Kernel Trick |
| C | 錯誤懲罰程度 |
| Gamma | 單一資料點影響範圍 |
| 前處理 | 通常需要標準化 |

一句話總結：

> SVM 透過 Support Vectors 找出 Maximum Margin Hyperplane；若資料非線性，可利用 Kernel Trick 映射至高維空間。C 控制錯誤懲罰，Gamma 控制資料點的影響範圍。
