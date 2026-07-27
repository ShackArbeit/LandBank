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



## ??????

? **40 ?**???????? **80 ?**??????? 3 ??? 27 ????

- [ ] 001. 串列順序處理：清理待辦清單?入門?
- [ ] 002. 串列索引與切片：取最近交易?入門?
- [ ] 003. 字典查找：客戶欄位查詢?入門?
- [ ] 004. 字典更新：狀態次數統計?入門?
- [ ] 005. 串列轉字典：建立客戶查詢表?入門?
- [ ] 006. if/elif/else：訊息分流?入門?
- [ ] 007. for、continue、break：批次過濾訊息?入門?
- [ ] 008. while 迴圈：尋找第一筆及格成績?入門?
- [ ] 009. 型別轉換與交易金額驗證?入門?
- [ ] 010. 條件判斷：交易金額分級?入門?
- [ ] 011. 複利計算?入門?
- [ ] 012. FizzBuzz 變形：規則標記?入門?
- [ ] 013. 一到 n 的總和?入門?
- [ ] 014. 字元頻率統計?入門?
- [ ] 015. 空白正規化?入門?
- [ ] 016. 帳號遮罩?入門?
- [ ] 017. 密碼規則驗證?入門?
- [ ] 018. 保留順序去除重複值?入門?
- [ ] 019. Two Sum?初階?
- [ ] 020. Top-K 高頻項目?初階?
- [ ] 021. 依帳戶彙總交易?初階?
- [ ] 022. 串列生成式篩選?初階?
- [ ] 023. 多欄位排序?初階?
- [ ] 024. 安全解析交易列?初階?
- [ ] 025. 使用 context manager 讀檔?初階?
- [ ] 026. 使用 deque 實作佇列?初階?
- [ ] 027. 二分搜尋?初階?
- [ ] 028. 廣度優先搜尋 BFS?中階?
- [ ] 029. CSV 交易彙總?中階?
- [ ] 030. JSON Schema 基礎驗證?中階?
- [ ] 031. 正規表示式驗證 Email?中階?
- [ ] 032. 計算工作日?中階?
- [ ] 033. NumPy Min-Max 正規化?中階?
- [ ] 034. NumPy 矩陣乘法與 shape?中階?
- [ ] 035. pandas 缺失值處理?中階?
- [ ] 036. pandas 月交易彙總?中階?
- [ ] 037. pandas 合併客戶與交易?中階?
- [ ] 038. pandas 樞紐分析表?中階?
- [ ] 039. SQLite 參數化查詢?中階?
- [ ] 040. 輸入白名單與 SQL 注入防護?中階?

---

## ?????


### 001. 串列順序處理：清理待辦清單 ( 7/19 Done )


- **難度：** 入門
- **主題：** list、順序、append


#### 題目

實作 `clean_tasks(tasks)`，接受一個待辦事項串列。請逐項去除前後空白，忽略空字串，並保留原本順序。
回傳清理後的新串列，不可修改原本傳入的串列。


#### 建議函式／介面

```python
def clean_tasks(tasks):
```

### 002. 串列索引與切片：取最近交易 ( 7/20 Done )


- **難度：** 入門
- **主題：** list、索引、切片


#### 題目

實作 `latest_transactions(transactions, n)`，接受依時間由舊到新排列的交易串列，回傳最近 `n` 筆交易。
若 `n` 小於等於 0，回傳空串列；若 `n` 大於資料筆數，回傳全部資料。不可修改原本串列。


#### 建議函式／介面

```python
def latest_transactions(transactions, n):
```

### 003. 字典查找：客戶欄位查詢 ( 7/20 Done )


- **難度：** 入門
- **主題：** dict、key 查找、預設值


#### 題目

實作 `get_customer_field(customer, field, default=None)`，接受單一客戶字典、欄位名稱與預設值。
若欄位存在，回傳對應值；若不存在，回傳 `default`。若 `customer` 不是字典，拋出 `ValueError`。


#### 建議函式／介面

```python
def get_customer_field(customer, field, default=None):
```

### 004. 字典更新：狀態次數統計 ( 7/20 Done )


- **難度：** 入門
- **主題：** dict、迴圈、累計


#### 題目

實作 `count_status(records)`，接受交易紀錄串列。每筆紀錄是字典，可能包含 `"status"` 欄位。
請統計各狀態出現次數；缺少 `"status"` 或狀態為空字串時，歸類為 `"UNKNOWN"`。


#### 建議函式／介面

```python
def count_status(records):
```

### 005. 串列轉字典：建立客戶查詢表 ( 7/21 Done)


- **難度：** 入門
- **主題：** list、dict、key 唯一性


#### 題目

