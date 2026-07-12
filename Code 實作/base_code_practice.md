# 2026 土地銀行 AI 應用人員：Python 程式設計基礎題


## 一、命題依據與土地銀行公開案例

> **重要說明：** 以下題目是依 2026 年甄試簡章、土地銀行公開案例與金融 AI 治理要求所設計的模擬題，
> 並非官方題庫、考古題或洩題。題目中的門檻、權重與資料均為教學用途。

### 1. 官方甄試方向

臺灣土地銀行 115 年新進人員甄試簡章將「AI 應用人員」專業科目列為 80%，範圍包含：

- AI 基礎與概念
- 機器學習
- 自然語言處理（NLP）
- 數據分析
- 程式設計（以 Java 或 Python 解答）
- 題型同時包含選擇題與非選擇題

簡章的口試加分條件同時明列：生成式 AI / Copilot、ML/DL 建模與評估、資料清洗與特徵工程、
洗錢防制／詐欺偵測、Python、AI 函式庫與 SQL。這代表「程式設計」不宜只準備語法，
而要能把 Python 用在資料、模型、風控與系統實作。

### 2. 土地銀行近年公開的 AI／數位應用

| 代碼 | 公開案例 | 可轉化的程式命題 |
|---|---|---|
| LB-1 | 智能客服與金融專業語庫；2024 年造訪 411,290 人次 | 文字正規化、意圖分類、FAQ 檢索、Top-K、信心門檻、敏感資料遮罩 |
| LB-2 | 2024 年已導入 54 項 RPA 流程，涵蓋報表、統計、稅務與人事 | CSV/Excel、對帳、冪等、重試、錯誤隔離、稽核日誌 |
| LB-3 | 大數據分析、Tableau 訓練；以爬網技術擷取營業稅籍資料 | pandas、資料清洗、分組聚合、時間序列、網路資料驗證 |
| LB-4 | 加入鷹眼識詐聯盟並使用 AI 模型；曾公開近一年阻詐 178 件、避免損失逾 1.6 億元 | 異常偵測、風險分數、類別不平衡、Precision/Recall、告警系統 |
| LB-5 | CRA 法令遵循管理系統，以 AI 比對外部法令與內部規章 | 文件分塊、TF-IDF、相似度、版本差異、人工覆核 |
| LB-6 | 2025 年與臺灣高等檢察署簽署可疑交易分析機制 MOU，以異常因子與參數強化識詐模型 | 特徵工程、可疑金流圖、模型版本、資料治理 |
| LB-7 | 2026 年部分 ATM 試辦 AI 臉部遮蔽提醒模組 | 模型輸出決策、閾值、重試、降級、隱私與公平性 |
| GOV-1 | 金管會「金融業運用人工智慧（AI）指引」 | 治理問責、公平性、隱私、穩健安全、透明可解釋、永續 |


## 二、程式設計重點架構

以下比重是**備考建議，不是官方配分**。在每天只有一小時的前提下，建議採「先能手寫、再能解釋、最後銀行化」：

| 優先級 | 模組 | 必會內容 | 建議投入 |
|---|---|---|---:|
| P0 | Python 基礎 | 型別、條件、迴圈、函式、例外、檔案、模組 | 20% |
| P0 | 核心資料結構 | list、tuple、dict、set、Counter、deque、heap | 18% |
| P0 | 演算法與複雜度 | 搜尋、排序、雙指標、滑動視窗、前綴和、BFS/DFS | 20% |
| P0 | 資料處理 | CSV、JSON、regex、datetime、NumPy、pandas、SQL | 22% |
| P1 | 安全程式設計 | 驗證、參數化 SQL、雜湊、遮罩、權限、日誌 | 8% |
| P1 | 軟體品質 | OOP、dataclass、單元測試、可讀性、邊界值 | 7% |
| P1 | AI 串接基礎 | 特徵矩陣、模型輸入、推論、指標、Pipeline | 5% |

### 非選擇題的標準作答骨架

1. **確認輸入／輸出與邊界**：空值、負數、重複值、時間順序、資料型別。
2. **說明資料結構**：為何選 dict、set、deque、heap 或 DataFrame。
3. **先寫主流程，再補驗證**：讓閱卷者看得懂核心邏輯。
4. **寫時間與空間複雜度**：至少能區分 O(1)、O(n)、O(n log n)、O(n²)。
5. **補金融情境注意事項**：Decimal、隱私、誤報、稽核、人工覆核。
6. **列測試案例**：正常值、邊界值、錯誤值、極端值。

### VS Code 練習方式

