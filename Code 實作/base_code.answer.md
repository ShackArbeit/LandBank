# 2026 土地銀行 AI 應用人員：Python 程式設計基礎詳解


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


## 二、使用方式

答案不只提供可執行程式，也刻意補上原理、複雜度與金融情境風險。
考試作答時不必逐字照抄，但應保留「輸入驗證 → 主演算法 → 複雜度 → 邊界」四層。


## ??????

? **40 ?**???????? **80 ?**?

- [001. 串列順序處理：清理待辦清單](#001-串列順序處理：清理待辦清單)
- [002. 串列索引與切片：取最近交易](#002-串列索引與切片：取最近交易)
- [003. 字典查找：客戶欄位查詢](#003-字典查找：客戶欄位查詢)
- [004. 字典更新：狀態次數統計](#004-字典更新：狀態次數統計)
- [005. 串列轉字典：建立客戶查詢表](#005-串列轉字典：建立客戶查詢表)
- [006. if/elif/else：訊息分流](#006-if/elif/else：訊息分流)
- [007. for、continue、break：批次過濾訊息](#007-for、continue、break：批次過濾訊息)
- [008. while 迴圈：尋找第一筆及格成績](#008-while-迴圈：尋找第一筆及格成績)
- [009. 型別轉換與交易金額驗證](#009-型別轉換與交易金額驗證)
- [010. 條件判斷：交易金額分級](#010-條件判斷：交易金額分級)
- [011. 複利計算](#011-複利計算)
- [012. FizzBuzz 變形：規則標記](#012-fizzbuzz-變形：規則標記)
- [013. 一到 n 的總和](#013-一到-n-的總和)
- [014. 字元頻率統計](#014-字元頻率統計)
- [015. 空白正規化](#015-空白正規化)
- [016. 帳號遮罩](#016-帳號遮罩)
- [017. 密碼規則驗證](#017-密碼規則驗證)
- [018. 保留順序去除重複值](#018-保留順序去除重複值)
- [019. Two Sum](#019-two-sum)
- [020. Top-K 高頻項目](#020-top-k-高頻項目)
- [021. 依帳戶彙總交易](#021-依帳戶彙總交易)
- [022. 串列生成式篩選](#022-串列生成式篩選)
- [023. 多欄位排序](#023-多欄位排序)
- [024. 安全解析交易列](#024-安全解析交易列)
- [025. 使用 context manager 讀檔](#025-使用-context-manager-讀檔)
- [026. 使用 deque 實作佇列](#026-使用-deque-實作佇列)
- [027. 二分搜尋](#027-二分搜尋)
- [028. 廣度優先搜尋 BFS](#028-廣度優先搜尋-bfs)
- [029. CSV 交易彙總](#029-csv-交易彙總)
- [030. JSON Schema 基礎驗證](#030-json-schema-基礎驗證)
- [031. 正規表示式驗證 Email](#031-正規表示式驗證-email)
- [032. 計算工作日](#032-計算工作日)
- [033. NumPy Min-Max 正規化](#033-numpy-min-max-正規化)
- [034. NumPy 矩陣乘法與 shape](#034-numpy-矩陣乘法與-shape)
- [035. pandas 缺失值處理](#035-pandas-缺失值處理)
- [036. pandas 月交易彙總](#036-pandas-月交易彙總)
- [037. pandas 合併客戶與交易](#037-pandas-合併客戶與交易)
- [038. pandas 樞紐分析表](#038-pandas-樞紐分析表)
- [039. SQLite 參數化查詢](#039-sqlite-參數化查詢)
- [040. 輸入白名單與 SQL 注入防護](#040-輸入白名單與-sql-注入防護)

---

## ??????


### 001. 串列順序處理：清理待辦清單


#### 核心原理

串列適合保存有順序的資料。處理清單時，通常用 `for` 逐項巡覽，再用 `append` 建立新的結果串列，避免直接改到原始資料。


#### Python 解答

```python
def clean_tasks(tasks):
    result = []
    for task in tasks:
        cleaned = str(task).strip()
        if cleaned:
            result.append(cleaned)
    return result
```


#### 複雜度

O(n) 時間、O(n) 空間。


#### 常見錯誤與延伸

不要一邊巡覽一邊刪除原串列元素，容易跳過資料。先建立新串列通常較清楚。

### 002. 串列索引與切片：取最近交易


#### 核心原理

串列有順序且支援索引與切片。若資料已由舊到新排序，最近 `n` 筆就是尾端 `n` 筆。


#### Python 解答

```python
def latest_transactions(transactions, n):
    if n <= 0:
        return []
    return transactions[-n:]
```


#### 複雜度

O(k) 時間、O(k) 空間，k 為回傳筆數。


#### 常見錯誤與延伸

`transactions[-0:]` 會等於整個串列，所以必須先處理 `n <= 0`。

### 003. 字典查找：客戶欄位查詢


#### 核心原理

字典以 key 對應 value，適合用欄位名稱快速查找資料。`get` 可在 key 不存在時回傳預設值。


#### Python 解答

```python
def get_customer_field(customer, field, default=None):
    if not isinstance(customer, dict):
        raise ValueError('customer 必須是字典')
    return customer.get(field, default)
```


#### 複雜度

平均 O(1) 時間、O(1) 空間。


#### 常見錯誤與延伸

不要用 `customer[field]` 處理可缺漏欄位，否則 key 不存在時會拋出 `KeyError`。

### 004. 字典更新：狀態次數統計


#### 核心原理

字典常用來累計分類次數。每讀到一筆資料，就把對應 key 的計數加一。


#### Python 解答

```python
def count_status(records):
    counts = {}
    for record in records:
        status = record.get('status', '')
        status = str(status).strip()
        if not status:
            status = 'UNKNOWN'
        counts[status] = counts.get(status, 0) + 1
    return counts
```


#### 複雜度

O(n) 時間、O(k) 空間，k 為不同狀態數。


#### 常見錯誤與延伸

要先處理缺漏與空白值，否則空字串和真正狀態會混在統計結果裡。

### 005. 串列轉字典：建立客戶查詢表


#### 核心原理

串列適合保存多筆資料，字典適合快速查找。把串列轉成以 id 為 key 的字典，可把查找從線性掃描降為平均 O(1)。


#### Python 解答

```python
def build_customer_index(customers):
    index = {}
    for customer in customers:
        customer_id = customer.get('id')
        if not customer_id:
            raise ValueError('客戶 id 不可為空')
        if customer_id in index:
            raise ValueError('客戶 id 不可重複')
        index[customer_id] = customer
    return index
```


#### 複雜度

O(n) 時間、O(n) 空間。


#### 常見錯誤與延伸

字典 key 不可重複；若沒有主動檢查，後面的資料會覆蓋前面的資料。

### 006. if/elif/else：訊息分流


#### 核心原理

條件判斷會依資料狀態決定程式走哪條路。多個互斥分類通常用 `if`、`elif`、`else` 由特殊情況往一般情況判斷。


#### Python 解答

```python
def classify_message(message):
    text = str(message).strip()
    if not text:
        return 'EMPTY'
    if '轉帳' in text or '匯款' in text:
        return 'TRANSFER'
    if '密碼' in text:
        return 'PASSWORD'
    return 'OTHER'
```


#### 複雜度

O(n) 時間、O(n) 空間，n 為訊息長度。


#### 常見錯誤與延伸

空白訊息要先判斷，否則後續分類可能把無效輸入當成一般訊息。

### 007. for、continue、break：批次過濾訊息


#### 核心原理

`for` 適合逐筆處理已知資料集合。`continue` 跳過本輪，`break` 直接結束整個迴圈。


#### Python 解答

```python
def collect_valid_messages(messages):
    result = []
    for message in messages:
        text = str(message).strip()
        if not text:
            continue
        if text == 'STOP':
            break
        result.append(text)
    return result
```


#### 複雜度

O(n) 時間、O(n) 空間；若提前遇到 `STOP`，實際處理筆數會較少。


#### 常見錯誤與延伸

`continue` 只跳過本輪，`break` 才會停止整個迴圈；兩者語意不同。

### 008. while 迴圈：尋找第一筆及格成績


#### 核心原理

`while` 適合在條件成立前持續執行。使用索引巡覽時，必須在每輪更新索引，避免無窮迴圈。


#### Python 解答

```python
def first_passing_index(scores, passing_score=60):
    index = 0
    while index < len(scores):
        if scores[index] >= passing_score:
            return index
        index += 1
    return -1
```


#### 複雜度

O(n) 時間、O(1) 空間。


#### 常見錯誤與延伸

若忘記 `index += 1`，且目前分數未達標，迴圈會停不下來。

### 009. 型別轉換與交易金額驗證


#### 核心原理

Python 的 `float` 採二進位浮點表示，某些十進位小數無法精確表示。金融金額通常使用 `Decimal`，
並從字串建立數值。驗證時需同時檢查有限值、正負號與量化規則。


#### Python 解答

```python
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def parse_amount(value):
    try:
        amount = Decimal(str(value).strip())
    except (InvalidOperation, AttributeError):
        raise ValueError('金額格式錯誤')
    if not amount.is_finite() or amount < 0:
        raise ValueError('金額必須是有限的非負數')
    return amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

不要寫 `Decimal(0.1)`；這會先產生不精確的 float。應寫 `Decimal("0.1")`。
此外，`Decimal("NaN")` 不會在建構時失敗，所以仍要呼叫 `is_finite()`。

### 010. 條件判斷：交易金額分級


#### 核心原理

多分支條件應由最嚴格或最小邊界依序判斷，並明確處理等號。考試常藉 9,999、10,000、99,999、100,000
測試 off-by-one 錯誤。


#### Python 解答

```python
def risk_band(amount):
    if amount < 0:
        raise ValueError('金額不可為負')
    if amount < 10000:
        return 'LOW'
    if amount < 100000:
        return 'MEDIUM'
    return 'HIGH'
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

邊界值要逐一測試；不要把第二段誤寫成 `amount <=100000`。

### 011. 複利計算


#### 核心原理

這題考參數驗證、預設參數與公式轉換。年利率應以小數表示，例如 2% 寫成 0.02。


#### Python 解答

```python
def compound(principal, annual_rate, years, times_per_year=12):
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError('本金、利率與年數不可為負')
    if times_per_year <= 0:
        raise ValueError('每年複利次數必須大於 0')
    value = principal * (1 + annual_rate / times_per_year) ** (times_per_year * years)
    return round(value, 2)
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

題目若要求金融級精度，應改用 Decimal；本題重點是公式與控制流程。

### 012. FizzBuzz 變形：規則標記


#### 核心原理

應先判斷同時整除的情況，或用字串累加，避免 15 只得到 A。


#### Python 解答

```python
def rule_tags(n):
    if n < 1:
        return []
    result = []
    for i in range(1, n + 1):
        tag = ''
        if i % 3 == 0:
            tag += 'A'
        if i % 5 == 0:
            tag += 'B'
        result.append(tag or str(i))
    return result
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

迴圈範圍要使用 `range(1, n + 1)`，否則會漏掉 n。

### 013. 一到 n 的總和


#### 核心原理

迴圈法逐項累加為 O(n)；等差級數公式 `n(n+1)/2` 為 O(1)。此題常用來測試能否辨識演算法優化。


#### Python 解答

```python
def sum_loop(n):
    if n < 0:
        raise ValueError('n 不可為負')
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_formula(n):
    if n < 0:
        raise ValueError('n 不可為負')
    return n * (n + 1) // 2
```


#### 複雜度

迴圈法 O(n)；公式法 O(1)；兩者額外空間皆 O(1)


#### 常見錯誤與延伸

`/` 會得到 float；整數總和應使用 `//`。

### 014. 字元頻率統計


#### 核心原理

雜湊表可在平均 O(1) 時間更新計數。`collections.Counter` 是 Python 的標準計數工具。


#### Python 解答

```python
from collections import Counter

def char_frequency(text):
    return dict(Counter((ch.casefold() for ch in text if not ch.isspace())))
```


#### 複雜度

O(n) 時間、O(k) 空間，k 為不同字元數


#### 常見錯誤與延伸

題目若要求保留標點，不能使用 `isalnum()` 過濾；此題只忽略空白。

### 015. 空白正規化


#### 核心原理

不帶參數的 `split()` 會把所有 Unicode 空白視為分隔符並忽略連續空白；再用單一空格 join。


#### Python 解答

```python
def normalize_spaces(text):
    return ' '.join(text.split())
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

`split()` 只處理一般空格，且會保留空字串，不適合本題。

### 016. 帳號遮罩


#### 核心原理

遮罩是最基本的資料最小揭露。切片 `account[-visible:]` 在 visible=0 時會出現 `-0 ==0` 的陷阱，
因此要單獨處理。


#### Python 解答

```python
def mask_account(account, visible=4):
    if visible < 0:
        raise ValueError('visible 不可為負')
    if len(account) <= visible:
        return account
    if visible == 0:
        return '*' * len(account)
    return '*' * (len(account) - visible) + account[-visible:]
```


#### 複雜度

O(n) 時間、O(n) 輸出空間


#### 常見錯誤與延伸

遮罩不等於加密；原始敏感資料仍需受到存取控制與安全儲存保護。

### 017. 密碼規則驗證


#### 核心原理

`any()` 適合表達「至少有一個」。回傳失敗原因比只回傳布林值更利於測試與使用者提示。


#### Python 解答

```python
def validate_password(password):
    errors = []
    if len(password) < 10:
        errors.append('長度至少 10')
    if not any((ch.isupper() for ch in password)):
        errors.append('缺少大寫字母')
    if not any((ch.islower() for ch in password)):
        errors.append('缺少小寫字母')
    if not any((ch.isdigit() for ch in password)):
        errors.append('缺少數字')
    if not any((not ch.isalnum() for ch in password)):
        errors.append('缺少特殊字元')
    return (not errors, errors)
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

實務上密碼規則不能取代 MFA、雜湊與登入速率限制。

### 018. 保留順序去除重複值


#### 核心原理

使用 set 記錄已看過的元素，可把雙層搜尋的 O(n²) 降到平均 O(n)。


#### Python 解答

```python
def deduplicate(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```


#### 複雜度

平均 O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

`list(set(items))` 不應依賴順序，且無法處理不可雜湊元素。

### 019. Two Sum


#### 核心原理

掃描到 value 時，查找 `target-value` 是否已出現。先查後存可避免同一索引被使用兩次。


#### Python 解答

```python
def two_sum(numbers, target):
    seen = {}
    for i, value in enumerate(numbers):
        needed = target - value
        if needed in seen:
            return (seen[needed], i)
        seen[value] = i
    return None
```


#### 複雜度

平均 O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

若題目要求所有組合或數值而非索引，資料結構與去重策略會不同。

### 020. Top-K 高頻項目


#### 核心原理

先計數，再排序不同項目。若不同項目數極大且 k 很小，可用 heap 將排序成本由 O(u log u) 降為 O(u log k)。


#### Python 解答

```python
from collections import Counter

def top_k_frequent(items, k):
    if k < 0:
        raise ValueError('k 不可為負')
    counts = Counter(items)
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ranked[:k]
```


#### 複雜度

O(n + u log u) 時間、O(u) 空間，u 為不同項目數


#### 常見錯誤與延伸

`Counter.most_common()` 對同次數項目的次序不一定符合題目指定，因此本題明確自訂排序鍵。

### 021. 依帳戶彙總交易


#### 核心原理

`defaultdict` 能省略鍵不存在時的初始化。金融題目若要求精確金額，amount 應換成 Decimal。


#### Python 解答

```python
from collections import defaultdict

def aggregate_by_account(records):
    totals = defaultdict(float)
    for account, amount in records:
        if not account:
            raise ValueError('帳戶不可為空')
        totals[account] += amount
    return dict(totals)
```


#### 複雜度

O(n) 時間、O(k) 空間


#### 常見錯誤與延伸

若使用 float，累加可能有精度誤差；實務可將金額轉為最小貨幣單位整數或 Decimal。

### 022. 串列生成式篩選


#### 核心原理

串列生成式適合簡單的一對一轉換與篩選。若條件過多，傳統迴圈可讀性更好。


#### Python 解答

```python
def filtered_squares(amounts, threshold):
    return [value * value for value in amounts if value > 0 and value >= threshold]
```


#### 複雜度

O(n) 時間、O(k) 輸出空間


#### 常見錯誤與延伸

不要為了炫技把複雜商業規則塞進一行生成式。

### 023. 多欄位排序


#### 核心原理

`sorted()` 回傳新串列。對數字可取負值實現遞減排序；tuple key 會由左至右比較。


#### Python 解答

```python
def sort_transactions(records):
    return sorted(records, key=lambda row: (-row['risk'], -row['amount'], row['id']))
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

若欄位可能缺失，應先做 schema 驗證，不要讓 KeyError 在排序中才發生。

### 024. 安全解析交易列


#### 核心原理

批次資料處理通常採「逐筆驗證、錯誤隔離」。例外範圍要小，只包住真正可能失敗的轉換。


#### Python 解答

```python
def parse_rows(lines):
    valid = []
    errors = []
    for line_no, line in enumerate(lines, start=1):
        parts = [part.strip() for part in line.split(',')]
        if len(parts) != 2:
            errors.append('第{}行：欄位數錯誤'.format(line_no))
            continue
        account, raw_amount = parts
        if not account:
            errors.append('第{}行：帳戶為空'.format(line_no))
            continue
        try:
            amount = float(raw_amount)
        except ValueError:
            errors.append('第{}行：金額錯誤'.format(line_no))
            continue
        valid.append((account, amount))
    return valid, errors
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

不要用裸 `except:`，否則可能吞掉 KeyboardInterrupt 或程式錯誤。

### 025. 使用 context manager 讀檔


#### 核心原理

`with open(...) as file` 透過 context manager 自動管理資源；離開區塊時一定呼叫 close。


#### Python 解答

```python
def count_nonempty_lines(path):
    count = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                count += 1
    return count
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

不要用 `file.readlines()` 處理大型檔案；逐行迭代較省記憶體。

### 026. 使用 deque 實作佇列


#### 核心原理

list 的 `pop(0)` 需要搬移其餘元素，為 O(n)。`collections.deque.popleft()` 是 O(1)。


#### Python 解答

```python
from collections import deque

def process_queue(items):
    queue = deque(items)
    processed = []
    while queue:
        processed.append(queue.popleft())
    return processed
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

若只是迭代而不需要動態加入，直接回傳 copy 更簡單；本題重點是理解 queue 操作。

### 027. 二分搜尋


#### 核心原理

每次比較中點並捨棄一半搜尋區間。使用閉區間 `[left,right]` 時，迴圈條件為 `left <=right`。


#### Python 解答

```python
def binary_search(numbers, target):
    left, right = (0, len(numbers) - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```


#### 複雜度

O(log n) 時間、O(1) 空間


#### 常見錯誤與延伸

二分搜尋前提是資料已排序；若每次查詢前都排序，總成本要把排序算進去。

### 028. 廣度優先搜尋 BFS


#### 核心原理

BFS 使用 queue，適合層級遍歷與無權重最短路徑。visited 應在入隊時標記，避免同一節點重複入隊。


#### Python 解答

```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```


#### 複雜度

O(V+E) 時間、O(V) 空間


#### 常見錯誤與延伸

若在出隊後才標記 visited，同一節點可能被多條邊重複放入 queue。

### 029. CSV 交易彙總


#### 核心原理

`csv.DictReader` 正確處理引號與逗號，比手動 split 安全。`utf-8-sig` 可移除 Excel 常見 BOM。


#### Python 解答

```python
u
def sum_csv(path):
    totals = defaultdict(float)
    with open(path, 'r', encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)
        required = {'account', 'amount'}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError('缺少必要欄位')
        for line_no, row in enumerate(reader, start=2):
            if not any((value or '').strip() for value in row.values()):
                continue
            account = (row['account'] or '').strip()
            try:
                amount = float(row['amount'])
            except (TypeError, ValueError):
                raise ValueError('第{}行金額錯誤'.format(line_no))
            if not account:
                raise ValueError('第{}行帳戶為空'.format(line_no))
            totals[account] += amount
    return dict(totals)
```


#### 複雜度

O(n) 時間、O(k) 空間


#### 常見錯誤與延伸

正式金融資料應改用 Decimal，並決定錯誤是整批失敗或隔離至錯誤檔。

### 030. JSON Schema 基礎驗證


#### 核心原理

JSON 解析成功不代表資料符合商業 schema。解析後仍需驗證容器型別、必要欄位與欄位型別。


#### Python 解答

```python
import json
import math

def parse_payment_json(payload):
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError('JSON 格式錯誤') from exc
    if not isinstance(data, dict):
        raise ValueError('最外層必須是物件')
    if not isinstance(data.get('customer_id'), str) or not data['customer_id']:
        raise ValueError('customer_id 錯誤')
    amount = data.get('amount')
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise ValueError('amount 型別錯誤')
    if not math.isfinite(amount) or amount < 0:
        raise ValueError('amount 值錯誤')
    if not isinstance(data.get('currency'), str) or not data['currency']:
        raise ValueError('currency 錯誤')
    return data
```


#### 複雜度

O(n) 時間與空間，n 為 JSON 長度


#### 常見錯誤與延伸

Python 的 bool 是 int 的子類別，因此要明確排除 `True` 被當成金額 1。

### 031. 正規表示式驗證 Email


#### 核心原理

`re.fullmatch()` 確保整個字串符合模式，避免只匹配前半段。此題是簡化規則，不等同完整 RFC 驗證。


#### Python 解答

```python
import re
EMAIL_RE = re.compile('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}')

def is_valid_email(email):
    return EMAIL_RE.fullmatch(email) is not None
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

不要自行宣稱此 regex 支援所有合法 Email；正式系統通常採成熟函式庫並搭配驗證信。

### 032. 計算工作日


#### 核心原理

日期以 `timedelta(days=1)` 逐日移動。`weekday()` 回傳 0=週一至 6=週日，值小於 5 為平日。


#### Python 解答

```python
from datetime import date, timedelta

def business_days(start, end, holidays):
    if end < start:
        raise ValueError('end 不可早於 start')
    count = 0
    current = start
    while current <= end:
        if current.weekday() < 5 and current not in holidays:
            count += 1
        current += timedelta(days=1)
    return count
```


#### 複雜度

O(日期跨度天數) 時間、O(1) 額外空間


#### 常見錯誤與延伸

跨時區的 timestamp 不應直接當本地日期；先明確轉換時區。

### 033. NumPy Min-Max 正規化


#### 核心原理

向量化運算一次作用於整個陣列。公式為 `(x-min)/(max-min)`；常數欄位分母為 0，需特別處理。


#### Python 解答

```python
import numpy as np

def minmax_scale(values):
    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError('只接受一維資料')
    if array.size == 0:
        return array.copy()
    minimum = array.min()
    maximum = array.max()
    if maximum == minimum:
        return np.zeros_like(array)
    return (array - minimum) / (maximum - minimum)
```


#### 複雜度

O(n) 時間、O(n) 輸出空間


#### 常見錯誤與延伸

模型正式上線時，min/max 必須只從訓練集估計，再套用到驗證與測試資料，避免資料洩漏。

### 034. NumPy 矩陣乘法與 shape


#### 核心原理

矩陣乘法要求內部維度一致。`@` 是矩陣乘法，`*` 是逐元素相乘。


#### Python 解答

```python
import numpy as np

def linear_scores(X, w, b):
    X = np.asarray(X, dtype=float)
    w = np.asarray(w, dtype=float)
    if X.ndim != 2 or w.ndim != 1:
        raise ValueError('X 必須二維、w 必須一維')
    if X.shape[1] != w.shape[0]:
        raise ValueError('特徵維度不一致')
    return X @ w + b
```


#### 複雜度

O(n·d) 時間、O(n) 輸出空間


#### 常見錯誤與延伸

廣播 broadcasting 雖方便，但 shape 錯誤有時不會立即報錯；關鍵介面應顯式驗證。

### 035. pandas 缺失值處理


#### 核心原理

數值中位數對離群值較穩健；不同欄位需依商業意義採不同策略。先 copy 可避免意外修改呼叫者資料。


#### Python 解答

```python
import pandas as pd

def clean_customers(df):
    required = {'age', 'income', 'city'}
    if not required.issubset(df.columns):
        raise ValueError('缺少必要欄位')
    result = df.copy()
    result['age'] = result['age'].fillna(result['age'].median())
    result = result.dropna(subset=['income'])
    result['city'] = result['city'].fillna('UNKNOWN')
    return result.reset_index(drop=True)
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

不能在切片上連鎖賦值，可能觸發 SettingWithCopy 問題；明確 copy 與欄位賦值較安全。

### 036. pandas 月交易彙總


#### 核心原理

先把 timestamp 轉成 datetime，再用 Period 月份鍵 groupby。聚合可同時計算 sum 與 size。


#### Python 解答

```python
import pandas as pd

def monthly_summary(df):
    required = {'account', 'timestamp', 'amount'}
    if not required.issubset(df.columns):
        raise ValueError('缺少必要欄位')
    data = df.copy()
    data['timestamp'] = pd.to_datetime(data['timestamp'], errors='raise')
    data['month'] = data['timestamp'].dt.to_period('M').astype(str)
    return data.groupby(['account', 'month'], as_index=False).agg(total_amount=('amount', 'sum'), tx_count=('amount', 'size')).sort_values(['account', 'month']).reset_index(drop=True)
```


#### 複雜度

O(n log n)（含排序）時間、O(n) 空間


#### 常見錯誤與延伸

`count` 會忽略缺失 amount，`size` 計算所有列；題目要交易筆數時通常 size 更明確。

### 037. pandas 合併客戶與交易


#### 核心原理

`merge(validate="many_to_one")` 可把資料關係假設轉成執行期檢查，避免主檔重複造成交易列爆增。


#### Python 解答

```python
import pandas as pd

def enrich_transactions(transactions, customers):
    result = transactions.merge(customers, on='customer_id', how='left', validate='many_to_one', indicator=True)
    result['customer_missing'] = result['_merge'].eq('left_only')
    return result.drop(columns='_merge')
```


#### 複雜度

平均 O(n+m) 至 O((n+m) log(n+m))，依 pandas 實作與排序而定


#### 常見錯誤與延伸

預設 merge 若主鍵重複可能產生笛卡兒放大；銀行資料管線應檢查鍵唯一性。

### 038. pandas 樞紐分析表


#### 核心原理

`pivot_table` 用於資料彙總與交叉表；`margins=True` 可加入總計。


#### Python 解答

```python
import pandas as pd

def branch_channel_pivot(df):
    return pd.pivot_table(df, index='branch', columns='channel', values='amount', aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
```


#### 複雜度

O(n) 以上時間、O(b·c) 輸出空間


#### 常見錯誤與延伸

樞紐表適合報表，但建模前通常要明確處理類別欄位與欄名。

### 039. SQLite 參數化查詢


#### 核心原理

參數化查詢把 SQL 結構與資料值分離，避免注入並正確處理跳脫。SQLite placeholder 為 `?`。


#### Python 解答

```python
def find_transactions(conn, account, min_amount):
    cursor = conn.execute('\n        SELECT id, account, amount, timestamp\n        FROM transactions\n        WHERE account =? AND amount >=?\n        ORDER BY timestamp ASC\n        ', (account, min_amount))
    return cursor.fetchall()
```


#### 複雜度

取決於索引；無索引最差 O(n)，有適當複合索引可大幅改善


#### 常見錯誤與延伸

參數化只能保護值，不能直接參數化欄名或排序方向；動態識別字需白名單。

### 040. 輸入白名單與 SQL 注入防護


#### 核心原理

SQL 的值可參數化，但欄名與關鍵字通常不能。對動態識別字要使用固定白名單映射，而非直接拼接任意輸入。


#### Python 解答

```python
def build_order_clause(field, direction):
    allowed_fields = {'timestamp': 'timestamp', 'amount': 'amount', 'account': 'account'}
    normalized_direction = direction.upper()
    if field not in allowed_fields:
        raise ValueError('不允許的排序欄位')
    if normalized_direction not in {'ASC', 'DESC'}:
        raise ValueError('不允許的排序方向')
    return 'ORDER BY {} {}'.format(allowed_fields[field], normalized_direction)
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

白名單內容必須由程式固定定義；不可把使用者輸入先『清理』後仍直接當 SQL 識別字。

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