實作 `build_customer_index(customers)`，接受客戶資料串列。每筆客戶資料是字典，且必須有 `"id"` 欄位。
回傳以客戶 id 為 key、原客戶字典為 value 的查詢表。若缺少 id、id 為空或 id 重複，拋出 `ValueError`。


#### 建議函式／介面

```python
def build_customer_index(customers):
```

### 006. if/elif/else：訊息分流 ( 7/21 Done )


- **難度：** 入門
- **主題：** if/elif/else、字串判斷


#### 題目

實作 `classify_message(message)`，依訊息內容回傳分類：
空白訊息回傳 `"EMPTY"`；包含 `"轉帳"` 或 `"匯款"` 回傳 `"TRANSFER"`；包含 `"密碼"` 回傳 `"PASSWORD"`；
其他訊息回傳 `"OTHER"`。判斷前請先去除前後空白。


#### 建議函式／介面

```python
def classify_message(message):
```

### 007. for、continue、break：批次過濾訊息 ( 7/21 Done )


- **難度：** 入門
- **主題：** for、continue、break


#### 題目

實作 `collect_valid_messages(messages)`，逐筆處理訊息串列。
空白訊息要用 `continue` 跳過；遇到內容為 `"STOP"` 的訊息時，用 `break` 停止處理；
其他訊息去除前後空白後加入結果串列。


#### 建議函式／介面

```python
def collect_valid_messages(messages):
```

### 008. while 迴圈：尋找第一筆及格成績 ( 7/21 Done )


- **難度：** 入門
- **主題：** while、條件更新、索引


#### 題目

實作 `first_passing_index(scores, passing_score=60)`，使用 `while` 迴圈尋找第一個大於等於及格分數的索引。
若找不到，回傳 `-1`。請注意每輪都要更新索引，避免無窮迴圈。


#### 建議函式／介面

```python
def first_passing_index(scores, passing_score=60):
```

### 009. 型別轉換與交易金額驗證 ( 7/21 Done )


- **難度：** 入門
- **主題：** 型別、例外處理、Decimal


#### 題目

實作 `parse_amount(value)`，接受整數、浮點數或字串，回傳 `Decimal` 金額並四捨五入至小數第 2 位。
空字串、非數字、NaN、Infinity 或負數都要拋出 `ValueError`。金融金額不得直接依賴二進位浮點數累加。


#### 建議函式／介面

```python
def parse_amount(value):
```

### 010. 條件判斷：交易金額分級 ( 7/21 Done )


- **難度：** 入門
- **主題：** if/elif/else、邊界條件


#### 題目

實作 `risk_band(amount)`：金額小於 10,000 回傳 `"LOW"`；10,000 至未滿 100,000 回傳 `"MEDIUM"`；
100,000 以上回傳 `"HIGH"`。負數須拋出 `ValueError`。


#### 建議函式／介面

```python
def risk_band(amount):
```

### 011. 複利計算


- **難度：** 入門
- **主題：** 運算子、函式、次方


#### 題目

實作 `compound(principal, annual_rate, years, times_per_year=12)`，
計算複利終值 `P(1+r/n)^(nt)`，結果四捨五入至小數第 2 位。輸入不得為負，複利次數必須大於 0。


#### 建議函式／介面

```python
def compound(principal, annual_rate, years, times_per_year=12):
```

### 012. FizzBuzz 變形：規則標記 ( 7/22 Done )


- **難度：** 入門
- **主題：** 迴圈、模數、串列


#### 題目

對 1 到 n 產生標記：3 的倍數為 `"A"`，5 的倍數為 `"B"`，同時為兩者倍數為 `"AB"`，
其餘轉成字串。回傳字串串列。


#### 建議函式／介面

```python
def rule_tags(n):
```

### 013. 一到 n 的總和 ( 7/22 Done )


- **難度：** 入門
- **主題：** 迴圈、公式、複雜度


#### 題目

分別實作 `sum_loop(n)` 與 `sum_formula(n)`，計算 1 到 n 的總和，並比較時間複雜度。
n 小於 0 時拋出 `ValueError`。


#### 建議函式／介面

```python
def sum_loop(n):
def sum_formula(n):
```

### 014. 字元頻率統計 ( 7/22 Done )


- **難度：** 入門
- **主題：** dict、Counter


#### 題目

實作 `char_frequency(text)`，忽略空白並不分大小寫，回傳每個字元出現次數。


#### 建議函式／介面

```python
def char_frequency(text):
```

### 015. 空白正規化 ( 7/22 Done )


- **難度：** 入門
- **主題：** split、join


#### 題目

實作 `normalize_spaces(text)`，把連續空白（空格、Tab、換行）縮成單一空格，並移除頭尾空白。


#### 建議函式／介面

