# DBSCAN 密度聚類重點整理

> **一句話：K-means 找中心；DBSCAN 找密度。**

## 1. DBSCAN 是什麼？

DBSCAN（Density-Based Spatial Clustering of Applications with
Noise）是一種**基於密度的分群演算法**。

核心概念：

``` text
資料點附近的人夠多？
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
高密度區域   可能是 Noise
   │
形成 Cluster
```

DBSCAN 將高密度區域視為群集，低密度區域則可能視為離群值。

------------------------------------------------------------------------

## 2. 機器學習分類

``` text
Machine Learning
│
├── Supervised Learning 監督式學習
│
└── Unsupervised Learning 非監督式學習
    │
    └── Clustering 分群
        ├── K-means
        ├── Hierarchical Clustering
        └── DBSCAN
```

DBSCAN 屬於：

-   **非監督式學習（Unsupervised Learning）**
-   **分群（Clustering）**
-   **密度式分群（Density-Based Clustering）**

------------------------------------------------------------------------

## 3. 兩個核心參數

### eps（ε）

代表**鄰域半徑**。

``` text
        eps
   ┌─────────┐
   │    ●    │
   │  ● X ●  │
   │    ●    │
   └─────────┘

X = 目前檢查的資料點
```

DBSCAN 會檢查：

> X 的 eps 範圍內有多少鄰居？

### min_samples

代表成為核心點所需要的**最少資料點數**。

``` text
min_samples = 4

        ●
    ●   X   ●
        ●

附近資料點數足夠
        ↓
   Core Point
```

------------------------------------------------------------------------

## 4. 三種資料點

### Core Point 核心點

``` text
eps 範圍內
鄰居數 >= min_samples
        ↓
    Core Point
```

圖解：

``` text
        ●
    ●   X   ●
        ●

X = Core Point
```

### Border Point 邊界點

自己的鄰居不足，但靠近 Core Point。

``` text
● ● ● ●
● ● ● X       Y
● ● ● ●

X = Core Point
Y = Border Point
```

### Noise Point 雜訊點

附近沒有足夠鄰居，也不靠近 Core Point。

``` text
● ● ● ●
 ● ● ●


                    X

X = Noise
```

在 scikit-learn DBSCAN 中：

``` python
label == -1
```

代表 Noise。

------------------------------------------------------------------------

## 5. DBSCAN 演算法流程

``` text
                Data
                  │
                  ▼
          選擇一個資料點
                  │
                  ▼
          搜尋 eps 鄰域
                  │
                  ▼
     鄰居數 >= min_samples ?
            │              │
           YES             NO
            │              │
            ▼              ▼
       Core Point     靠近 Core Point？
            │              │
            ▼         YES  │  NO
      建立 Cluster         │
            │          Border Point
            ▼              │
      擴張附近鄰居          ▼
            │             Noise
            ▼
     Density Reachable
            │
            ▼
         Cluster
```

### 密度擴張概念

``` text
A 靠近 B
    ↓
B 靠近 C
    ↓
C 靠近 D

A → B → C → D
        ↓
   同一個 Cluster
```

即使 A 與 D 很遠，也可能透過密度連接形成同一群。

------------------------------------------------------------------------

## 6. 為什麼可以找不規則形狀？

假設資料：

``` text
● ● ● ●
        ●
        ●
        ● ● ● ●
```

DBSCAN 不尋找中心，而是持續檢查附近是否有足夠密度：

``` text
●附近有人？
     ↓
●附近有人？
     ↓
●附近有人？
     ↓
持續擴張 Cluster
```

因此可以發現**任意形狀的 Cluster**。

------------------------------------------------------------------------

## 7. DBSCAN vs K-means

  特性       K-means        DBSCAN
  ---------- -------------- ------------------
  類型       非監督式       非監督式
  方法       中心式         密度式
  核心概念   Centroid       Density
  指定群數   需要 K         不需要
  主要參數   K              eps、min_samples
  群集形狀   偏凸狀／球狀   任意形狀
  Noise      不擅長         可識別
  Outlier    強制分群       可標記 Noise
  不同密度   視資料而定     容易有問題

``` text
K-means
資料 → 找中心 → 計算距離 → 分群

DBSCAN
資料 → 找高密度區域 → Core Point → 擴張 → Cluster
```

> **口訣：K-means 找中心；DBSCAN 找人群。**

------------------------------------------------------------------------

## 8. 實務應用

### 銀行異常交易偵測

