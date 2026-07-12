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


## 三、答案索引

共 **65 題**。

- [001. 型別轉換與交易金額驗證](#001-型別轉換與交易金額驗證)
- [002. 條件判斷：交易金額分級](#002-條件判斷：交易金額分級)
- [003. 複利計算](#003-複利計算)
- [004. 閏年判斷](#004-閏年判斷)
- [005. FizzBuzz 變形：規則標記](#005-fizzbuzz-變形：規則標記)
- [006. 一到 n 的總和](#006-一到-n-的總和)
- [007. 九九乘法表矩陣](#007-九九乘法表矩陣)
- [008. 質數判斷](#008-質數判斷)
- [009. 最大公因數與最小公倍數](#009-最大公因數與最小公倍數)
- [010. 反轉字串與回文判斷](#010-反轉字串與回文判斷)
- [011. 字元頻率統計](#011-字元頻率統計)
- [012. 空白正規化](#012-空白正規化)
- [013. 帳號遮罩](#013-帳號遮罩)
- [014. 密碼規則驗證](#014-密碼規則驗證)
- [015. 保留順序去除重複值](#015-保留順序去除重複值)
- [016. 第二大不重複值](#016-第二大不重複值)
- [017. Two Sum](#017-two-sum)
- [018. 串列右旋](#018-串列右旋)
- [019. 合併兩個已排序串列](#019-合併兩個已排序串列)
- [020. Top-K 高頻項目](#020-top-k-高頻項目)
- [021. 集合交集與差集](#021-集合交集與差集)
- [022. 依帳戶彙總交易](#022-依帳戶彙總交易)
- [023. 展平巢狀字典](#023-展平巢狀字典)
- [024. 串列生成式篩選](#024-串列生成式篩選)
- [025. 可變預設參數陷阱](#025-可變預設參數陷阱)
- [026. *args 與 **kwargs 費用計算器](#026-*args-與-**kwargs-費用計算器)
- [027. 多欄位排序](#027-多欄位排序)
- [028. 費波那契數列與記憶化](#028-費波那契數列與記憶化)
- [029. 安全解析交易列](#029-安全解析交易列)
- [030. 使用 context manager 讀檔](#030-使用-context-manager-讀檔)
- [031. BankAccount 類別](#031-bankaccount-類別)
- [032. 使用 deque 實作佇列](#032-使用-deque-實作佇列)
- [033. 括號配對](#033-括號配對)
- [034. 二分搜尋](#034-二分搜尋)
- [035. 線性搜尋與比較](#035-線性搜尋與比較)
- [036. 氣泡排序](#036-氣泡排序)
- [037. 插入排序](#037-插入排序)
- [038. 合併排序](#038-合併排序)
- [039. 快速排序](#039-快速排序)
- [040. 廣度優先搜尋 BFS](#040-廣度優先搜尋-bfs)
- [041. 深度優先搜尋 DFS](#041-深度優先搜尋-dfs)
- [042. 無權重最短路徑](#042-無權重最短路徑)
- [043. 以 heap 取得前 K 大值](#043-以-heap-取得前-k-大值)
- [044. 固定長度滑動視窗最大總和](#044-固定長度滑動視窗最大總和)
- [045. 雙指標移除重複值](#045-雙指標移除重複值)
- [046. 前綴和區間查詢](#046-前綴和區間查詢)
- [047. 和為 K 的子陣列數量](#047-和為-k-的子陣列數量)
- [048. CSV 交易彙總](#048-csv-交易彙總)
- [049. JSON Schema 基礎驗證](#049-json-schema-基礎驗證)
- [050. 正規表示式驗證 Email](#050-正規表示式驗證-email)
- [051. 計算工作日](#051-計算工作日)
- [052. NumPy Min-Max 正規化](#052-numpy-min-max-正規化)
- [053. NumPy 矩陣乘法與 shape](#053-numpy-矩陣乘法與-shape)
- [054. pandas 缺失值處理](#054-pandas-缺失值處理)
- [055. pandas 月交易彙總](#055-pandas-月交易彙總)
- [056. pandas 合併客戶與交易](#056-pandas-合併客戶與交易)
- [057. pandas 樞紐分析表](#057-pandas-樞紐分析表)
- [058. SQLite 參數化查詢](#058-sqlite-參數化查詢)
- [059. Generator 分批處理](#059-generator-分批處理)
- [060. Decorator 記錄執行時間](#060-decorator-記錄執行時間)
- [061. 單元測試：parse_amount](#061-單元測試：parse_amount)
- [062. 密碼安全雜湊](#062-密碼安全雜湊)
- [063. 輸入白名單與 SQL 注入防護](#063-輸入白名單與-sql-注入防護)
- [064. Big-O 優化：重複會員查找](#064-big-o-優化：重複會員查找)
- [065. dataclass 交易資料模型](#065-dataclass-交易資料模型)


---

## 四、詳細解答


### 001. 型別轉換與交易金額驗證


#### 核心原理

Python 的 `float` 採二進位浮點表示，某些十進位小數無法精確表示。金融金額通常使用 `Decimal`，
並從字串建立數值。驗證時需同時檢查有限值、正負號與量化規則。


#### Python 解答

```python
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def parse_amount(value) -> Decimal:
    try:
        amount = Decimal(str(value).strip())
    except (InvalidOperation, AttributeError):
        raise ValueError("金額格式錯誤")
    if not amount.is_finite() or amount < 0:
        raise ValueError("金額必須是有限的非負數")
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

不要寫 `Decimal(0.1)`；這會先產生不精確的 float。應寫 `Decimal("0.1")`。
此外，`Decimal("NaN")` 不會在建構時失敗，所以仍要呼叫 `is_finite()`。


### 002. 條件判斷：交易金額分級


#### 核心原理

多分支條件應由最嚴格或最小邊界依序判斷，並明確處理等號。考試常藉 9,999、10,000、99,999、100,000
測試 off-by-one 錯誤。


#### Python 解答

```python
def risk_band(amount: float) -> str:
    if amount < 0:
        raise ValueError("金額不可為負")
    if amount < 10_000:
        return "LOW"
    if amount < 100_000:
        return "MEDIUM"
    return "HIGH"
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

邊界值要逐一測試；不要把第二段誤寫成 `amount <= 100000`。


### 003. 複利計算


#### 核心原理

這題考參數驗證、預設參數與公式轉換。年利率應以小數表示，例如 2% 寫成 0.02。


#### Python 解答

```python
def compound(principal: float, annual_rate: float, years: int, times_per_year: int = 12) -> float:
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("本金、利率與年數不可為負")
    if times_per_year <= 0:
        raise ValueError("每年複利次數必須大於 0")
    value = principal * (1 + annual_rate / times_per_year) ** (times_per_year * years)
    return round(value, 2)
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

題目若要求金融級精度，應改用 Decimal；本題重點是公式與控制流程。


### 004. 閏年判斷


#### 核心原理

複合條件要理解運算優先序。標準表示式是 `(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)`。


#### Python 解答

```python
def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

只判斷 `% 4 == 0` 會把 1900 錯判成閏年。


### 005. FizzBuzz 變形：規則標記


#### 核心原理

應先判斷同時整除的情況，或用字串累加，避免 15 只得到 A。


#### Python 解答

```python
def rule_tags(n: int) -> list[str]:
    if n < 1:
        return []
    result = []
    for i in range(1, n + 1):
        tag = ""
        if i % 3 == 0:
            tag += "A"
        if i % 5 == 0:
            tag += "B"
        result.append(tag or str(i))
    return result
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

迴圈範圍要使用 `range(1, n + 1)`，否則會漏掉 n。


### 006. 一到 n 的總和


#### 核心原理

迴圈法逐項累加為 O(n)；等差級數公式 `n(n+1)/2` 為 O(1)。此題常用來測試能否辨識演算法優化。


#### Python 解答

```python
def sum_loop(n: int) -> int:
    if n < 0:
        raise ValueError("n 不可為負")
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_formula(n: int) -> int:
    if n < 0:
        raise ValueError("n 不可為負")
    return n * (n + 1) // 2
```


#### 複雜度

迴圈法 O(n)；公式法 O(1)；兩者額外空間皆 O(1)


#### 常見錯誤與延伸

`/` 會得到 float；整數總和應使用 `//`。


### 007. 九九乘法表矩陣


#### 核心原理

巢狀迴圈對應二維資料。建立每一列時要產生新的 list，避免多列共享同一參考。


#### Python 解答

```python
def multiplication_table(n: int) -> list[list[int]]:
    if n <= 0:
        raise ValueError("n 必須大於 0")
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
```


#### 複雜度

O(n²) 時間、O(n²) 輸出空間


#### 常見錯誤與延伸

不要使用 `[[0] * n] * n` 後再修改元素；這會讓各列指向同一個串列。


### 008. 質數判斷


#### 核心原理

若 n 有大於平方根的因數，必定也有一個小於平方根的配對因數。因此檢查到 `isqrt(n)` 即可。


#### Python 解答

```python
from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for factor in range(3, isqrt(n) + 1, 2):
        if n % factor == 0:
            return False
    return True
```


#### 複雜度

O(√n) 時間、O(1) 空間


#### 常見錯誤與延伸

上界要加 1，否則完全平方數如 49 可能漏掉因數 7。


### 009. 最大公因數與最小公倍數


#### 核心原理

輾轉相除法反覆令 `(a,b)=(b,a%b)`，直到 b 為 0。LCM 可由 `abs(a*b)//gcd(a,b)` 得到，
但先除再乘可減少中間數值。


#### Python 解答

```python
def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)
```


#### 複雜度

O(log(min(|a|,|b|))) 時間、O(1) 空間


#### 常見錯誤與延伸

若 a=b=0，gcd 定義依題目而定；本解回傳 0。


### 010. 反轉字串與回文判斷


#### 核心原理

可先以 `isalnum()` 過濾，配合 `casefold()` 做較完整的大小寫正規化，再與反轉字串比較。


#### Python 解答

```python
def is_palindrome(text: str) -> bool:
    normalized = "".join(ch.casefold() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

`lower()` 對多數英文足夠；`casefold()` 對 Unicode 大小寫處理更完整。


### 011. 字元頻率統計


#### 核心原理

雜湊表可在平均 O(1) 時間更新計數。`collections.Counter` 是 Python 的標準計數工具。


#### Python 解答

```python
from collections import Counter

def char_frequency(text: str) -> dict[str, int]:
    return dict(Counter(ch.casefold() for ch in text if not ch.isspace()))
```


#### 複雜度

O(n) 時間、O(k) 空間，k 為不同字元數


#### 常見錯誤與延伸

題目若要求保留標點，不能使用 `isalnum()` 過濾；此題只忽略空白。


### 012. 空白正規化


#### 核心原理

不帶參數的 `split()` 會把所有 Unicode 空白視為分隔符並忽略連續空白；再用單一空格 join。


#### Python 解答

```python
def normalize_spaces(text: str) -> str:
    return " ".join(text.split())
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

`split()` 只處理一般空格，且會保留空字串，不適合本題。


### 013. 帳號遮罩


#### 核心原理

遮罩是最基本的資料最小揭露。切片 `account[-visible:]` 在 visible=0 時會出現 `-0 == 0` 的陷阱，
因此要單獨處理。


#### Python 解答

```python
def mask_account(account: str, visible: int = 4) -> str:
    if visible < 0:
        raise ValueError("visible 不可為負")
    if len(account) <= visible:
        return account
    if visible == 0:
        return "*" * len(account)
    return "*" * (len(account) - visible) + account[-visible:]
```


#### 複雜度

O(n) 時間、O(n) 輸出空間


#### 常見錯誤與延伸

遮罩不等於加密；原始敏感資料仍需受到存取控制與安全儲存保護。


### 014. 密碼規則驗證


#### 核心原理

`any()` 適合表達「至少有一個」。回傳失敗原因比只回傳布林值更利於測試與使用者提示。


#### Python 解答

```python
def validate_password(password: str) -> tuple[bool, list[str]]:
    errors = []
    if len(password) < 10:
        errors.append("長度至少 10")
    if not any(ch.isupper() for ch in password):
        errors.append("缺少大寫字母")
    if not any(ch.islower() for ch in password):
        errors.append("缺少小寫字母")
    if not any(ch.isdigit() for ch in password):
        errors.append("缺少數字")
    if not any(not ch.isalnum() for ch in password):
        errors.append("缺少特殊字元")
    return not errors, errors
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

實務上密碼規則不能取代 MFA、雜湊與登入速率限制。


### 015. 保留順序去除重複值


#### 核心原理

使用 set 記錄已看過的元素，可把雙層搜尋的 O(n²) 降到平均 O(n)。


#### Python 解答

```python
def deduplicate(items: list) -> list:
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


### 016. 第二大不重複值


#### 核心原理

維護 largest 與 second 兩個狀態即可單次掃描。遇到等於最大值的元素不應更新第二大。


#### Python 解答

```python
def second_largest(numbers: list[float]) -> float:
    largest = None
    second = None
    for value in numbers:
        if largest is None or value > largest:
            if value != largest:
                second = largest
                largest = value
        elif value != largest and (second is None or value > second):
            second = value
    if second is None:
        raise ValueError("不足兩個不同值")
    return second
```


#### 複雜度

O(n) 時間、O(1) 空間


#### 常見錯誤與延伸

使用 `sorted(set(numbers))[-2]` 雖簡潔，但時間為 O(n log n) 且使用 O(n) 空間。


### 017. Two Sum


#### 核心原理

掃描到 value 時，查找 `target-value` 是否已出現。先查後存可避免同一索引被使用兩次。


#### Python 解答

```python
def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    seen = {}
    for i, value in enumerate(numbers):
        needed = target - value
        if needed in seen:
            return seen[needed], i
        seen[value] = i
    return None
```


#### 複雜度

平均 O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

若題目要求所有組合或數值而非索引，資料結構與去重策略會不同。


### 018. 串列右旋


#### 核心原理

以 `k %= n` 把位移縮至 0..n-1。Python 的負數取模也會得到非負結果，因此自然支援負 k。


#### Python 解答

```python
def rotate_right(items: list, k: int) -> list:
    if not items:
        return []
    k %= len(items)
    if k == 0:
        return items.copy()
    return items[-k:] + items[:-k]
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

空串列不可做 `k % len(items)`，必須先處理。


### 019. 合併兩個已排序串列


#### 核心原理

雙指標比較兩串列目前元素，把較小者加入結果；其中一方耗盡後追加另一方剩餘元素。


#### Python 解答

```python
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```


#### 複雜度

O(n+m) 時間、O(n+m) 輸出空間


#### 常見錯誤與延伸

若用 `pop(0)`，每次移動串列元素可能使總時間退化。


### 020. Top-K 高頻項目


#### 核心原理

先計數，再排序不同項目。若不同項目數極大且 k 很小，可用 heap 將排序成本由 O(u log u) 降為 O(u log k)。


#### Python 解答

```python
from collections import Counter

def top_k_frequent(items: list[str], k: int) -> list[tuple[str, int]]:
    if k < 0:
        raise ValueError("k 不可為負")
    counts = Counter(items)
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ranked[:k]
```


#### 複雜度

O(n + u log u) 時間、O(u) 空間，u 為不同項目數


#### 常見錯誤與延伸

`Counter.most_common()` 對同次數項目的次序不一定符合題目指定，因此本題明確自訂排序鍵。


### 021. 集合交集與差集


#### 核心原理

集合交集 `&` 與差集 `-` 可直接表達需求；最後排序確保輸出穩定。


#### Python 解答

```python
def compare_customers(a: list[int], b: list[int]) -> tuple[list[int], list[int], list[int]]:
    sa, sb = set(a), set(b)
    return sorted(sa & sb), sorted(sa - sb), sorted(sb - sa)
```


#### 複雜度

O(n+m + u log u) 時間、O(n+m) 空間


#### 常見錯誤與延伸

set 會移除重複值；若重複次數有意義，應使用 Counter 而非 set。


### 022. 依帳戶彙總交易


#### 核心原理

`defaultdict` 能省略鍵不存在時的初始化。金融題目若要求精確金額，amount 應換成 Decimal。


#### Python 解答

```python
from collections import defaultdict

def aggregate_by_account(records: list[tuple[str, float]]) -> dict[str, float]:
    totals = defaultdict(float)
    for account, amount in records:
        if not account:
            raise ValueError("帳戶不可為空")
        totals[account] += amount
    return dict(totals)
```


#### 複雜度

O(n) 時間、O(k) 空間


#### 常見錯誤與延伸

若使用 float，累加可能有精度誤差；實務可將金額轉為最小貨幣單位整數或 Decimal。


### 023. 展平巢狀字典


#### 核心原理

遞迴函式需要攜帶目前路徑。只對非空 dict 繼續展開，避免空 dict 消失。


#### Python 解答

```python
def flatten_dict(data: dict, sep: str = ".") -> dict:
    result = {}

    def walk(value, prefix):
        if isinstance(value, dict) and value:
            for key, child in value.items():
                next_key = f"{prefix}{sep}{key}" if prefix else str(key)
                walk(child, next_key)
        else:
            result[prefix] = value

    walk(data, "")
    return result
```


#### 複雜度

O(n) 時間、O(d) 遞迴堆疊，n 為節點數、d 為深度


#### 常見錯誤與延伸

極深資料可能觸發遞迴深度限制；若輸入不可信，可改用顯式 stack。


### 024. 串列生成式篩選


#### 核心原理

串列生成式適合簡單的一對一轉換與篩選。若條件過多，傳統迴圈可讀性更好。


#### Python 解答

```python
def filtered_squares(amounts: list[int], threshold: int) -> list[int]:
    return [value * value for value in amounts if value > 0 and value >= threshold]
```


#### 複雜度

O(n) 時間、O(k) 輸出空間


#### 常見錯誤與延伸

不要為了炫技把複雜商業規則塞進一行生成式。


### 025. 可變預設參數陷阱


#### 核心原理

預設參數只在函式定義時求值一次。可變物件會跨呼叫保留內容，應使用 `None` 作為 sentinel，
在函式內建立新串列。


#### Python 解答

```python
def add_alert(alert: str, alerts: list[str] | None = None) -> list[str]:
    if alerts is None:
        alerts = []
    alerts.append(alert)
    return alerts
```


#### 複雜度

O(1) 攤銷時間；回傳串列空間依既有內容而定


#### 常見錯誤與延伸

若呼叫者傳入現有 list，本函式會原地修改；若不希望副作用，先做 `alerts = list(alerts or [])`。


### 026. *args 與 **kwargs 費用計算器


#### 核心原理

`*args` 收集位置參數為 tuple，`**kwargs` 收集具名參數為 dict。具名-only 參數 discount 放在 `*fees` 後。


#### Python 解答

```python
def total_fee(*fees: float, discount: float = 0, **taxes: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("discount 必須介於 0 與 1")
    if any(value < 0 for value in (*fees, *taxes.values())):
        raise ValueError("費用不可為負")
    return sum(fees) * (1 - discount) + sum(taxes.values())
```


#### 複雜度

O(n+m) 時間、O(n+m) 參數收集空間


#### 常見錯誤與延伸

`**taxes` 的鍵只作名稱，真正加總的是 values。


### 027. 多欄位排序


#### 核心原理

`sorted()` 回傳新串列。對數字可取負值實現遞減排序；tuple key 會由左至右比較。


#### Python 解答

```python
def sort_transactions(records: list[dict]) -> list[dict]:
    return sorted(
        records,
        key=lambda row: (-row["risk"], -row["amount"], row["id"])
    )
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

若欄位可能缺失，應先做 schema 驗證，不要讓 KeyError 在排序中才發生。


### 028. 費波那契數列與記憶化


#### 核心原理

樸素遞迴重複計算相同子問題，時間近 O(2^n)。迭代只保留前兩項，時間 O(n)、空間 O(1)。


#### Python 解答

```python
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n 不可為負")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```


#### 複雜度

O(n) 時間、O(1) 空間


#### 常見錯誤與延伸

更新時要使用 tuple assignment；若先改 a 再算 b，可能使用到新值造成錯誤。


### 029. 安全解析交易列


#### 核心原理

批次資料處理通常採「逐筆驗證、錯誤隔離」。例外範圍要小，只包住真正可能失敗的轉換。


#### Python 解答

```python
def parse_rows(lines: list[str]) -> tuple[list[tuple[str, float]], list[str]]:
    valid = []
    errors = []
    for line_no, line in enumerate(lines, start=1):
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 2:
            errors.append(f"第{line_no}行：欄位數錯誤")
            continue
        account, raw_amount = parts
        if not account:
            errors.append(f"第{line_no}行：帳戶為空")
            continue
        try:
            amount = float(raw_amount)
        except ValueError:
            errors.append(f"第{line_no}行：金額錯誤")
            continue
        valid.append((account, amount))
    return valid, errors
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

不要用裸 `except:`，否則可能吞掉 KeyboardInterrupt 或程式錯誤。


### 030. 使用 context manager 讀檔


#### 核心原理

`with open(...) as file` 透過 context manager 自動管理資源；離開區塊時一定呼叫 close。


#### Python 解答

```python
def count_nonempty_lines(path: str) -> int:
    count = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                count += 1
    return count
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

不要用 `file.readlines()` 處理大型檔案；逐行迭代較省記憶體。


### 031. BankAccount 類別


#### 核心原理

封裝讓物件自行維護不變條件（invariant），例如餘額不可為負。以 property 暴露唯讀值，
避免外部直接修改內部狀態。


#### Python 解答

```python
class BankAccount:
    def __init__(self, account_id: str, opening_balance: float = 0) -> None:
        if not account_id:
            raise ValueError("account_id 不可為空")
        if opening_balance < 0:
            raise ValueError("期初餘額不可為負")
        self._account_id = account_id
        self._balance = opening_balance

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("存款必須大於 0")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("提款必須大於 0")
        if amount > self._balance:
            raise ValueError("餘額不足")
        self._balance -= amount
```


#### 複雜度

每次存提款 O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

實際銀行帳務還需要交易一致性、鎖定、日誌與 Decimal；單一記憶體物件不等於正式帳務系統。


### 032. 使用 deque 實作佇列


#### 核心原理

list 的 `pop(0)` 需要搬移其餘元素，為 O(n)。`collections.deque.popleft()` 是 O(1)。


#### Python 解答

```python
from collections import deque

def process_queue(items: list[str]) -> list[str]:
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


### 033. 括號配對


#### 核心原理

遇到左括號推入 stack；遇到右括號時檢查 stack 頂端是否為對應左括號。


#### Python 解答

```python
def is_balanced(expression: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in expression:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

最後必須確認 stack 為空，否則 `(((` 會被錯判。


### 034. 二分搜尋


#### 核心原理

每次比較中點並捨棄一半搜尋區間。使用閉區間 `[left,right]` 時，迴圈條件為 `left <= right`。


#### Python 解答

```python
def binary_search(numbers: list[int], target: int) -> int:
    left, right = 0, len(numbers) - 1
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


### 035. 線性搜尋與比較


#### 核心原理

線性搜尋不要求排序，適合資料量小、只查一次、或資料無法比較排序的情境。
二分搜尋雖快，但需要已排序或先支付排序成本。


#### Python 解答

```python
def linear_search(items: list, target) -> int:
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1
```


#### 複雜度

O(n) 時間、O(1) 空間


#### 常見錯誤與延伸

不要一律認為 O(log n) 比 O(n) 好；資料前處理與使用次數也會影響整體成本。


### 036. 氣泡排序


#### 核心原理

氣泡排序每輪把最大值推到右端。`swapped` 可讓已排序輸入最佳情況降為 O(n)。


#### Python 解答

```python
def bubble_sort(items: list[int]) -> list[int]:
    result = items.copy()
    n = len(result)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result
```


#### 複雜度

平均/最差 O(n²)，最佳 O(n)；O(n) 輸出 copy


#### 常見錯誤與延伸

正式系統通常使用內建 Timsort；本題是理解排序機制，不是建議實務採氣泡排序。


### 037. 插入排序


#### 核心原理

插入排序把當前值插入左側已排序區間。若資料近乎有序，移動次數少，表現可接近 O(n)。


#### Python 解答

```python
def insertion_sort(items: list[int]) -> list[int]:
    result = items.copy()
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result
```


#### 複雜度

平均/最差 O(n²)，最佳 O(n)；O(n) 輸出 copy


#### 常見錯誤與延伸

不要在 while 內只交換卻忘記更新 j，否則可能無窮迴圈。


### 038. 合併排序


#### 核心原理

合併排序把問題分成兩半，遞迴排序後線性合併。時間穩定為 O(n log n)，但需要額外空間。


#### Python 解答

```python
def merge_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items.copy()
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```


#### 複雜度

O(n log n) 時間、O(n) 輔助空間，另有 O(log n) 遞迴深度


#### 常見錯誤與延伸

切片本身會建立新串列；若追求低配置，可用索引區間實作。


### 039. 快速排序


#### 核心原理

選 pivot 後分成小於、等於、大於三組，遞迴處理兩側。平均 O(n log n)，若 pivot 每次極端不平衡則最差 O(n²)。


#### Python 解答

```python
def quick_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items.copy()
    pivot = items[len(items) // 2]
    lower = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    higher = [x for x in items if x > pivot]
    return quick_sort(lower) + equal + quick_sort(higher)
```


#### 複雜度

平均 O(n log n)、最差 O(n²)；此版本 O(n) 以上額外空間


#### 常見錯誤與延伸

若只分 `< pivot` 與 `>= pivot`，大量重複值可能造成嚴重不平衡。


### 040. 廣度優先搜尋 BFS


#### 核心原理

BFS 使用 queue，適合層級遍歷與無權重最短路徑。visited 應在入隊時標記，避免同一節點重複入隊。


#### Python 解答

```python
from collections import deque

def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
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


### 041. 深度優先搜尋 DFS


#### 核心原理

stack 為 LIFO。若希望第一個鄰居先拜訪，推入 stack 時需反向迭代鄰居。


#### Python 解答

```python
def dfs(graph: dict[str, list[str]], start: str) -> list[str]:
    stack = [start]
    visited = set()
    order = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return order
```


#### 複雜度

O(V+E) 時間、O(V) 空間


#### 常見錯誤與延伸

DFS 不保證無權重圖的最短路徑；最短邊數通常用 BFS。


### 042. 無權重最短路徑


#### 核心原理

BFS 第一次到達節點時即得到最短邊數。用 parent map 記錄前驅，抵達 end 後反向重建路徑。


#### Python 解答

```python
from collections import deque

def shortest_path(graph: dict[str, list[str]], start: str, end: str) -> list[str]:
    if start == end:
        return [start]
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor in parent:
                continue
            parent[neighbor] = node
            if neighbor == end:
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]
            queue.append(neighbor)
    return []
```


#### 複雜度

O(V+E) 時間、O(V) 空間


#### 常見錯誤與延伸

有權重圖不可直接用 BFS；非負權重通常用 Dijkstra。


### 043. 以 heap 取得前 K 大值


#### 核心原理

維護大小最多 k 的 min-heap，掃描每個值。heap 頂端是目前前 k 大中的最小值。


#### Python 解答

```python
import heapq

def largest_k(numbers: list[int], k: int) -> list[int]:
    if k < 0:
        raise ValueError("k 不可為負")
    if k == 0:
        return []
    heap = []
    for value in numbers:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return sorted(heap, reverse=True)
```


#### 複雜度

O(n log k + k log k) 時間、O(k) 空間


#### 常見錯誤與延伸

若 k 接近 n，直接排序可能更簡單；演算法選擇要看 n 與 k 的比例。


### 044. 固定長度滑動視窗最大總和


#### 核心原理

先計算第一個視窗，再每次加進右端、扣掉離開左端的元素，避免每個視窗重算 O(k)。


#### Python 解答

```python
def max_window_sum(numbers: list[int], k: int) -> int:
    if k <= 0 or k > len(numbers):
        raise ValueError("k 範圍錯誤")
    current = sum(numbers[:k])
    best = current
    for right in range(k, len(numbers)):
        current += numbers[right] - numbers[right - k]
        best = max(best, current)
    return best
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

不能把 best 初始化為 0，否則全負數輸入會得到錯誤答案。


### 045. 雙指標移除重複值


#### 核心原理

慢指標指向最後一個唯一值，快指標掃描新值。因資料已排序，相同值相鄰。


#### Python 解答

```python
def remove_duplicates_sorted(numbers: list[int]) -> int:
    if not numbers:
        return 0
    write = 1
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write - 1]:
            numbers[write] = numbers[read]
            write += 1
    return write
```


#### 複雜度

O(n) 時間、O(1) 空間


#### 常見錯誤與延伸

題目只保證前 k 個有效；k 之後的舊值不必清除。


### 046. 前綴和區間查詢


#### 核心原理

令 prefix[0]=0，prefix[i+1] 為前 i+1 項總和，則區間 [l,r] 為 `prefix[r+1]-prefix[l]`。


#### Python 解答

```python
def build_prefix(numbers: list[int]) -> list[int]:
    prefix = [0]
    for value in numbers:
        prefix.append(prefix[-1] + value)
    return prefix

def range_sum(prefix: list[int], left: int, right: int) -> int:
    n = len(prefix) - 1
    if left < 0 or right < left or right >= n:
        raise IndexError("區間索引錯誤")
    return prefix[right + 1] - prefix[left]
```


#### 複雜度

建表 O(n)，每次查詢 O(1)；空間 O(n)


#### 常見錯誤與延伸

prefix 長度應為原資料長度加 1，能簡化 left=0 的邊界。


### 047. 和為 K 的子陣列數量


#### 核心原理

若目前前綴和為 s，先前出現過 `s-k`，則兩者之間子陣列和為 k。用 dict 計數前綴和出現次數。


#### Python 解答

```python
from collections import defaultdict

def count_subarrays_sum(numbers: list[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    prefix = 0
    result = 0
    for value in numbers:
        prefix += value
        result += counts[prefix - k]
        counts[prefix] += 1
    return result
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

滑動視窗不適合含負數的任意和問題，因視窗和不具單調性。


### 048. CSV 交易彙總


#### 核心原理

`csv.DictReader` 正確處理引號與逗號，比手動 split 安全。`utf-8-sig` 可移除 Excel 常見 BOM。


#### Python 解答

```python
import csv
from collections import defaultdict

def sum_csv(path: str) -> dict[str, float]:
    totals = defaultdict(float)
    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = {"account", "amount"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("缺少必要欄位")
        for line_no, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue
            account = (row["account"] or "").strip()
            try:
                amount = float(row["amount"])
            except (TypeError, ValueError):
                raise ValueError(f"第{line_no}行金額錯誤")
            if not account:
                raise ValueError(f"第{line_no}行帳戶為空")
            totals[account] += amount
    return dict(totals)
```


#### 複雜度

O(n) 時間、O(k) 空間


#### 常見錯誤與延伸

正式金融資料應改用 Decimal，並決定錯誤是整批失敗或隔離至錯誤檔。


### 049. JSON Schema 基礎驗證


#### 核心原理

JSON 解析成功不代表資料符合商業 schema。解析後仍需驗證容器型別、必要欄位與欄位型別。


#### Python 解答

```python
import json
import math

def parse_payment_json(payload: str) -> dict:
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError("JSON 格式錯誤") from exc
    if not isinstance(data, dict):
        raise ValueError("最外層必須是物件")
    if not isinstance(data.get("customer_id"), str) or not data["customer_id"]:
        raise ValueError("customer_id 錯誤")
    amount = data.get("amount")
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise ValueError("amount 型別錯誤")
    if not math.isfinite(amount) or amount < 0:
        raise ValueError("amount 值錯誤")
    if not isinstance(data.get("currency"), str) or not data["currency"]:
        raise ValueError("currency 錯誤")
    return data
```


#### 複雜度

O(n) 時間與空間，n 為 JSON 長度


#### 常見錯誤與延伸

Python 的 bool 是 int 的子類別，因此要明確排除 `True` 被當成金額 1。


### 050. 正規表示式驗證 Email


#### 核心原理

`re.fullmatch()` 確保整個字串符合模式，避免只匹配前半段。此題是簡化規則，不等同完整 RFC 驗證。


#### Python 解答

```python
import re

EMAIL_RE = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

def is_valid_email(email: str) -> bool:
    return EMAIL_RE.fullmatch(email) is not None
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

不要自行宣稱此 regex 支援所有合法 Email；正式系統通常採成熟函式庫並搭配驗證信。


### 051. 計算工作日


#### 核心原理

日期以 `timedelta(days=1)` 逐日移動。`weekday()` 回傳 0=週一至 6=週日，值小於 5 為平日。


#### Python 解答

```python
from datetime import date, timedelta

def business_days(start: date, end: date, holidays: set[date]) -> int:
    if end < start:
        raise ValueError("end 不可早於 start")
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


### 052. NumPy Min-Max 正規化


#### 核心原理

向量化運算一次作用於整個陣列。公式為 `(x-min)/(max-min)`；常數欄位分母為 0，需特別處理。


#### Python 解答

```python
import numpy as np

def minmax_scale(values):
    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError("只接受一維資料")
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


### 053. NumPy 矩陣乘法與 shape


#### 核心原理

矩陣乘法要求內部維度一致。`@` 是矩陣乘法，`*` 是逐元素相乘。


#### Python 解答

```python
import numpy as np

def linear_scores(X, w, b: float):
    X = np.asarray(X, dtype=float)
    w = np.asarray(w, dtype=float)
    if X.ndim != 2 or w.ndim != 1:
        raise ValueError("X 必須二維、w 必須一維")
    if X.shape[1] != w.shape[0]:
        raise ValueError("特徵維度不一致")
    return X @ w + b
```


#### 複雜度

O(n·d) 時間、O(n) 輸出空間


#### 常見錯誤與延伸

廣播 broadcasting 雖方便，但 shape 錯誤有時不會立即報錯；關鍵介面應顯式驗證。


### 054. pandas 缺失值處理


#### 核心原理

數值中位數對離群值較穩健；不同欄位需依商業意義採不同策略。先 copy 可避免意外修改呼叫者資料。


#### Python 解答

```python
import pandas as pd

def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    required = {"age", "income", "city"}
    if not required.issubset(df.columns):
        raise ValueError("缺少必要欄位")
    result = df.copy()
    result["age"] = result["age"].fillna(result["age"].median())
    result = result.dropna(subset=["income"])
    result["city"] = result["city"].fillna("UNKNOWN")
    return result.reset_index(drop=True)
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

不能在切片上連鎖賦值，可能觸發 SettingWithCopy 問題；明確 copy 與欄位賦值較安全。


### 055. pandas 月交易彙總


#### 核心原理

先把 timestamp 轉成 datetime，再用 Period 月份鍵 groupby。聚合可同時計算 sum 與 size。


#### Python 解答

```python
import pandas as pd

def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    required = {"account", "timestamp", "amount"}
    if not required.issubset(df.columns):
        raise ValueError("缺少必要欄位")
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    data["month"] = data["timestamp"].dt.to_period("M").astype(str)
    return (
        data.groupby(["account", "month"], as_index=False)
        .agg(total_amount=("amount", "sum"), tx_count=("amount", "size"))
        .sort_values(["account", "month"])
        .reset_index(drop=True)
    )
```


#### 複雜度

O(n log n)（含排序）時間、O(n) 空間


#### 常見錯誤與延伸

`count` 會忽略缺失 amount，`size` 計算所有列；題目要交易筆數時通常 size 更明確。


### 056. pandas 合併客戶與交易


#### 核心原理

`merge(validate="many_to_one")` 可把資料關係假設轉成執行期檢查，避免主檔重複造成交易列爆增。


#### Python 解答

```python
import pandas as pd

def enrich_transactions(transactions: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    result = transactions.merge(
        customers,
        on="customer_id",
        how="left",
        validate="many_to_one",
        indicator=True
    )
    result["customer_missing"] = result["_merge"].eq("left_only")
    return result.drop(columns="_merge")
```


#### 複雜度

平均 O(n+m) 至 O((n+m) log(n+m))，依 pandas 實作與排序而定


#### 常見錯誤與延伸

預設 merge 若主鍵重複可能產生笛卡兒放大；銀行資料管線應檢查鍵唯一性。


### 057. pandas 樞紐分析表


#### 核心原理

`pivot_table` 用於資料彙總與交叉表；`margins=True` 可加入總計。


#### Python 解答

```python
import pandas as pd

def branch_channel_pivot(df: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(
        df,
        index="branch",
        columns="channel",
        values="amount",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="TOTAL"
    )
```


#### 複雜度

O(n) 以上時間、O(b·c) 輸出空間


#### 常見錯誤與延伸

樞紐表適合報表，但建模前通常要明確處理類別欄位與欄名。


### 058. SQLite 參數化查詢


#### 核心原理

參數化查詢把 SQL 結構與資料值分離，避免注入並正確處理跳脫。SQLite placeholder 為 `?`。


#### Python 解答

```python
def find_transactions(conn, account: str, min_amount: float) -> list[tuple]:
    cursor = conn.execute(
        '''
        SELECT id, account, amount, timestamp
        FROM transactions
        WHERE account = ? AND amount >= ?
        ORDER BY timestamp ASC
        ''',
        (account, min_amount)
    )
    return cursor.fetchall()
```


#### 複雜度

取決於索引；無索引最差 O(n)，有適當複合索引可大幅改善


#### 常見錯誤與延伸

參數化只能保護值，不能直接參數化欄名或排序方向；動態識別字需白名單。


### 059. Generator 分批處理


#### 核心原理

generator 只在需要時產生下一批，可處理無法一次放入記憶體的大型資料流。


#### Python 解答

```python
from itertools import islice

def chunks(iterable, size: int):
    if size <= 0:
        raise ValueError("size 必須大於 0")
    iterator = iter(iterable)
    while True:
        batch = list(islice(iterator, size))
        if not batch:
            break
        yield batch
```


#### 複雜度

O(n) 總時間、O(size) 額外空間


#### 常見錯誤與延伸

函式含 yield 後，驗證錯誤會在開始迭代時才發生，而不是呼叫函式當下。


### 060. Decorator 記錄執行時間


#### 核心原理

decorator 回傳包裝函式。`functools.wraps` 保留名稱與 docstring；`try/finally` 確保例外時仍執行記錄。
`perf_counter()` 適合量測經過時間。


#### Python 解答

```python
from functools import wraps
from time import perf_counter

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            print(f"{func.__name__}: {elapsed:.6f}s")
    return wrapper
```


#### 複雜度

包裝額外成本 O(1)


#### 常見錯誤與延伸

正式系統應使用 logging 而非 print，並避免把敏感參數寫入日誌。


### 061. 單元測試：parse_amount


#### 核心原理

好測試涵蓋正常值、邊界值與錯誤路徑。對例外使用 `assertRaises`，對 Decimal 直接比較精確值。


#### Python 解答

```python
import unittest
from decimal import Decimal

class ParseAmountTests(unittest.TestCase):
    def test_rounding(self):
        self.assertEqual(parse_amount("12.345"), Decimal("12.35"))

    def test_negative(self):
        with self.assertRaises(ValueError):
            parse_amount("-0.01")

    def test_invalid_text(self):
        with self.assertRaises(ValueError):
            parse_amount("abc")

    def test_nan(self):
        with self.assertRaises(ValueError):
            parse_amount("NaN")
```


#### 複雜度

每個測試 O(1)


#### 常見錯誤與延伸

測試不得依賴執行順序；每個測試應獨立建立所需狀態。


### 062. 密碼安全雜湊


#### 核心原理

密碼不能以可逆加密或單次 SHA-256 儲存。KDF 透過 salt 防彩虹表，透過高迭代成本提高暴力破解成本。
比較摘要時用 `hmac.compare_digest` 降低 timing attack 風險。


#### Python 解答

```python
import hashlib
import hmac
import os

def hash_password(password: str) -> str:
    if not password:
        raise ValueError("密碼不可為空")
    iterations = 200_000
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iterations
    )
    return f"{iterations}${salt.hex()}${digest.hex()}"

def verify_password(password: str, stored: str) -> bool:
    try:
        raw_iterations, salt_hex, digest_hex = stored.split("$")
        iterations = int(raw_iterations)
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)
    except (ValueError, TypeError):
        return False
    actual = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iterations
    )
    return hmac.compare_digest(actual, expected)
```


#### 複雜度

每次雜湊 O(iterations)，空間 O(1)


#### 常見錯誤與延伸

實務優先採 Argon2、scrypt、bcrypt 等成熟方案與框架；不可自行發明密碼學格式。


### 063. 輸入白名單與 SQL 注入防護


#### 核心原理

SQL 的值可參數化，但欄名與關鍵字通常不能。對動態識別字要使用固定白名單映射，而非直接拼接任意輸入。


#### Python 解答

```python
def build_order_clause(field: str, direction: str) -> str:
    allowed_fields = {
        "timestamp": "timestamp",
        "amount": "amount",
        "account": "account",
    }
    normalized_direction = direction.upper()
    if field not in allowed_fields:
        raise ValueError("不允許的排序欄位")
    if normalized_direction not in {"ASC", "DESC"}:
        raise ValueError("不允許的排序方向")
    return f"ORDER BY {allowed_fields[field]} {normalized_direction}"
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

白名單內容必須由程式固定定義；不可把使用者輸入先『清理』後仍直接當 SQL 識別字。


### 064. Big-O 優化：重複會員查找


#### 核心原理

list membership 為 O(m)，n 筆交易總計 O(nm)。先把客戶 ID 建成 set，平均 membership O(1)，
總計降為 O(n+m)。


#### Python 解答

```python
def filter_known_transactions(
    transactions: list[dict], customer_ids: list[str]
) -> list[dict]:
    known = set(customer_ids)
    return [
        tx for tx in transactions
        if tx.get("customer_id") in known
    ]
```


#### 複雜度

平均 O(n+m) 時間、O(m) 空間


#### 常見錯誤與延伸

set 適合精確 membership；若資料量極大且可接受誤判，可考慮 Bloom filter，但考試通常不必延伸到此。


### 065. dataclass 交易資料模型


#### 核心原理

`dataclass` 可自動產生初始化、比較與表示方法。`frozen=True` 讓實例不可被一般方式修改，
有助於把交易事件視為不可變資料；`__post_init__` 負責跨欄位與商業規則驗證。


#### Python 解答

```python
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Transaction:
    tx_id: str
    amount: Decimal
    currency: str

    def __post_init__(self) -> None:
        if not self.tx_id:
            raise ValueError("tx_id 不可為空")
        if self.amount < 0:
            raise ValueError("amount 不可為負")
        if len(self.currency) != 3 or not self.currency.isalpha() or not self.currency.isupper():
            raise ValueError("currency 必須是三碼大寫英文字母")
```


#### 複雜度

建立物件 O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

`frozen=True` 不是安全邊界，也不能保護欄位內部可變物件；它主要表達程式設計上的不可變意圖。

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