```python
def normalize_spaces(text):
```

### 016. 帳號遮罩 ( 7/22 Done )


- **難度：** 入門
- **主題：** 字串切片、資料隱私


#### 題目

實作 `mask_account(account, visible=4)`：只保留末 visible 碼，其餘以 `*` 取代。
若 visible 為負數拋出錯誤；若帳號長度不超過 visible，全部回傳。


#### 建議函式／介面

```python
def mask_account(account, visible=4):
```

### 017. 密碼規則驗證 ( 7/ 22 Done )


- **難度：** 入門
- **主題：** 字串方法、all/any


#### 題目

實作 `validate_password(password)`，要求至少 10 碼，且至少包含一個大寫字母、小寫字母、數字及特殊字元。
回傳 `(bool, list[str])`，第二項列出未通過規則。


#### 建議函式／介面

```python
def validate_password(password):
```

### 018. 保留順序去除重複值 ( 7/22 Done )


- **難度：** 入門
- **主題：** list、set


#### 題目

實作 `deduplicate(items)`，移除重複元素但保留第一次出現的順序。假設元素可雜湊。


#### 建議函式／介面

```python
def deduplicate(items):
```

### 019. Two Sum ( 7/23 Done )


- **難度：** 初階
- **主題：** 雜湊表、索引


#### 題目

給定整數串列與 target，找出兩個不同索引，使其數值總和等於 target。回傳索引 tuple；
若不存在回傳 `None`。只需回傳第一組。


#### 建議函式／介面

```python
def two_sum(numbers, target):
```

### 020. Top-K 高頻項目 (7/23 Done )


- **難度：** 初階
- **主題：** Counter、heap


#### 題目

實作 `top_k_frequent(items,k)`，回傳出現次數最高的 k 個項目與次數，依次數遞減、項目字串遞增排序。


#### 建議函式／介面

```python
def top_k_frequent(items, k):
```

### 021. 依帳戶彙總交易 ( 7/23 Done )


- **難度：** 初階
- **主題：** dict、defaultdict


#### 題目

輸入為 `(account, amount)` tuple 串列，回傳每個帳戶的交易總額。空帳戶字串視為錯誤。


#### 建議函式／介面

```python
def aggregate_by_account(records):
```

### 022. 串列生成式篩選 ( 7/23 Done )


- **難度：** 初階
- **主題：** comprehension、條件


#### 題目

給定交易金額串列，回傳所有大於等於 threshold 的正數平方，並保持原順序。
負數與 0 一律忽略。


#### 建議函式／介面

```python
def filtered_squares(amounts, threshold):
```

### 023. 多欄位排序 ( 7/24 Done )


- **難度：** 初階
- **主題：** sorted、lambda、穩定排序


#### 題目

交易紀錄為 dict，含 `risk`、`amount`、`id`。依 risk 由高到低、amount 由高到低、id 由小到大排序，
且不得修改原串列。


#### 建議函式／介面

```python
def sort_transactions(records):
```

### 024. 安全解析交易列 ( 7/24 Done )


- **難度：** 初階
- **主題：** 例外處理、錯誤收集


#### 題目

輸入多行 `"account,amount"` 字串。實作 `parse_rows(lines)`，回傳 `(valid_records, errors)`。
錯誤不能中止整批處理；errors 需包含 1-based 行號與原因。


#### 建議函式／介面

```python
def parse_rows(lines):
```

### 025. 使用 context manager 讀檔 ( 7/26 Done )


- **難度：** 初階
- **主題：** with、檔案 I/O


#### 題目

實作 `count_nonempty_lines(path)`，以 UTF-8 讀取文字檔並計算非空白行數。必須確保發生例外時檔案仍會關閉。


#### 建議函式／介面

```python
def count_nonempty_lines(path):
```

### 026. 使用 deque 實作佇列 ( 7/26 Done )


- **難度：** 初階
- **主題：** queue、deque


#### 題目

實作 `process_queue(items)`：依輸入順序處理元素並回傳處理順序。必須使用適合從左端移除的資料結構。


#### 建議函式／介面

```python
def process_queue(items):
```

### 027. 二分搜尋 ( 7/27 Done  )


- **難度：** 初階
- **主題：** binary search、邊界


#### 題目

在升冪串列中尋找 target，回傳任一匹配索引，不存在回傳 -1。請用迭代方式實作。


#### 建議函式／介面

```python
def binary_search(numbers, target):
```

### 028. 廣度優先搜尋 BFS ( 7/27 Done )


- **難度：** 中階
- **主題：** graph、deque


#### 題目

圖以 adjacency dict 表示。實作 `bfs(graph,start)`，回傳從 start 出發的拜訪順序。
鄰居按原串列順序處理，且圖可能有環。