- 建議 Python 3.11 以上。
- 基礎題優先只看題目檔，限時 10～20 分鐘手寫。
- 完成後再開答案檔，比對：正確性、複雜度、邊界、可讀性。
- 需要套件的題目可建立虛擬環境並安裝：

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install numpy pandas scipy scikit-learn fastapi uvicorn joblib pyarrow
```



## 三、題目總覽

共 **65 題**。建議先自行作答，再查閱對應答案檔。

- [ ] 001. 型別轉換與交易金額驗證（入門）
- [ ] 002. 條件判斷：交易金額分級（入門）
- [ ] 003. 複利計算（入門）
- [ ] 004. 閏年判斷（入門）
- [ ] 005. FizzBuzz 變形：規則標記（入門）
- [ ] 006. 一到 n 的總和（入門）
- [ ] 007. 九九乘法表矩陣（入門）
- [ ] 008. 質數判斷（入門）
- [ ] 009. 最大公因數與最小公倍數（入門）
- [ ] 010. 反轉字串與回文判斷（入門）
- [ ] 011. 字元頻率統計（入門）
- [ ] 012. 空白正規化（入門）
- [ ] 013. 帳號遮罩（入門）
- [ ] 014. 密碼規則驗證（入門）
- [ ] 015. 保留順序去除重複值（入門）
- [ ] 016. 第二大不重複值（入門）
- [ ] 017. Two Sum（初階）
- [ ] 018. 串列右旋（初階）
- [ ] 019. 合併兩個已排序串列（初階）
- [ ] 020. Top-K 高頻項目（初階）
- [ ] 021. 集合交集與差集（初階）
- [ ] 022. 依帳戶彙總交易（初階）
- [ ] 023. 展平巢狀字典（初階）
- [ ] 024. 串列生成式篩選（初階）
- [ ] 025. 可變預設參數陷阱（初階）
- [ ] 026. *args 與 **kwargs 費用計算器（初階）
- [ ] 027. 多欄位排序（初階）
- [ ] 028. 費波那契數列與記憶化（初階）
- [ ] 029. 安全解析交易列（初階）
- [ ] 030. 使用 context manager 讀檔（初階）
- [ ] 031. BankAccount 類別（初階）
- [ ] 032. 使用 deque 實作佇列（初階）
- [ ] 033. 括號配對（初階）
- [ ] 034. 二分搜尋（初階）
- [ ] 035. 線性搜尋與比較（初階）
- [ ] 036. 氣泡排序（初階）
- [ ] 037. 插入排序（初階）
- [ ] 038. 合併排序（中階）
- [ ] 039. 快速排序（中階）
- [ ] 040. 廣度優先搜尋 BFS（中階）
- [ ] 041. 深度優先搜尋 DFS（中階）
- [ ] 042. 無權重最短路徑（中階）
- [ ] 043. 以 heap 取得前 K 大值（中階）
- [ ] 044. 固定長度滑動視窗最大總和（中階）
- [ ] 045. 雙指標移除重複值（中階）
- [ ] 046. 前綴和區間查詢（中階）
- [ ] 047. 和為 K 的子陣列數量（中階）
- [ ] 048. CSV 交易彙總（中階）
- [ ] 049. JSON Schema 基礎驗證（中階）
- [ ] 050. 正規表示式驗證 Email（中階）
- [ ] 051. 計算工作日（中階）
- [ ] 052. NumPy Min-Max 正規化（中階）
- [ ] 053. NumPy 矩陣乘法與 shape（中階）
- [ ] 054. pandas 缺失值處理（中階）
- [ ] 055. pandas 月交易彙總（中階）
- [ ] 056. pandas 合併客戶與交易（中階）
- [ ] 057. pandas 樞紐分析表（中階）
- [ ] 058. SQLite 參數化查詢（中階）
- [ ] 059. Generator 分批處理（中階）
- [ ] 060. Decorator 記錄執行時間（中階）
- [ ] 061. 單元測試：parse_amount（中階）
- [ ] 062. 密碼安全雜湊（中階）
- [ ] 063. 輸入白名單與 SQL 注入防護（中階）
- [ ] 064. Big-O 優化：重複會員查找（中階）
- [ ] 065. dataclass 交易資料模型（中階）


---

## 四、練習題


### 001. 型別轉換與交易金額驗證


- **難度：** 入門
- **主題：** 型別、例外處理、Decimal


#### 題目

實作 `parse_amount(value)`，接受整數、浮點數或字串，回傳 `Decimal` 金額並四捨五入至小數第 2 位。
空字串、非數字、NaN、Infinity 或負數都要拋出 `ValueError`。金融金額不得直接依賴二進位浮點數累加。


#### 建議函式／介面

```python
def parse_amount(value) -> Decimal:
```


#### 範例

parse_amount("1234.567") -> Decimal("1234.57")
parse_amount(-1) -> ValueError


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 002. 條件判斷：交易金額分級


- **難度：** 入門
- **主題：** if/elif/else、邊界條件


#### 題目

實作 `risk_band(amount)`：金額小於 10,000 回傳 `"LOW"`；10,000 至未滿 100,000 回傳 `"MEDIUM"`；
100,000 以上回傳 `"HIGH"`。負數須拋出 `ValueError`。


#### 建議函式／介面

```python
def risk_band(amount: float) -> str:
```


#### 範例

risk_band(9999) -> "LOW"
risk_band(10000) -> "MEDIUM"
risk_band(100000) -> "HIGH"


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 003. 複利計算


- **難度：** 入門
- **主題：** 運算子、函式、次方


#### 題目

實作 `compound(principal, annual_rate, years, times_per_year=12)`，
計算複利終值 `P(1+r/n)^(nt)`，結果四捨五入至小數第 2 位。輸入不得為負，複利次數必須大於 0。


#### 建議函式／介面

```python
def compound(principal: float, annual_rate: float, years: int, times_per_year: int = 12) -> float:
```


#### 範例

compound(100000, 0.02, 1, 12) -> 約 102018.44


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 004. 閏年判斷


- **難度：** 入門
- **主題：** 布林邏輯、整除


#### 題目

實作 `is_leap_year(year)`。能被 400 整除為閏年；能被 100 整除但不能被 400 整除不是閏年；
其餘能被 4 整除者為閏年。


#### 建議函式／介面

```python
def is_leap_year(year: int) -> bool:
```


#### 範例

is_leap_year(2000) -> True
is_leap_year(1900) -> False
is_leap_year(2024) -> True


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 005. FizzBuzz 變形：規則標記


- **難度：** 入門
- **主題：** 迴圈、模數、串列


#### 題目

對 1 到 n 產生標記：3 的倍數為 `"A"`，5 的倍數為 `"B"`，同時為兩者倍數為 `"AB"`，
其餘轉成字串。回傳字串串列。


#### 建議函式／介面

```python
def rule_tags(n: int) -> list[str]:
```


#### 範例

rule_tags(5) -> ["1", "2", "A", "4", "B"]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 006. 一到 n 的總和


- **難度：** 入門
- **主題：** 迴圈、公式、複雜度


#### 題目

分別實作 `sum_loop(n)` 與 `sum_formula(n)`，計算 1 到 n 的總和，並比較時間複雜度。
n 小於 0 時拋出 `ValueError`。


#### 建議函式／介面

```python
def sum_loop(n: int) -> int:
def sum_formula(n: int) -> int:
```


#### 範例

sum_loop(100) == sum_formula(100) == 5050


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 007. 九九乘法表矩陣


- **難度：** 入門
- **主題：** 巢狀迴圈、二維串列


#### 題目

實作 `multiplication_table(n)`，回傳 n×n 二維串列，其中第 i 列第 j 欄為 `(i+1)*(j+1)`。
n 必須大於 0。


#### 建議函式／介面

```python
def multiplication_table(n: int) -> list[list[int]]:
```


#### 範例

multiplication_table(3) -> [[1,2,3],[2,4,6],[3,6,9]]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 008. 質數判斷


- **難度：** 入門
- **主題：** 迴圈、平方根優化


#### 題目

實作 `is_prime(n)`。只需檢查因數到平方根，並正確處理 0、1、2 與負數。


#### 建議函式／介面

```python
def is_prime(n: int) -> bool:
```


#### 範例

is_prime(2) -> True
is_prime(49) -> False


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 009. 最大公因數與最小公倍數


- **難度：** 入門
- **主題：** Euclidean algorithm


#### 題目

實作 `gcd(a,b)` 與 `lcm(a,b)`。允許負數輸入；gcd 回傳非負數。若任一數為 0，lcm 回傳 0。


#### 建議函式／介面

```python
def gcd(a: int, b: int) -> int:
def lcm(a: int, b: int) -> int:
```


#### 範例

gcd(48, 18) -> 6
lcm(6, 8) -> 24


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 010. 反轉字串與回文判斷


- **難度：** 入門
- **主題：** 切片、字串正規化


#### 題目

實作 `is_palindrome(text)`，忽略大小寫與非英數字元，判斷是否為回文。


#### 建議函式／介面

```python
def is_palindrome(text: str) -> bool:
```


#### 範例

is_palindrome("A man, a plan, a canal: Panama") -> True


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 011. 字元頻率統計


- **難度：** 入門
- **主題：** dict、Counter


#### 題目

實作 `char_frequency(text)`，忽略空白並不分大小寫，回傳每個字元出現次數。


#### 建議函式／介面

```python
def char_frequency(text: str) -> dict[str, int]:
```


#### 範例

char_frequency("Aa b") -> {"a": 2, "b": 1}


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 012. 空白正規化


- **難度：** 入門
- **主題：** split、join


#### 題目

實作 `normalize_spaces(text)`，把連續空白（空格、Tab、換行）縮成單一空格，並移除頭尾空白。


#### 建議函式／介面

```python
def normalize_spaces(text: str) -> str:
```


#### 範例

normalize_spaces("  AI\tbank\n test ") -> "AI bank test"


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 013. 帳號遮罩


- **難度：** 入門
- **主題：** 字串切片、資料隱私


#### 題目

實作 `mask_account(account, visible=4)`：只保留末 visible 碼，其餘以 `*` 取代。
若 visible 為負數拋出錯誤；若帳號長度不超過 visible，全部回傳。


#### 建議函式／介面

```python
def mask_account(account: str, visible: int = 4) -> str:
```


#### 範例

mask_account("1234567890") -> "******7890"


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 014. 密碼規則驗證


- **難度：** 入門
- **主題：** 字串方法、all/any


#### 題目

實作 `validate_password(password)`，要求至少 10 碼，且至少包含一個大寫字母、小寫字母、數字及特殊字元。
回傳 `(bool, list[str])`，第二項列出未通過規則。


#### 建議函式／介面

```python
def validate_password(password: str) -> tuple[bool, list[str]]:
```


#### 範例

validate_password("Abc123!xyz") -> (True, [])


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 015. 保留順序去除重複值


- **難度：** 入門
- **主題：** list、set


#### 題目

實作 `deduplicate(items)`，移除重複元素但保留第一次出現的順序。假設元素可雜湊。


#### 建議函式／介面

```python
def deduplicate(items: list) -> list:
```


#### 範例

deduplicate([3,1,3,2,1]) -> [3,1,2]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 016. 第二大不重複值


- **難度：** 入門
- **主題：** 單次掃描、邊界


#### 題目

實作 `second_largest(numbers)`，回傳第二大的「不重複」值。若不足兩個不同值，拋出 `ValueError`。
不得直接排序整個串列。


#### 建議函式／介面

```python
def second_largest(numbers: list[float]) -> float:
```


#### 範例

second_largest([5,1,5,3]) -> 3


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 017. Two Sum


- **難度：** 初階
- **主題：** 雜湊表、索引


#### 題目

給定整數串列與 target，找出兩個不同索引，使其數值總和等於 target。回傳索引 tuple；
若不存在回傳 `None`。只需回傳第一組。


#### 建議函式／介面

```python
def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
```


#### 範例

two_sum([2,7,11,15], 9) -> (0,1)


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 018. 串列右旋


- **難度：** 初階
- **主題：** 切片、模數


#### 題目

實作 `rotate_right(items, k)`，將串列向右旋轉 k 格；k 可大於串列長度，也可為負數。
不得修改原串列。


#### 建議函式／介面

```python
def rotate_right(items: list, k: int) -> list:
```


#### 範例

rotate_right([1,2,3,4,5], 2) -> [4,5,1,2,3]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 019. 合併兩個已排序串列


- **難度：** 初階
- **主題：** 雙指標、排序


#### 題目

實作 `merge_sorted(a,b)`，在 O(n+m) 時間內合併兩個升冪串列，不得呼叫 `sorted()`。


#### 建議函式／介面

```python
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
```


#### 範例

merge_sorted([1,3,7],[2,3,8]) -> [1,2,3,3,7,8]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 020. Top-K 高頻項目


- **難度：** 初階
- **主題：** Counter、heap


#### 題目

實作 `top_k_frequent(items,k)`，回傳出現次數最高的 k 個項目與次數，依次數遞減、項目字串遞增排序。


#### 建議函式／介面

```python
def top_k_frequent(items: list[str], k: int) -> list[tuple[str, int]]:
```


#### 範例

top_k_frequent(["a","b","a","c","b","a"],2) -> [("a",3),("b",2)]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 021. 集合交集與差集


- **難度：** 初階
- **主題：** set、集合運算


#### 題目

給定兩份客戶 ID，回傳 `(兩者皆有, 只在A, 只在B)` 三個升冪串列。


#### 建議函式／介面

```python
def compare_customers(a: list[int], b: list[int]) -> tuple[list[int], list[int], list[int]]:
```


#### 範例

compare_customers([1,2,3],[2,3,4]) -> ([2,3],[1],[4])


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 022. 依帳戶彙總交易


- **難度：** 初階
- **主題：** dict、defaultdict


#### 題目

輸入為 `(account, amount)` tuple 串列，回傳每個帳戶的交易總額。空帳戶字串視為錯誤。


#### 建議函式／介面

```python
def aggregate_by_account(records: list[tuple[str, float]]) -> dict[str, float]:
```


#### 範例

aggregate_by_account([("A",10),("B",5),("A",3)]) -> {"A":13,"B":5}


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 023. 展平巢狀字典


- **難度：** 初階
- **主題：** 遞迴、dict


#### 題目

實作 `flatten_dict(data, sep=".")`，把任意深度的巢狀字典展平成單層鍵。
例如 `{"a":{"b":1}}` 變成 `{"a.b":1}`。空字典保留為值。


#### 建議函式／介面

```python
def flatten_dict(data: dict, sep: str = ".") -> dict:
```


#### 範例

flatten_dict({"customer":{"id":7,"name":"Lin"}})
-> {"customer.id":7,"customer.name":"Lin"}


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 024. 串列生成式篩選


- **難度：** 初階
- **主題：** comprehension、條件


#### 題目

給定交易金額串列，回傳所有大於等於 threshold 的正數平方，並保持原順序。
負數與 0 一律忽略。


#### 建議函式／介面

```python
def filtered_squares(amounts: list[int], threshold: int) -> list[int]:
```


#### 範例

filtered_squares([-2,0,3,5],4) -> [25]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 025. 可變預設參數陷阱


- **難度：** 初階
- **主題：** 函式、預設參數、None sentinel


#### 題目

修正下列函式，使每次呼叫不會共用同一個 list：
`def add_alert(alert, alerts=[]): alerts.append(alert); return alerts`


#### 建議函式／介面

```python
def add_alert(alert: str, alerts: list[str] | None = None) -> list[str]:
```


#### 範例

add_alert("A") -> ["A"]
add_alert("B") -> ["B"]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 026. *args 與 **kwargs 費用計算器


- **難度：** 初階
- **主題：** 可變參數、參數解包


#### 題目

實作 `total_fee(*fees, discount=0, **taxes)`：先加總 fees，再乘上 `(1-discount)`，
最後加上 taxes 的所有值。discount 必須介於 0 與 1。


#### 建議函式／介面

```python
def total_fee(*fees: float, discount: float = 0, **taxes: float) -> float:
```


#### 範例

total_fee(100,50,discount=0.1,vat=5) -> 140.0


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 027. 多欄位排序


- **難度：** 初階
- **主題：** sorted、lambda、穩定排序


#### 題目

交易紀錄為 dict，含 `risk`、`amount`、`id`。依 risk 由高到低、amount 由高到低、id 由小到大排序，
且不得修改原串列。


#### 建議函式／介面

```python
def sort_transactions(records: list[dict]) -> list[dict]:
```


#### 範例

輸入 risk 3/2/3 時，risk=3 先；同 risk 時 amount 較大者先。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 028. 費波那契數列與記憶化


- **難度：** 初階
- **主題：** 遞迴、memoization、迭代


#### 題目

實作 `fibonacci(n)` 回傳第 n 個費波那契數，定義 F0=0、F1=1。n 不可為負。
請避免指數時間的樸素遞迴。


#### 建議函式／介面

```python
def fibonacci(n: int) -> int:
```


#### 範例

fibonacci(10) -> 55


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 029. 安全解析交易列


- **難度：** 初階
- **主題：** 例外處理、錯誤收集


#### 題目

輸入多行 `"account,amount"` 字串。實作 `parse_rows(lines)`，回傳 `(valid_records, errors)`。
錯誤不能中止整批處理；errors 需包含 1-based 行號與原因。


#### 建議函式／介面

```python
def parse_rows(lines: list[str]) -> tuple[list[tuple[str, float]], list[str]]:
```


#### 範例

["A,10.5","bad","B,x"] -> ([("A",10.5)], ["第2行：欄位數錯誤","第3行：金額錯誤"])


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 030. 使用 context manager 讀檔


- **難度：** 初階
- **主題：** with、檔案 I/O


#### 題目

實作 `count_nonempty_lines(path)`，以 UTF-8 讀取文字檔並計算非空白行數。必須確保發生例外時檔案仍會關閉。


#### 建議函式／介面

```python
def count_nonempty_lines(path: str) -> int:
```


#### 範例

檔案內容三行，其中一行空白 -> 2


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 031. BankAccount 類別


- **難度：** 初階
- **主題：** OOP、封裝、例外


#### 題目

建立 `BankAccount` 類別，具有唯讀 account_id、balance 屬性，以及 deposit、withdraw 方法。
存提款必須大於 0；提款不得超過餘額。


#### 建議函式／介面

```python
class BankAccount:
```


#### 範例

acc = BankAccount("A001", 100)
acc.deposit(50)
acc.withdraw(20)
acc.balance -> 130


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 032. 使用 deque 實作佇列


- **難度：** 初階
- **主題：** queue、deque


#### 題目

實作 `process_queue(items)`：依輸入順序處理元素並回傳處理順序。必須使用適合從左端移除的資料結構。


#### 建議函式／介面

```python
def process_queue(items: list[str]) -> list[str]:
```


#### 範例

process_queue(["A","B","C"]) -> ["A","B","C"]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 033. 括號配對


- **難度：** 初階
- **主題：** stack、dict


#### 題目

實作 `is_balanced(expression)`，檢查 `()[]{}` 是否正確巢狀配對。其他字元忽略。


#### 建議函式／介面

```python
def is_balanced(expression: str) -> bool:
```


#### 範例

is_balanced("a*(b+[c])") -> True
is_balanced("([)]") -> False


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 034. 二分搜尋


- **難度：** 初階
- **主題：** binary search、邊界


#### 題目

在升冪串列中尋找 target，回傳任一匹配索引，不存在回傳 -1。請用迭代方式實作。


#### 建議函式／介面

```python
def binary_search(numbers: list[int], target: int) -> int:
```


#### 範例

binary_search([1,3,5,7],5) -> 2


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 035. 線性搜尋與比較


- **難度：** 初階
- **主題：** linear search、複雜度


#### 題目

實作 `linear_search(items,target)`，回傳第一個匹配索引，不存在回傳 -1。
說明它何時比二分搜尋更適合。


#### 建議函式／介面

```python
def linear_search(items: list, target) -> int:
```


#### 範例

linear_search(["A","B","A"],"A") -> 0


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 036. 氣泡排序


- **難度：** 初階
- **主題：** sorting、交換、提前停止


#### 題目

實作升冪氣泡排序，回傳新串列。若某一輪沒有交換，應提前停止。


#### 建議函式／介面

```python
def bubble_sort(items: list[int]) -> list[int]:
```


#### 範例

bubble_sort([5,1,4,2]) -> [1,2,4,5]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 037. 插入排序


- **難度：** 初階
- **主題：** sorting、局部有序


#### 題目

實作升冪插入排序，回傳新串列。說明它在近乎排序資料上的優點。


#### 建議函式／介面

```python
def insertion_sort(items: list[int]) -> list[int]:
```


#### 範例

insertion_sort([4,2,3,1]) -> [1,2,3,4]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 038. 合併排序


- **難度：** 中階
- **主題：** divide and conquer、遞迴


#### 題目

實作 `merge_sort(items)`，回傳升冪新串列。不得使用內建排序。


#### 建議函式／介面

```python
def merge_sort(items: list[int]) -> list[int]:
```


#### 範例

merge_sort([5,2,4,1,3]) -> [1,2,3,4,5]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 039. 快速排序


- **難度：** 中階
- **主題：** partition、遞迴


#### 題目

實作簡潔版 `quick_sort(items)`，回傳升冪新串列，需正確處理重複值。
並說明最差情況。


#### 建議函式／介面

```python
def quick_sort(items: list[int]) -> list[int]:
```


#### 範例

quick_sort([3,1,2,3]) -> [1,2,3,3]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 040. 廣度優先搜尋 BFS


- **難度：** 中階
- **主題：** graph、deque


#### 題目

圖以 adjacency dict 表示。實作 `bfs(graph,start)`，回傳從 start 出發的拜訪順序。
鄰居按原串列順序處理，且圖可能有環。


#### 建議函式／介面

```python
def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
```


#### 範例

graph={"A":["B","C"],"B":["D"],"C":[],"D":[]}
bfs(graph,"A") -> ["A","B","C","D"]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 041. 深度優先搜尋 DFS


- **難度：** 中階
- **主題：** graph、stack


#### 題目

以迭代方式實作 DFS，回傳拜訪順序。鄰居要按照 adjacency list 原順序深入。


#### 建議函式／介面

```python
def dfs(graph: dict[str, list[str]], start: str) -> list[str]:
```


#### 範例

graph={"A":["B","C"],"B":["D"],"C":[],"D":[]}
dfs(graph,"A") -> ["A","B","D","C"]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 042. 無權重最短路徑


- **難度：** 中階
- **主題：** BFS、parent map


#### 題目

實作 `shortest_path(graph,start,end)`，回傳無權重圖中最少邊數的路徑；不存在回傳空串列。


#### 建議函式／介面

```python
def shortest_path(graph: dict[str, list[str]], start: str, end: str) -> list[str]:
```


#### 範例

A-B-D 與 A-C-E-D 中應回傳較短的 A-B-D。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 043. 以 heap 取得前 K 大值


- **難度：** 中階
- **主題：** heapq、Top-K


#### 題目

實作 `largest_k(numbers,k)`，回傳前 k 大值的遞減串列。k 可為 0；若 k 大於資料長度，回傳全部。


#### 建議函式／介面

```python
def largest_k(numbers: list[int], k: int) -> list[int]:
```


#### 範例

largest_k([5,1,9,3,7],3) -> [9,7,5]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 044. 固定長度滑動視窗最大總和


- **難度：** 中階
- **主題：** sliding window


#### 題目

實作 `max_window_sum(numbers,k)`，回傳連續 k 個元素的最大總和。k 必須介於 1 與 len(numbers)。


#### 建議函式／介面

```python
def max_window_sum(numbers: list[int], k: int) -> int:
```


#### 範例

max_window_sum([2,1,5,1,3,2],3) -> 9


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 045. 雙指標移除重複值


- **難度：** 中階
- **主題：** two pointers、in-place


#### 題目

已排序串列 `numbers`，原地移除重複值，回傳有效長度 k；前 k 個元素需為唯一值。


#### 建議函式／介面

```python
def remove_duplicates_sorted(numbers: list[int]) -> int:
```


#### 範例

numbers=[1,1,2,2,3] -> k=3，numbers[:3]==[1,2,3]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 046. 前綴和區間查詢


- **難度：** 中階
- **主題：** prefix sum


#### 題目

建立 `build_prefix(numbers)`，再實作 `range_sum(prefix,left,right)` 回傳包含兩端的區間總和。
需驗證索引。


#### 建議函式／介面

```python
def build_prefix(numbers: list[int]) -> list[int]:
def range_sum(prefix: list[int], left: int, right: int) -> int:
```


#### 範例

numbers=[2,4,1,3]，range_sum(prefix,1,3) -> 8


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 047. 和為 K 的子陣列數量


- **難度：** 中階
- **主題：** prefix sum、hash map


#### 題目

實作 `count_subarrays_sum(numbers,k)`，計算連續子陣列總和等於 k 的數量。元素可為負數。


#### 建議函式／介面

```python
def count_subarrays_sum(numbers: list[int], k: int) -> int:
```


#### 範例

count_subarrays_sum([1,1,1],2) -> 2


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 048. CSV 交易彙總


- **難度：** 中階
- **主題：** csv 模組、檔案 I/O


#### 題目

CSV 欄位為 `account,amount`。實作 `sum_csv(path)`，以 UTF-8-sig 讀取，略過空列，
回傳帳戶總額 dict；欄位缺失或金額錯誤應指出行號。


#### 建議函式／介面

```python
def sum_csv(path: str) -> dict[str, float]:
```


#### 範例

A,10 與 A,5 -> {"A":15.0}


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 049. JSON Schema 基礎驗證


- **難度：** 中階
- **主題：** json、資料驗證


#### 題目

輸入 JSON 字串，格式應為物件且包含字串 `customer_id`、非負數 `amount`、字串 `currency`。
實作 `parse_payment_json(payload)`，成功回傳 dict，失敗拋出 `ValueError`。


#### 建議函式／介面

```python
def parse_payment_json(payload: str) -> dict:
```


#### 範例

'{"customer_id":"C1","amount":100,"currency":"TWD"}' -> dict


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 050. 正規表示式驗證 Email


- **難度：** 中階
- **主題：** re、fullmatch


#### 題目

實作簡化版 `is_valid_email(email)`：本地部分允許英數與 `._%+-`，網域允許英數、點、連字號，
頂級網域至少 2 個英文字母。必須整串匹配。


#### 建議函式／介面

```python
def is_valid_email(email: str) -> bool:
```


#### 範例

is_valid_email("user.name+tag@example.com") -> True


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 051. 計算工作日


- **難度：** 中階
- **主題：** datetime、集合


#### 題目

實作 `business_days(start,end,holidays)`，計算含起訖日的工作日數。
週六、週日與 holidays 不算；若 end 早於 start 拋出錯誤。


#### 建議函式／介面

```python
def business_days(start: date, end: date, holidays: set[date]) -> int:
```


#### 範例

週一到週五、無假日 -> 5


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 052. NumPy Min-Max 正規化


- **難度：** 中階
- **主題：** NumPy、向量化


#### 題目

實作 `minmax_scale(values)`，將一維數值陣列縮放到 0~1。
若所有值相同，回傳全 0；輸入需轉成 float ndarray。


#### 建議函式／介面

```python
def minmax_scale(values):
```


#### 範例

[10,20,30] -> [0.0,0.5,1.0]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 053. NumPy 矩陣乘法與 shape


- **難度：** 中階
- **主題：** NumPy、線性代數


#### 題目

實作 `linear_scores(X,w,b)`，計算 `X @ w + b`。驗證 X 為二維、w 為一維，且特徵數相同。


#### 建議函式／介面

```python
def linear_scores(X, w, b: float):
```


#### 範例

X shape=(3,2), w shape=(2,) -> output shape=(3,)


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 054. pandas 缺失值處理


- **難度：** 中階
- **主題：** pandas、fillna、median


#### 題目

DataFrame 含 `age`、`income`、`city`。實作 `clean_customers(df)`：
age 以中位數補值，income 缺失列刪除，city 以 `"UNKNOWN"` 補值，且不得修改原 df。


#### 建議函式／介面

```python
def clean_customers(df):
```


#### 範例

輸出為清理後的新 DataFrame。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 055. pandas 月交易彙總


- **難度：** 中階
- **主題：** pandas、datetime、groupby


#### 題目

DataFrame 含 `account`、`timestamp`、`amount`。實作每帳戶每月的交易總額與筆數，
輸出欄位 `account,month,total_amount,tx_count`。


#### 建議函式／介面

```python
def monthly_summary(df):
```


#### 範例

同一帳戶同月多筆交易合併為一列。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 056. pandas 合併客戶與交易


- **難度：** 中階
- **主題：** pandas、merge、join validation


#### 題目

customers 有唯一 `customer_id`；transactions 可有多筆同客戶。實作 left join，
保留所有交易，並驗證關係為 many-to-one。找不到客戶的交易要標記 `customer_missing=True`。


#### 建議函式／介面

```python
def enrich_transactions(transactions, customers):
```


#### 範例

交易客戶不存在時仍保留該列。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 057. pandas 樞紐分析表


- **難度：** 中階
- **主題：** pivot_table、報表


#### 題目

DataFrame 含 `branch`、`channel`、`amount`。實作分行×通路的金額總和樞紐表，
缺少組合填 0，並加入總計列與總計欄。


#### 建議函式／介面

```python
def branch_channel_pivot(df):
```


#### 範例

index=branch，columns=channel，值為 amount sum。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 058. SQLite 參數化查詢


- **難度：** 中階
- **主題：** SQL、sqlite3、安全查詢


#### 題目

實作 `find_transactions(conn, account, min_amount)`，查詢指定帳戶且金額大於等於門檻的紀錄，
依 timestamp 升冪。不得使用 f-string 拼接 SQL。


#### 建議函式／介面

```python
def find_transactions(conn, account: str, min_amount: float) -> list[tuple]:
```


#### 範例

回傳 cursor.fetchall()。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 059. Generator 分批處理


- **難度：** 中階
- **主題：** yield、迭代器、記憶體


#### 題目

實作 `chunks(iterable,size)`，把任意 iterable 分成最多 size 個元素的 list 逐批 yield。
size 必須大於 0。


#### 建議函式／介面

```python
def chunks(iterable, size: int):
```


#### 範例

list(chunks(range(5),2)) -> [[0,1],[2,3],[4]]


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 060. Decorator 記錄執行時間


- **難度：** 中階
- **主題：** decorator、functools、time


#### 題目

實作 `timed` decorator，執行函式後印出函式名稱與耗時，並保留原函式 metadata。
即使函式拋出例外也要記錄耗時。


#### 建議函式／介面

```python
def timed(func):
```


#### 範例

@timed
def work(): ...


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 061. 單元測試：parse_amount


- **難度：** 中階
- **主題：** unittest、邊界測試


#### 題目

為第 1 題 `parse_amount` 撰寫 unittest，至少測正常四捨五入、負數、非數字、NaN 四種情況。


#### 建議函式／介面

```python
class ParseAmountTests(unittest.TestCase):
```


#### 範例

執行 `python -m unittest` 應全部通過。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 062. 密碼安全雜湊


- **難度：** 中階
- **主題：** hashlib、salt、constant-time compare


#### 題目

實作 `hash_password(password)` 與 `verify_password(password, stored)`，
使用 `hashlib.pbkdf2_hmac`、隨機 salt 與至少 200,000 次迭代。stored 可採 `iterations$salt_hex$digest_hex`。


#### 建議函式／介面

```python
def hash_password(password: str) -> str:
def verify_password(password: str, stored: str) -> bool:
```


#### 範例

verify_password("secret", hash_password("secret")) -> True


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 063. 輸入白名單與 SQL 注入防護


- **難度：** 中階
- **主題：** 安全程式設計、白名單


#### 題目

實作 `build_order_clause(field,direction)`，field 只允許 `timestamp,amount,account`，
direction 只允許 `ASC,DESC`（不分大小寫）。回傳安全的 ORDER BY 片段，非法值拋出錯誤。


#### 建議函式／介面

```python
def build_order_clause(field: str, direction: str) -> str:
```


#### 範例

build_order_clause("amount","desc") -> "ORDER BY amount DESC"


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 064. Big-O 優化：重複會員查找


- **難度：** 中階
- **主題：** 複雜度、set


#### 題目

原程式對每筆交易執行 `if customer_id in customer_list`，customer_list 是 list。
實作 `filter_known_transactions(transactions, customer_ids)`，先建立適當資料結構，
回傳已知客戶交易。


#### 建議函式／介面

```python
def filter_known_transactions(transactions: list[dict], customer_ids: list[str]) -> list[dict]:
```


#### 範例

大量交易與會員資料時，應避免每筆線性搜尋。


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌


### 065. dataclass 交易資料模型


- **難度：** 中階
- **主題：** dataclasses、型別、__post_init__


#### 題目

建立不可變的 `Transaction` dataclass，欄位為 `tx_id: str`、`amount: Decimal`、`currency: str`。
在 `__post_init__` 驗證 tx_id 不可為空、amount 不可為負、currency 必須是三碼大寫英文字母。


#### 建議函式／介面

```python
@dataclass(frozen=True)
class Transaction:
```


#### 範例

Transaction("T001", Decimal("100.00"), "TWD") 可建立；
Transaction("", Decimal("1"), "TWD") -> ValueError


#### 自我檢查

- [ ] 正常案例通過
- [ ] 空值／邊界／錯誤輸入已處理
- [ ] 能說明使用的資料結構
- [ ] 能寫出時間與空間複雜度
- [ ] 沒有把敏感資料直接印到日誌

## 參考依據（官方公開資料）

1. 台灣金融研訓院，〈臺灣土地銀行股份有限公司 115 年新進人員甄試簡章〉，2026-06-25。
2. 臺灣土地銀行，〈永續發展－客戶權益－數位金融〉，內容涵蓋智能客服、RPA、大數據分析與爬網應用。
3. 臺灣土地銀行，〈防詐利器再加一 土地銀行啟用短碼簡訊〉，2024-06-27。
4. 臺灣土地銀行，〈土銀攜手高檢署簽署 MOU 用數據強化 AI 識詐模型〉，2025-12-10。
5. 臺灣土地銀行，〈土地銀行 ATM 導入 AI 臉部辨識防詐〉，2026-01-20。
6. 臺灣土地銀行，〈永續發展－公司治理－誠信經營〉，內容涵蓋 CRA 法令遵循管理系統。
7. 臺灣土地銀行，〈115 年度行務會議：聚焦創新與價值、邁向永續〉，2026-01-28。
8. 金融監督管理委員會，〈金融業運用人工智慧（AI）指引〉，2024-06-20。

---

本教材僅供甄試準備與程式練習；金融門檻、模型閾值、法遵判斷與生產架構均不可直接套用至正式系統。