``` text
交易資料
│
├── 交易金額
├── 交易時間
├── 交易頻率
├── 登入位置
└── 轉帳次數
        │
        ▼
      DBSCAN
        │
   ┌────┴────┐
   │         │
Cluster     Noise
   │         │
正常模式   異常候選
```

例如：

``` text
正常交易

● ● ● ●
 ● ● ●
● ● ● ●


異常交易

                ▲
```

特殊交易可能被標記為 Noise。

> 注意：**Noise 不等於詐欺，只代表異常候選。**

### 其他應用

-   客戶分群
-   ATM / GPS 地理熱點分析
-   異常交易偵測
-   網路入侵偵測
-   Outlier Detection
-   空間資料分析

------------------------------------------------------------------------

## 9. 優點

1.  **不需要預先指定 Cluster 數量**
2.  **可以發現任意形狀的群集**
3.  **可以識別 Noise / Outlier**
4.  **對離群值的處理比 K-means 自然**

``` text
K-means

Outlier
   ↓
強制加入某個 Cluster

DBSCAN

Outlier
   ↓
Noise (-1)
```

------------------------------------------------------------------------

## 10. 缺點

### eps 敏感

``` text
eps 太小
   ↓
大量資料成為 Noise
```

``` text
eps 太大
   ↓
不同 Cluster 可能連在一起
```

### 不適合密度差異大的資料

``` text
Cluster A

●●●●●●●
●●●●●●●

Cluster B

○       ○

    ○

        ○
```

同一組 eps 很難同時處理高密度與低密度 Cluster。

### 高維資料可能受維度詛咒影響

DBSCAN 依賴 Distance。

``` text
維度增加
   ↓
距離差異辨識能力下降
   ↓
DBSCAN 效果可能下降
```

### 通常需要資料標準化

``` text
Age      = 20 ~ 70
Income   = 30,000 ~ 5,000,000
```

Income 尺度可能主導距離，因此常先使用：

``` python
StandardScaler
```

流程：

``` text
Raw Data
   ↓
StandardScaler
   ↓
DBSCAN
```

------------------------------------------------------------------------

## 11. Python 簡單範例

模擬銀行交易資料：

``` python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# [交易金額, 每日交易次數]
X = np.array([
    [1000, 2],
    [1200, 3],
    [1100, 2],
    [1300, 3],
    [900, 2],

    [10000, 10],
    [11000, 11],
    [10500, 10],
    [12000, 12],

    [500000, 50]
])

# 資料標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 建立 DBSCAN
model = DBSCAN(
    eps=0.8,
    min_samples=2
)

# 執行分群
labels = model.fit_predict(X_scaled)

print(labels)

# 找出 Noise
for data, label in zip(X, labels):
    if label == -1:
        print("異常交易候選:", data)
```

可能結果：

``` text
[ 0  0  0  0  0
  1  1  1  1
 -1]
```

解讀：

``` text
0  → Cluster 0
1  → Cluster 1
-1 → Noise
```

完整流程：

``` text
交易資料
   ↓
StandardScaler
   ↓
DBSCAN
   ↓
產生 Cluster Label
   ↓
label == -1
   ↓
異常交易候選
```

------------------------------------------------------------------------

## 12. 考試重點速記

  考點           DBSCAN
  -------------- -------------------------------------------------------------
  全名           Density-Based Spatial Clustering of Applications with Noise
  類型           非監督式學習
  任務           Clustering
  核心           Density
  參數           eps、min_samples
  資料點         Core、Border、Noise
  Noise Label    -1
  指定 K         不需要
  Cluster 形狀   任意形狀
  強項           Noise / Outlier
  缺點           eps 敏感
  密度差異       處理較困難

## 一句話定義

> **DBSCAN 是一種基於密度的非監督式分群演算法，透過 eps 與 min_samples
> 判斷資料密度，從核心點向外擴張形成群集，並將離群資料標記為 Noise。**

## 最後心智模型

``` text
K-NN
 ↓
找鄰居
 ↓
分類 / 迴歸


K-means
 ↓
找中心
 ↓
分群


DBSCAN
 ↓
找密度
 ↓
分群 + Noise
```

> **K-NN：鄰居是誰？**\
> **K-means：中心在哪？**\
> **DBSCAN：附近夠不夠多人？**

------------------------------------------------------------------------

## 參考資料

-   scikit-learn DBSCAN API Documentation
-   scikit-learn Clustering User Guide