#### 建議函式／介面

```python
def bfs(graph, start):
```

### 029. CSV 交易彙總


- **難度：** 中階
- **主題：** csv 模組、檔案 I/O


#### 題目

CSV 欄位為 `account,amount`。實作 `sum_csv(path)`，以 UTF-8-sig 讀取，略過空列，
回傳帳戶總額 dict；欄位缺失或金額錯誤應指出行號。


#### 建議函式／介面

```python
def sum_csv(path):
```

### 030. JSON Schema 基礎驗證


- **難度：** 中階
- **主題：** json、資料驗證


#### 題目

輸入 JSON 字串，格式應為物件且包含字串 `customer_id`、非負數 `amount`、字串 `currency`。
實作 `parse_payment_json(payload)`，成功回傳 dict，失敗拋出 `ValueError`。


#### 建議函式／介面

```python
def parse_payment_json(payload):
```

### 031. 正規表示式驗證 Email


- **難度：** 中階
- **主題：** re、fullmatch


#### 題目

實作簡化版 `is_valid_email(email)`：本地部分允許英數與 `._%+-`，網域允許英數、點、連字號，
頂級網域至少 2 個英文字母。必須整串匹配。


#### 建議函式／介面

```python
def is_valid_email(email):
```

### 032. 計算工作日


- **難度：** 中階
- **主題：** datetime、集合


#### 題目

實作 `business_days(start,end,holidays)`，計算含起訖日的工作日數。
週六、週日與 holidays 不算；若 end 早於 start 拋出錯誤。


#### 建議函式／介面

```python
def business_days(start, end, holidays):
```

### 033. NumPy Min-Max 正規化


- **難度：** 中階
- **主題：** NumPy、向量化


#### 題目

實作 `minmax_scale(values)`，將一維數值陣列縮放到 0~1。
若所有值相同，回傳全 0；輸入需轉成 float ndarray。


#### 建議函式／介面

```python
def minmax_scale(values):
```

### 034. NumPy 矩陣乘法與 shape


- **難度：** 中階
- **主題：** NumPy、線性代數


#### 題目

實作 `linear_scores(X,w,b)`，計算 `X @ w + b`。驗證 X 為二維、w 為一維，且特徵數相同。


#### 建議函式／介面

```python
def linear_scores(X, w, b):
```

### 035. pandas 缺失值處理


- **難度：** 中階
- **主題：** pandas、fillna、median


#### 題目

DataFrame 含 `age`、`income`、`city`。實作 `clean_customers(df)`：
age 以中位數補值，income 缺失列刪除，city 以 `"UNKNOWN"` 補值，且不得修改原 df。


#### 建議函式／介面

```python
def clean_customers(df):
```

### 036. pandas 月交易彙總


- **難度：** 中階
- **主題：** pandas、datetime、groupby


#### 題目

DataFrame 含 `account`、`timestamp`、`amount`。實作每帳戶每月的交易總額與筆數，
輸出欄位 `account,month,total_amount,tx_count`。


#### 建議函式／介面

```python
def monthly_summary(df):
```

### 037. pandas 合併客戶與交易


- **難度：** 中階
- **主題：** pandas、merge、join validation


#### 題目

customers 有唯一 `customer_id`；transactions 可有多筆同客戶。實作 left join，
保留所有交易，並驗證關係為 many-to-one。找不到客戶的交易要標記 `customer_missing=True`。


#### 建議函式／介面

```python
def enrich_transactions(transactions, customers):
```

### 038. pandas 樞紐分析表


- **難度：** 中階
- **主題：** pivot_table、報表


#### 題目

DataFrame 含 `branch`、`channel`、`amount`。實作分行×通路的金額總和樞紐表，
缺少組合填 0，並加入總計列與總計欄。


#### 建議函式／介面

```python
def branch_channel_pivot(df):
```

### 039. SQLite 參數化查詢


- **難度：** 中階
- **主題：** SQL、sqlite3、安全查詢


#### 題目

實作 `find_transactions(conn, account, min_amount)`，查詢指定帳戶且金額大於等於門檻的紀錄，
依 timestamp 升冪。不得使用 f-string 拼接 SQL。


#### 建議函式／介面

```python
def find_transactions(conn, account, min_amount):
```

### 040. 輸入白名單與 SQL 注入防護


- **難度：** 中階
- **主題：** 安全程式設計、白名單


#### 題目

實作 `build_order_clause(field,direction)`，field 只允許 `timestamp,amount,account`，
direction 只允許 `ASC,DESC`（不分大小寫）。回傳安全的 ORDER BY 片段，非法值拋出錯誤。


#### 建議函式／介面

```python
def build_order_clause(field, direction):
```

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
