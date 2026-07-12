# 2026 土地銀行 AI 應用人員：Python 應用實作詳解


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

這一份答案把程式碼放在「銀行資料、AI 模型、風控決策與治理」的完整脈絡中。
請特別注意：範例閾值與規則是練習值；高分答案要主動指出需要驗證、人工覆核、稽核與降級。


## 三、答案索引

共 **65 題**。

- [001. 交易資料清洗管線](#001-交易資料清洗管線)
- [002. 分行月度 KPI 報表](#002-分行月度-kpi-報表)
- [003. 重複交易偵測](#003-重複交易偵測)
- [004. 餘額序列一致性檢查](#004-餘額序列一致性檢查)
- [005. 滾動平均與異常尖峰](#005-滾動平均與異常尖峰)
- [006. 外幣換算與精度](#006-外幣換算與精度)
- [007. 本息平均攤還表](#007-本息平均攤還表)
- [008. 信用額度使用率告警](#008-信用額度使用率告警)
- [009. 客戶 360 彙總](#009-客戶-360-彙總)
- [010. 兩份報表自動對帳](#010-兩份報表自動對帳)
- [011. 規則式詐欺風險分數](#011-規則式詐欺風險分數)
- [012. 短時間大量交易 Velocity Rule](#012-短時間大量交易-velocity-rule)
- [013. 拆單（Structuring）偵測](#013-拆單（structuring）偵測)
- [014. 深夜 ATM 提款異常](#014-深夜-atm-提款異常)
- [015. 不可能移動（Impossible Travel）](#015-不可能移動（impossible-travel）)
- [016. 新受款人高額轉帳](#016-新受款人高額轉帳)
- [017. ATM 臉部遮蔽判定邏輯](#017-atm-臉部遮蔽判定邏輯)
- [018. 混淆矩陣實作](#018-混淆矩陣實作)
- [019. Precision、Recall、F1](#019-precision、recall、f1)
- [020. 成本敏感閾值選擇](#020-成本敏感閾值選擇)
- [021. 類別權重計算](#021-類別權重計算)
- [022. Isolation Forest 異常偵測](#022-isolation-forest-異常偵測)
- [023. Robust Z-score（MAD）](#023-robust-z-score（mad）)
- [024. 交易特徵工程](#024-交易特徵工程)
- [025. 時間序列切分](#025-時間序列切分)
- [026. 共享裝置的人頭帳戶網路](#026-共享裝置的人頭帳戶網路)
- [027. 帳戶關係圖連通元件](#027-帳戶關係圖連通元件)
- [028. 三角循環金流偵測](#028-三角循環金流偵測)
- [029. Fan-in / Fan-out 可疑帳戶](#029-fan-in-/-fan-out-可疑帳戶)
- [030. 即時告警去重與冷卻時間](#030-即時告警去重與冷卻時間)
- [031. 智能客服意圖規則分類器](#031-智能客服意圖規則分類器)
- [032. 中文文字正規化](#032-中文文字正規化)
- [033. FAQ TF-IDF 檢索](#033-faq-tf-idf-檢索)
- [034. 熱搜問題 Top-K 推薦](#034-熱搜問題-top-k-推薦)
- [035. 客服日誌敏感資料遮罩](#035-客服日誌敏感資料遮罩)
- [036. Prompt Injection 基礎防護](#036-prompt-injection-基礎防護)
- [037. 低信心回答轉人工](#037-低信心回答轉人工)
- [038. 對話上下文視窗](#038-對話上下文視窗)
- [039. 法遵文件分塊](#039-法遵文件分塊)
- [040. 法規條文相似度比對](#040-法規條文相似度比對)
- [041. 外規與內規變更差異](#041-外規與內規變更差異)
- [042. 客訴情緒關鍵詞基線](#042-客訴情緒關鍵詞基線)
- [043. 釣魚簡訊特徵擷取](#043-釣魚簡訊特徵擷取)
- [044. 官方短碼驗證](#044-官方短碼驗證)
- [045. TF-IDF 關鍵詞抽取](#045-tf-idf-關鍵詞抽取)
- [046. 金融文字欄位擷取](#046-金融文字欄位擷取)
- [047. Logistic Regression 詐欺模型](#047-logistic-regression-詐欺模型)
- [048. 決策樹與特徵重要度](#048-決策樹與特徵重要度)
- [049. Stratified Cross-Validation](#049-stratified-cross-validation)
- [050. 機率校準](#050-機率校準)
- [051. ROC-AUC 與 PR-AUC 比較](#051-roc-auc-與-pr-auc-比較)
- [052. 群體公平性檢查](#052-群體公平性檢查)
- [053. 單筆預測理由](#053-單筆預測理由)
- [054. 模型保存與版本資訊](#054-模型保存與版本資訊)
- [055. 推論輸入 Schema 驗證](#055-推論輸入-schema-驗證)
- [056. FastAPI 模型推論端點](#056-fastapi-模型推論端點)
- [057. 批次評分管線](#057-批次評分管線)
- [058. Population Stability Index](#058-population-stability-index)
- [059. Kolmogorov–Smirnov 漂移檢定](#059-kolmogorov–smirnov-漂移檢定)
- [060. 模型績效監控](#060-模型績效監控)
- [061. 不可竄改稽核日誌雜湊鏈](#061-不可竄改稽核日誌雜湊鏈)
- [062. 客戶識別碼假名化](#062-客戶識別碼假名化)
- [063. 角色權限檢查](#063-角色權限檢查)
- [064. RPA 重試與冪等性](#064-rpa-重試與冪等性)
- [065. 端到端可疑交易決策管線](#065-端到端可疑交易決策管線)


---

## 四、詳細解答


### 001. 交易資料清洗管線


#### 核心原理

銀行資料管線不能只「drop 掉錯誤資料」而不留痕跡。應先建立拒絕原因，再把有效與無效資料分流。
對 tx_id 去重前先排序，才能明確定義保留規則。


#### Python 解答

```python
import pandas as pd

def clean_transactions(df: pd.DataFrame):
    required = {"tx_id", "account_id", "timestamp", "amount", "channel"}
    if not required.issubset(df.columns):
        raise ValueError("缺少必要欄位")

    data = df.copy().drop_duplicates()
    data["_row_id"] = range(len(data))
    data["timestamp_parsed"] = pd.to_datetime(data["timestamp"], errors="coerce")
    data["amount_parsed"] = pd.to_numeric(data["amount"], errors="coerce")
    data["reject_reason"] = ""

    data.loc[data["tx_id"].isna() | data["tx_id"].eq(""), "reject_reason"] += "missing_tx_id;"
    data.loc[data["account_id"].isna() | data["account_id"].eq(""), "reject_reason"] += "missing_account;"
    data.loc[data["timestamp_parsed"].isna(), "reject_reason"] += "bad_timestamp;"
    data.loc[data["amount_parsed"].isna(), "reject_reason"] += "bad_amount;"
    data.loc[data["amount_parsed"].lt(0), "reject_reason"] += "negative_amount;"

    valid_candidates = data[data["reject_reason"].eq("")].sort_values(
        ["timestamp_parsed", "_row_id"]
    )
    duplicate_mask = valid_candidates.duplicated("tx_id", keep="first")
    duplicate_ids = set(valid_candidates.loc[duplicate_mask, "_row_id"])
    data.loc[data["_row_id"].isin(duplicate_ids), "reject_reason"] += "duplicate_tx_id;"

    rejected = data[data["reject_reason"].ne("")].copy()
    clean = data[data["reject_reason"].eq("")].copy()
    clean["timestamp"] = clean["timestamp_parsed"]
    clean["amount"] = clean["amount_parsed"]
    clean["channel"] = clean["channel"].fillna("UNKNOWN").str.upper()

    helper_cols = ["_row_id", "timestamp_parsed", "amount_parsed", "reject_reason"]
    clean = clean.drop(columns=helper_cols).reset_index(drop=True)
    rejected = rejected.drop(columns=["timestamp_parsed", "amount_parsed"]).reset_index(drop=True)
    return clean, rejected
```


#### 複雜度

O(n log n) 時間（排序主導）、O(n) 空間


#### 常見錯誤與延伸

資料去重規則必須由業務定義；不能假設「最後一筆」一定正確。正式流程還應記錄批次 ID、來源檔、
處理時間與資料血緣。


### 002. 分行月度 KPI 報表


#### 核心原理

先聚合到分行月層級，再以 groupby + pct_change 計算同一分行的月增率。
時間欄位應先正規化，避免字串月份排序錯亂。


#### Python 解答

```python
import pandas as pd

def branch_monthly_kpi(df: pd.DataFrame) -> pd.DataFrame:
    data = df[df["status"].eq("SUCCESS")].copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    data["month"] = data["timestamp"].dt.to_period("M")
    result = (
        data.groupby(["branch", "month"], as_index=False)
        .agg(
            tx_count=("amount", "size"),
            total_amount=("amount", "sum"),
            avg_amount=("amount", "mean"),
        )
        .sort_values(["branch", "month"])
    )
    result["mom_growth"] = result.groupby("branch")["total_amount"].pct_change()
    result["month"] = result["month"].astype(str)
    return result.reset_index(drop=True)
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

若上月為 0，月增率會是 inf；報表需明確決定要顯示空值、特殊符號或另設狀態欄。


### 003. 重複交易偵測


#### 核心原理

先按分組鍵與時間排序，再用 groupby.shift 取得前一筆。只比較相鄰筆即可，因為時間已排序。


#### Python 解答

```python
import pandas as pd

def find_duplicate_transactions(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    keys = ["account_id", "merchant", "amount"]
    data = data.sort_values(keys + ["timestamp"])
    data["previous_time"] = data.groupby(keys)["timestamp"].shift(1)
    data["previous_tx_id"] = data.groupby(keys)["tx_id"].shift(1)
    delta = data["timestamp"] - data["previous_time"]
    mask = delta.between(pd.Timedelta(0), pd.Timedelta(minutes=2), inclusive="both")
    return data.loc[mask].reset_index(drop=True)
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

相同金額不一定是重複扣款，因此結果應是待查核名單，不應直接逆轉交易。


### 004. 餘額序列一致性檢查


#### 核心原理

這是序列資料的 invariant 驗證。先排序，再取得前一筆 balance_after，依交易方向計算預期值。
金額比較應考慮 Decimal 或最小貨幣單位整數。


#### Python 解答

```python
import pandas as pd
import numpy as np

def validate_balance_sequence(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    data = data.sort_values(["account_id", "timestamp", "tx_id"])
    data["previous_balance"] = data.groupby("account_id")["balance_after"].shift(1)

    direction = np.where(
        data["type"].eq("CREDIT"), 1,
        np.where(data["type"].eq("DEBIT"), -1, np.nan)
    )
    data["expected_balance"] = data["previous_balance"] + direction * data["amount"]
    mask = data["previous_balance"].notna() & (
        ~np.isclose(data["expected_balance"], data["balance_after"], atol=0.005)
    )
    return data.loc[mask].reset_index(drop=True)
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

若同一時間有多筆交易，必須有可靠的序號或事件順序；只靠 timestamp 可能無法重建正確帳務。


### 005. 滾動平均與異常尖峰


#### 核心原理

避免把當前交易納入基準，否則異常值會拉高自己的門檻。pandas rolling 後先 shift 或先 shift 再 rolling。


#### Python 解答

```python
import pandas as pd

def flag_amount_spikes(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    data = data.sort_values(["account_id", "timestamp"])

    def add_features(group):
        history = group["amount"].shift(1)
        group["rolling_mean"] = history.rolling(7, min_periods=3).mean()
        group["rolling_std"] = history.rolling(7, min_periods=3).std(ddof=0)
        threshold = group["rolling_mean"] + 3 * group["rolling_std"]
        group["is_spike"] = group["rolling_mean"].notna() & group["amount"].gt(threshold)
        return group

    return data.groupby("account_id", group_keys=False).apply(add_features).reset_index(drop=True)
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

常態分布假設在交易金額上可能不成立；實務可用 log 轉換、分位數或 MAD。


### 006. 外幣換算與精度


#### 核心原理

金融計算用 Decimal，且應明確定義運算順序與 rounding mode。匯率與費率通常來自外部資料，
需保留來源與生效時間。


#### Python 解答

```python
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")

def convert_currency(amount, rate, fee_rate="0") -> Decimal:
    amount = Decimal(str(amount))
    rate = Decimal(str(rate))
    fee_rate = Decimal(str(fee_rate))
    if amount < 0 or rate < 0 or not Decimal("0") <= fee_rate <= Decimal("1"):
        raise ValueError("輸入範圍錯誤")
    converted = amount * rate
    net = converted - converted * fee_rate
    return net.quantize(CENT, rounding=ROUND_HALF_UP)
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

不同幣別小數位可能不同；正式系統不能一律假設 2 位。


### 007. 本息平均攤還表


#### 核心原理

先算月利率與固定付款，再逐月拆分利息與本金。最後一期應調整因四捨五入造成的微小殘值。


#### Python 解答

```python
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")

def amortization_schedule(principal, annual_rate, months):
    p = Decimal(str(principal))
    annual = Decimal(str(annual_rate))
    if p <= 0 or annual < 0 or months <= 0:
        raise ValueError("輸入範圍錯誤")
    monthly_rate = annual / Decimal("12")
    if monthly_rate == 0:
        payment = p / months
    else:
        factor = (Decimal("1") + monthly_rate) ** months
        payment = p * monthly_rate * factor / (factor - Decimal("1"))

    balance = p
    rows = []
    for period in range(1, months + 1):
        interest = balance * monthly_rate
        principal_paid = payment - interest
        if period == months:
            principal_paid = balance
            payment_now = principal_paid + interest
        else:
            payment_now = payment
        balance -= principal_paid
        rows.append({
            "period": period,
            "payment": payment_now.quantize(CENT, rounding=ROUND_HALF_UP),
            "principal": principal_paid.quantize(CENT, rounding=ROUND_HALF_UP),
            "interest": interest.quantize(CENT, rounding=ROUND_HALF_UP),
            "balance": max(balance, Decimal("0")).quantize(CENT, rounding=ROUND_HALF_UP),
        })
    return rows
```


#### 複雜度

O(months) 時間、O(months) 空間


#### 常見錯誤與延伸

實務貸款會有日計息、寬限期、提前清償、變動利率與各種費用，本題是簡化模型。


### 008. 信用額度使用率告警


#### 核心原理

規則引擎必須把閾值、邊界與資料錯誤分開處理。可以用 numpy.select 向量化。


#### Python 解答

```python
import pandas as pd
import numpy as np

def credit_utilization_alert(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    if (data["credit_limit"] <= 0).any():
        raise ValueError("credit_limit 必須大於 0")
    data["utilization"] = data["outstanding_balance"] / data["credit_limit"]
    conditions = [
        data["utilization"] >= 0.90,
        data["utilization"] >= 0.70,
    ]
    choices = ["HIGH", "WATCH"]
    data["alert_level"] = np.select(conditions, choices, default="NORMAL")
    return data
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

使用率高不等同違約；它只是風險特徵之一。不得以單一規則自動做重大不利決策。


### 009. 客戶 360 彙總


#### 核心原理

先把交易接到 account 的 customer_id，再做時間篩選與聚合，最後 left join 回客戶主檔。
對關係使用 merge validate，能及早發現鍵重複。


#### Python 解答

```python
import pandas as pd

def build_customer_360(customers, accounts, transactions, as_of):
    as_of = pd.Timestamp(as_of)
    tx = transactions.copy()
    tx["timestamp"] = pd.to_datetime(tx["timestamp"], errors="raise")
    tx = tx.merge(
        accounts[["account_id", "customer_id"]],
        on="account_id",
        how="left",
        validate="many_to_one",
    )
    recent = tx[tx["timestamp"].between(as_of - pd.Timedelta(days=90), as_of)]
    tx_agg = recent.groupby("customer_id", as_index=False).agg(
        amount_90d=("amount", "sum"),
        tx_count_90d=("tx_id", "size"),
        last_tx_time=("timestamp", "max"),
    )
    account_agg = accounts.groupby("customer_id", as_index=False).agg(
        account_count=("account_id", "nunique")
    )
    result = (
        customers.merge(account_agg, on="customer_id", how="left", validate="one_to_one")
        .merge(tx_agg, on="customer_id", how="left", validate="one_to_one")
    )
    result[["account_count", "amount_90d", "tx_count_90d"]] = result[
        ["account_count", "amount_90d", "tx_count_90d"]
    ].fillna(0)
    return result
```


#### 複雜度

O(n log n) 以聚合與 join 為主、O(n) 空間


#### 常見錯誤與延伸

客戶 360 涉及高度敏感資料，應依最小權限、目的限制與資料保留政策管理。


### 010. 兩份報表自動對帳


#### 核心原理

對帳前先驗證主鍵唯一，再 outer merge 並使用 indicator 區分來源。金額比較需採 Decimal 或容許差異。


#### Python 解答

```python
import pandas as pd
import numpy as np

def reconcile(a: pd.DataFrame, b: pd.DataFrame) -> dict[str, pd.DataFrame]:
    if a["reference_id"].duplicated().any() or b["reference_id"].duplicated().any():
        raise ValueError("reference_id 必須唯一")
    merged = a.merge(
        b,
        on="reference_id",
        how="outer",
        suffixes=("_a", "_b"),
        indicator=True,
        validate="one_to_one",
    )
    only_a = merged[merged["_merge"].eq("left_only")]
    only_b = merged[merged["_merge"].eq("right_only")]
    both = merged[merged["_merge"].eq("both")]
    same = np.isclose(both["amount_a"], both["amount_b"], atol=0.005)
    return {
        "only_a": only_a.reset_index(drop=True),
        "only_b": only_b.reset_index(drop=True),
        "amount_mismatch": both[~same].reset_index(drop=True),
        "matched": both[same].reset_index(drop=True),
    }
```


#### 複雜度

O(n+m) 平均時間、O(n+m) 空間


#### 常見錯誤與延伸

RPA 自動化不能跳過異常處理；對帳結果應可追溯，且不可自動把差異『修平』。


### 011. 規則式詐欺風險分數


#### 核心原理

規則分數透明、易稽核，適合當模型前後的安全護欄。規則本身不是機器學習，仍需版本化與成效監控。


#### Python 解答

```python
def fraud_rule_score(tx: dict) -> dict:
    score = 0
    reasons = []
    if tx["amount"] >= 100_000:
        score += 30
        reasons.append("high_amount")
    if 0 <= tx["hour"] <= 5:
        score += 15
        reasons.append("unusual_hour")
    if tx["is_new_beneficiary"]:
        score += 20
        reasons.append("new_beneficiary")
    if tx["device_changed"]:
        score += 20
        reasons.append("device_changed")
    if tx["country_risk"] == "HIGH":
        score += 25
        reasons.append("high_risk_country")
    score = min(score, 100)
    return {"score": score, "review": score >= 60, "reasons": reasons}
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

規則門檻應由歷史資料與誤報成本驗證；不可把示範權重直接視為正式風控政策。


### 012. 短時間大量交易 Velocity Rule


#### 核心原理

每個帳戶維護 deque，加入新交易後移除視窗外舊交易。這比每筆重新掃描全部歷史更有效率。


#### Python 解答

```python
from collections import defaultdict, deque
from datetime import timedelta

def velocity_alerts(transactions):
    windows = defaultdict(deque)
    sums = defaultdict(float)
    alerts = []

    for tx in transactions:
        account = tx["account_id"]
        now = tx["timestamp"]
        window = windows[account]
        cutoff = now - timedelta(minutes=10)

        while window and window[0]["timestamp"] < cutoff:
            old = window.popleft()
            sums[account] -= old["amount"]

        window.append(tx)
        sums[account] += tx["amount"]

        if len(window) >= 5 or sums[account] >= 200_000:
            alerts.append({
                "tx_id": tx["tx_id"],
                "account_id": account,
                "window_count": len(window),
                "window_amount": sums[account],
            })
    return alerts
```


#### 複雜度

O(n) 攤銷時間、O(w) 空間，w 為活躍視窗內交易數


#### 常見錯誤與延伸

分散式即時系統還要處理亂序事件、事件時間、狀態保存與重複投遞。


### 013. 拆單（Structuring）偵測


#### 核心原理

固定日曆日與真正 rolling 24h 不同。本題以每筆為右端點，用雙指標維持 24 小時視窗。


#### Python 解答

```python
from collections import deque
import pandas as pd

def detect_structuring(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    data = data[data["amount"].between(80_000, 99_999)]
    alerts = []

    for account, group in data.sort_values("timestamp").groupby("account_id"):
        window = deque()
        total = 0.0
        for row in group.itertuples(index=False):
            cutoff = row.timestamp - pd.Timedelta(hours=24)
            while window and window[0].timestamp < cutoff:
                old = window.popleft()
                total -= old.amount
            window.append(row)
            total += row.amount
            if len(window) >= 3 and total >= 250_000:
                alerts.append({
                    "account_id": account,
                    "window_start": window[0].timestamp,
                    "window_end": row.timestamp,
                    "tx_count": len(window),
                    "total_amount": total,
                    "tx_ids": [x.tx_id for x in window],
                })
    return pd.DataFrame(alerts)
```


#### 複雜度

O(n log n + n) 時間、O(w) 空間


#### 常見錯誤與延伸

實務 AML 情境需結合客戶風險、交易目的、關係人與法規門檻；單一規則只產生可疑線索。


### 014. 深夜 ATM 提款異常


#### 核心原理

跨午夜區間不能用單純 `start <= hour <= end`。若 start > end，區間是 `hour>=start or hour<=end`。


#### Python 解答

```python
def is_unusual_atm_withdrawal(tx: dict, profile: dict) -> bool:
    hour = tx["timestamp"].hour
    start = profile["usual_start"]
    end = profile["usual_end"]

    if start <= end:
        in_usual_hours = start <= hour <= end
    else:
        in_usual_hours = hour >= start or hour <= end

    return (
        tx["channel"] == "ATM"
        and not in_usual_hours
        and tx["amount"] > 2 * profile["avg_withdrawal"]
    )
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

深夜提款可能完全合法，告警應搭配裝置、地點、受款人、客戶確認等證據。


### 015. 不可能移動（Impossible Travel）


#### 核心原理

Haversine 以地球半徑和經緯度弧度估計兩點大圓距離。需先檢查時間順序與缺失座標。


#### Python 解答

```python
from math import radians, sin, cos, asin, sqrt

def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    return 2 * r * asin(sqrt(a))

def impossible_travel(prev_tx: dict, current_tx: dict) -> dict:
    seconds = (current_tx["timestamp"] - prev_tx["timestamp"]).total_seconds()
    if seconds <= 0:
        return {"flagged": False, "reason": "non_positive_time_gap"}
    distance = haversine_km(
        prev_tx["lat"], prev_tx["lon"], current_tx["lat"], current_tx["lon"]
    )
    speed = distance / (seconds / 3600)
    return {"flagged": speed > 900, "distance_km": distance, "speed_kmh": speed}
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

VPN、代理交易、卡片共用或定位誤差都可能造成誤報；地理訊號不可單獨作為拒絕交易依據。


### 016. 新受款人高額轉帳


#### 核心原理

set membership 平均 O(1)。規則輸出應包含 reason code，利於稽核、客服說明與成效分析。


#### Python 解答

```python
def new_beneficiary_alert(tx: dict, known_beneficiaries: set[str]) -> dict:
    beneficiary = tx.get("beneficiary_id")
    if not beneficiary:
        raise ValueError("缺少 beneficiary_id")
    is_new = beneficiary not in known_beneficiaries
    alert = is_new and tx["amount"] >= 100_000
    return {
        "alert": alert,
        "is_new_beneficiary": is_new,
        "reason": "NEW_HIGH_VALUE_BENEFICIARY" if alert else None,
    }
```


#### 複雜度

O(1) 平均時間、O(1) 額外空間


#### 常見錯誤與延伸

受款人歷史集合要有時間範圍與身份合併規則；同一人可能有多個帳號。


### 017. ATM 臉部遮蔽判定邏輯


#### 核心原理

把模型推論與業務決策分層，可獨立測試閾值與流程。實務上臉部遮蔽提示不應等同身份認證結果。


#### Python 解答

```python
def atm_face_decision(result: dict, retry_count: int) -> str:
    bad_signal = (
        not result.get("face_detected", False)
        or result.get("occlusion_ratio", 1.0) >= 0.4
        or result.get("confidence", 0.0) < 0.7
    )
    if not bad_signal:
        return "PASS"
    if retry_count + 1 >= 3:
        return "ESCALATE"
    return "RETRY"
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

生物辨識涉及隱私、公平性、活體偵測與攻擊風險。示範閾值不可直接用於正式 ATM。


### 018. 混淆矩陣實作


#### 核心原理

混淆矩陣是 precision、recall、specificity、F1 的基礎。正類應明確定義為「詐欺」或「異常」。


#### Python 解答

```python
def confusion_counts(y_true, y_pred) -> dict:
    if len(y_true) != len(y_pred):
        raise ValueError("長度不一致")
    allowed = {0, 1}
    if set(y_true) - allowed or set(y_pred) - allowed:
        raise ValueError("只允許 0/1")
    tp = fp = tn = fn = 0
    for actual, predicted in zip(y_true, y_pred):
        if actual == 1 and predicted == 1:
            tp += 1
        elif actual == 0 and predicted == 1:
            fp += 1
        elif actual == 0 and predicted == 0:
            tn += 1
        else:
            fn += 1
    return {"TP": tp, "FP": fp, "TN": tn, "FN": fn}
```


#### 複雜度

O(n) 時間、O(1) 空間


#### 常見錯誤與延伸

不要只看 accuracy；在詐欺比例極低時，全部預測正常也可能有很高 accuracy。


### 019. Precision、Recall、F1


#### 核心原理

Precision 衡量告警中多少是真的；Recall 衡量真詐欺中攔到多少。F1 是兩者調和平均，
適合需要平衡時使用，但仍未反映不同錯誤成本。


#### Python 解答

```python
def classification_metrics(tp: int, fp: int, fn: int) -> dict:
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall else 0.0
    )
    return {"precision": precision, "recall": recall, "f1": f1}
```


#### 複雜度

O(1) 時間、O(1) 空間


#### 常見錯誤與延伸

選擇指標要跟業務代價一致；高 recall 可能帶來大量人工審查。


### 020. 成本敏感閾值選擇


#### 核心原理

分類機率需要轉成決策。閾值不是固定 0.5，而應由成本、容量、法遵與風險承受度決定。


#### Python 解答

```python
def choose_threshold(y_true, probabilities, thresholds, fp_cost, fn_cost):
    best = None
    for threshold in sorted(thresholds, reverse=True):
        predictions = [int(p >= threshold) for p in probabilities]
        counts = confusion_counts(y_true, predictions)
        cost = counts["FP"] * fp_cost + counts["FN"] * fn_cost
        candidate = {"threshold": threshold, "cost": cost, **counts}
        if best is None or cost < best["cost"]:
            best = candidate
    if best is None:
        raise ValueError("thresholds 不可為空")
    return best
```


#### 複雜度

O(n·t) 時間、O(n) 空間，t 為候選閾值數


#### 常見錯誤與延伸

閾值只能在驗證集上選，不能在最終測試集反覆調整，否則會高估泛化能力。


### 021. 類別權重計算


#### 核心原理

讓少數類別樣本在 loss 中有較高權重，是處理不平衡的一種方法。它不會創造新資訊，
仍需搭配適當評估與機率校準。


#### Python 解答

```python
from collections import Counter

def balanced_class_weights(labels) -> dict:
    counts = Counter(labels)
    if len(counts) < 2:
        raise ValueError("至少需要兩個類別")
    n = len(labels)
    k = len(counts)
    return {label: n / (k * count) for label, count in counts.items()}
```


#### 複雜度

O(n) 時間、O(k) 空間


#### 常見錯誤與延伸

權重過大可能使模型不穩定；也不能在 train/test 切分前用全資料計算。


### 022. Isolation Forest 異常偵測


#### 核心原理

Isolation Forest 透過隨機切割隔離樣本；異常點通常較快被隔離。它是非監督方法，
輸出代表「少見」而不必然代表詐欺。


#### Python 解答

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

def isolation_forest_flags(df: pd.DataFrame, contamination=0.01):
    features = ["amount", "tx_count_1h", "new_beneficiary", "device_age_days"]
    X = df[features].copy()
    if X.isna().any().any():
        raise ValueError("特徵不可有缺失值")
    model = IsolationForest(
        n_estimators=200,
        contamination=contamination,
        random_state=42,
    )
    prediction = model.fit_predict(X)
    result = df.copy()
    result["anomaly_score"] = -model.score_samples(X)
    result["is_anomaly"] = prediction == -1
    return result, model
```


#### 複雜度

約 O(t·n log n)，t 為樹數；O(t·n) 模型與結果空間


#### 常見錯誤與延伸

contamination 是預期異常比例，不應為了得到漂亮數字任意設定；需以調查容量與驗證結果調整。


### 023. Robust Z-score（MAD）


#### 核心原理

平均與標準差會被極端值拉動；median 與 MAD 對離群值更穩健。modified z-score 常用門檻約 3.5，
但仍需依資料分布驗證。


#### Python 解答

```python
import numpy as np

def modified_z_scores(values):
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or x.size == 0:
        raise ValueError("需為非空一維資料")
    median = np.median(x)
    mad = np.median(np.abs(x - median))
    if mad == 0:
        result = np.zeros_like(x)
        result[x > median] = np.inf
        result[x < median] = -np.inf
        return result
    return 0.6745 * (x - median) / mad
```


#### 複雜度

O(n) 平均時間、O(n) 空間


#### 常見錯誤與延伸

交易金額常右偏，分群後或 log 轉換後再做異常判斷可能更合理。


### 024. 交易特徵工程


#### 核心原理

特徵必須只使用預測當下已知資訊。`beneficiary_seen_before` 若直接用全資料 nunique，
會引入未來資料洩漏；需依序維護歷史集合。


#### Python 解答

```python
import pandas as pd
import numpy as np

def engineer_transaction_features(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    data = data.sort_values(["account_id", "timestamp", "tx_id"]).reset_index(drop=True)
    data["hour"] = data["timestamp"].dt.hour
    data["is_weekend"] = data["timestamp"].dt.weekday >= 5
    data["time_since_prev_min"] = (
        data.groupby("account_id")["timestamp"].diff().dt.total_seconds() / 60
    )
    medians = data.groupby("account_id")["amount"].transform("median")
    data["amount_vs_account_median"] = np.where(
        medians > 0, data["amount"] / medians, np.nan
    )

    seen = {}
    flags = []
    for row in data.itertuples():
        key = row.account_id
        history = seen.setdefault(key, set())
        flags.append(row.beneficiary_id in history)
        history.add(row.beneficiary_id)
    data["beneficiary_seen_before"] = flags
    return data
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

本題 median 使用整段資料，若用於真實模型也會洩漏未來；正式訓練應以滾動歷史中位數或訓練期統計量。


### 025. 時間序列切分


#### 核心原理

金融交易模型常面對概念漂移，因此以時間切分比隨機切分更接近上線情境。
以 unique timestamp 作切點可避免同一事件時點跨集合。


#### Python 解答

```python
import pandas as pd

def temporal_split(df: pd.DataFrame, train_ratio=0.7, val_ratio=0.15):
    if train_ratio <= 0 or val_ratio < 0 or train_ratio + val_ratio >= 1:
        raise ValueError("比例錯誤")
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    times = sorted(data["timestamp"].unique())
    if len(times) < 3:
        raise ValueError("時間點不足")
    train_end = times[max(0, int(len(times) * train_ratio) - 1)]
    val_end = times[max(1, int(len(times) * (train_ratio + val_ratio)) - 1)]

    train = data[data["timestamp"] <= train_end]
    validation = data[(data["timestamp"] > train_end) & (data["timestamp"] <= val_end)]
    test = data[data["timestamp"] > val_end]
    return train, validation, test
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

切分後仍要檢查每組是否含正負類別；極度稀少事件可能需要調整時間窗。


### 026. 共享裝置的人頭帳戶網路


#### 核心原理

共享裝置形成二分圖（account ↔ device）。先按 device 聚合唯一帳戶，是最簡單的 fan-out 規則。


#### Python 解答

```python
import pandas as pd

def shared_device_clusters(df: pd.DataFrame, min_accounts=5) -> pd.DataFrame:
    data = df.dropna(subset=["device_id"]).drop_duplicates(
        ["account_id", "device_id"]
    )
    grouped = (
        data.groupby("device_id")["account_id"]
        .agg(lambda s: sorted(set(s)))
        .reset_index(name="accounts")
    )
    grouped["account_count"] = grouped["accounts"].str.len()
    return grouped[grouped["account_count"] >= min_accounts].reset_index(drop=True)
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

家庭、企業或公共電腦也可能共享裝置；需加入 IP、地點、交易關係與時間特徵。


### 027. 帳戶關係圖連通元件


#### 核心原理

Disjoint Set Union 以路徑壓縮與按秩合併，高效處理大量連通關係。


#### Python 解答

```python
def connected_account_components(edges, min_size=3):
    parent = {}
    rank = {}

    def find(x):
        parent.setdefault(x, x)
        rank.setdefault(x, 0)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    for a, b in edges:
        find(a)
        find(b)
        if a != b:
            union(a, b)

    groups = {}
    for node in parent:
        groups.setdefault(find(node), set()).add(node)
    return [sorted(group) for group in groups.values() if len(group) >= min_size]
```


#### 複雜度

近似 O((V+E)·α(V)) 時間、O(V) 空間


#### 常見錯誤與延伸

連通不代表犯罪關係；元件過大時要用時間窗、金額與方向進一步切分。


### 028. 三角循環金流偵測


#### 核心原理

建立有向 adjacency map，再枚舉長度 3 的路徑。用排序後 tuple canonicalize，避免同一環從不同起點重複。


#### Python 解答

```python
from collections import defaultdict

def detect_triangular_cycles(transfers):
    graph = defaultdict(dict)
    for source, target, amount in transfers:
        if source != target:
            graph[source][target] = graph[source].get(target, 0) + amount

    cycles = {}
    for a, neighbors_a in graph.items():
        for b, ab in neighbors_a.items():
            for c, bc in graph.get(b, {}).items():
                if c in {a, b} or a not in graph.get(c, {}):
                    continue
                ca = graph[c][a]
                amounts = [ab, bc, ca]
                if max(amounts) == 0:
                    continue
                if max(amounts) - min(amounts) <= 0.10 * max(amounts):
                    key = tuple(sorted([a, b, c]))
                    cycles[key] = {
                        "accounts": key,
                        "amounts": amounts,
                    }
    return list(cycles.values())
```


#### 複雜度

最差 O(V³)，稀疏圖約依三段鄰接展開；O(E) 空間


#### 常見錯誤與延伸

真正資金網路可能跨多日、多層與多幣別；三角環只是可解釋的初步規則。


### 029. Fan-in / Fan-out 可疑帳戶


#### 核心原理

先把 timestamp floor 到小時，再分別按收款帳戶與付款帳戶聚合唯一對手方及金額。


#### Python 解答

```python
import pandas as pd

def detect_fan_patterns(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], errors="raise")
    data["hour_bucket"] = data["timestamp"].dt.floor("h")

    incoming = (
        data.groupby(["to_account", "hour_bucket"], as_index=False)
        .agg(
            counterparty_count=("from_account", "nunique"),
            total_amount=("amount", "sum"),
        )
        .rename(columns={"to_account": "account_id"})
    )
    incoming["pattern"] = "FAN_IN"

    outgoing = (
        data.groupby(["from_account", "hour_bucket"], as_index=False)
        .agg(
            counterparty_count=("to_account", "nunique"),
            total_amount=("amount", "sum"),
        )
        .rename(columns={"from_account": "account_id"})
    )
    outgoing["pattern"] = "FAN_OUT"

    result = pd.concat([incoming, outgoing], ignore_index=True)
    return result[
        (result["counterparty_count"] >= 10)
        & (result["total_amount"] >= 500_000)
    ].reset_index(drop=True)
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

整點分桶會漏掉跨小時邊界的真實 60 分鐘視窗；正式偵測可改 rolling window。


### 030. 即時告警去重與冷卻時間


#### 核心原理

告警疲勞會降低調查品質。以 `(account_id, rule_id)` 作 key 保存最近通知時間與累計次數。


#### Python 解答

```python
from datetime import timedelta

class AlertDeduplicator:
    def __init__(self, cooldown_minutes=30):
        self.cooldown = timedelta(minutes=cooldown_minutes)
        self.state = {}

    def process(self, alert: dict) -> dict:
        key = (alert["account_id"], alert["rule_id"])
        now = alert["timestamp"]
        record = self.state.get(key)

        if record is None:
            record = {"last_notified": now, "occurrence_count": 1}
            self.state[key] = record
            return {"notify": True, **record}

        record["occurrence_count"] += 1
        notify = now - record["last_notified"] >= self.cooldown
        if notify:
            record["last_notified"] = now
        return {"notify": notify, **record}
```


#### 複雜度

每筆平均 O(1) 時間、O(k) 狀態空間


#### 常見錯誤與延伸

多實例部署需用共享且具原子性的狀態儲存；記憶體 dict 無法跨程序一致。


### 031. 智能客服意圖規則分類器


#### 核心原理

規則式 baseline 可快速建立可解釋結果，並產生後續訓練資料。文字先正規化，再依明確優先序匹配。


#### Python 解答

```python
def classify_intent(text: str) -> dict:
    normalized = "".join(text.lower().split())
    rules = [
        ("CREDIT_CARD", ["信用卡", "卡費", "帳單補寄"]),
        ("LOAN", ["房貸", "信貸", "貸款", "借款"]),
        ("EXCHANGE_RATE", ["匯率", "換匯", "外幣"]),
        ("BRANCH", ["分行", "營業據點", "atm位置"]),
    ]
    for intent, keywords in rules:
        hits = [word for word in keywords if word in normalized]
        if hits:
            return {"intent": intent, "keywords": hits}
    return {"intent": "OTHER", "keywords": []}
```


#### 複雜度

O(n·k) 時間，k 為關鍵詞總數；O(1) 額外空間


#### 常見錯誤與延伸

規則會受同義詞、否定句與上下文影響，應持續分析 OTHER 與誤分類樣本。


### 032. 中文文字正規化


#### 核心原理

NFKC 可統一相容字元與全半形。控制字元可能破壞索引或日誌，應移除；但不可盲目刪除所有標點，
因問號、百分號等可能有語義。


#### Python 解答

```python
import unicodedata

def normalize_chinese_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKC", text).lower()
    cleaned = "".join(
        ch for ch in normalized
        if unicodedata.category(ch) not in {"Cc", "Cf"} or ch.isspace()
    )
    return " ".join(cleaned.split())
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

NFKC 可能改變某些字元語義；對法規原文、帳號或密碼欄位不應任意正規化。


### 033. FAQ TF-IDF 檢索


#### 核心原理

中文未必有空格分詞，字元 2~4 gram 是簡單且穩健的 baseline。檢索分數低時應 fallback，
不能硬回傳不相關答案。


#### Python 解答

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQRetriever:
    def __init__(self, questions, answers, threshold=0.2):
        self.questions = list(questions)
        self.answers = list(answers)
        self.threshold = threshold
        self.vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 4))
        self.matrix = self.vectorizer.fit_transform(self.questions)

    def search(self, query, k=3):
        if k <= 0:
            return []
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.matrix).ravel()
        order = scores.argsort()[::-1][:k]
        if len(order) == 0 or scores[order[0]] < self.threshold:
            return []
        return [
            {
                "question": self.questions[i],
                "answer": self.answers[i],
                "score": float(scores[i]),
            }
            for i in order
        ]
```


#### 複雜度

建索引 O(n·d)；查詢約 O(n·d_sparse)，空間 O(n·d_sparse)


#### 常見錯誤與延伸

threshold 應以客服驗證集調整；FAQ 更新後要重建或增量更新索引。


### 034. 熱搜問題 Top-K 推薦


#### 核心原理

熱搜推薦本質是時間窗內頻率統計。先正規化可避免「匯率」「 匯率 」被分開計數。


#### Python 解答

```python
from collections import Counter
from datetime import timedelta

def trending_queries(records, now, k=10):
    cutoff = now - timedelta(days=7)
    counts = Counter(
        normalize_chinese_text(query)
        for query, timestamp in records
        if cutoff <= timestamp <= now
    )
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]
```


#### 複雜度

O(n + u log u) 時間、O(u) 空間


#### 常見錯誤與延伸

熱門不等於重要；推薦還需排除敏感詞、攻擊字串與短期異常灌量。


### 035. 客服日誌敏感資料遮罩


#### 核心原理

敏感資料應在寫入日誌前最小化。regex 是 baseline，仍可能漏掉帶空格、連字號或非典型格式。
替換順序也重要，先處理身分證與 Email，避免被一般數字規則拆散。


#### Python 解答

```python
import re

ID_RE = re.compile(r"(?<![A-Za-z0-9])[A-Z][12]\d{8}(?![A-Za-z0-9])")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ACCOUNT_RE = re.compile(r"(?<!\d)(\d{6,12})(\d{4})(?!\d)")

def redact_sensitive_text(text: str) -> str:
    text = ID_RE.sub("[NATIONAL_ID]", text)
    text = EMAIL_RE.sub("[EMAIL]", text)
    text = ACCOUNT_RE.sub(lambda m: "*" * len(m.group(1)) + m.group(2), text)
    return text
```


#### 複雜度

O(n) 平均時間、O(n) 輸出空間


#### 常見錯誤與延伸

遮罩不保證匿名化；自由文字可能含姓名、地址與交易內容，仍需存取控制與保留期限。


### 036. Prompt Injection 基礎防護


#### 核心原理

關鍵詞篩選只能當第一層；真正防護依賴權限隔離、工具白名單、輸出驗證、最小資料存取與人工覆核。


#### Python 解答

```python
import re

def screen_prompt(text: str) -> dict:
    normalized = normalize_chinese_text(text)
    blocked_patterns = {
        "IGNORE_INSTRUCTIONS": r"忽略.{0,8}(之前|上述).{0,8}指令",
        "REVEAL_SYSTEM_PROMPT": r"(顯示|透露|輸出).{0,8}(系統提示|system prompt)",
        "EXFILTRATE_CUSTOMERS": r"(輸出|列出|匯出).{0,8}(所有|全部).{0,8}客戶資料",
    }
    reasons = [
        code for code, pattern in blocked_patterns.items()
        if re.search(pattern, normalized, flags=re.IGNORECASE)
    ]
    if reasons:
        return {"decision": "BLOCK", "reasons": reasons}
    if re.search(r"https?://|```", text):
        return {"decision": "REVIEW", "reasons": ["EXTERNAL_CONTENT_OR_CODE"]}
    return {"decision": "ALLOW", "reasons": []}
```


#### 複雜度

O(n) 時間、O(n) 空間


#### 常見錯誤與延伸

不能把 regex 當成完整 prompt injection 防禦；模型不可直接持有任意資料庫查詢權限。


### 037. 低信心回答轉人工


#### 核心原理

高風險金融客服要有拒答與轉人工機制。信心分數本身需校準，來源也要驗證是否屬核准知識庫。


#### Python 解答

```python
def response_gate(model_output: dict) -> dict:
    answer = model_output.get("answer", "")
    confidence = float(model_output.get("confidence", 0))
    sources = model_output.get("sources") or []
    risky_phrase = "不確定但可能" in answer

    if confidence < 0.75 or not sources or risky_phrase:
        return {
            "action": "HANDOFF",
            "message": "此問題需要由專人進一步確認。",
            "reason": {
                "low_confidence": confidence < 0.75,
                "missing_sources": not sources,
                "risky_phrase": risky_phrase,
            },
        }
    return {"action": "ANSWER", "answer": answer, "sources": sources}
```


#### 複雜度

O(n) 時間（檢查答案文字）、O(1) 額外空間


#### 常見錯誤與延伸

LLM 自報 confidence 通常不可靠；較佳做法是用檢索分數、驗證模型、規則與抽樣稽核共同判斷。


### 038. 對話上下文視窗


#### 核心原理

受限上下文能控制成本與敏感資料暴露。實務 token 數不能用字元精確取代，但可作簡化估算。


#### Python 解答

```python
from collections import deque

class ConversationMemory:
    def __init__(self, max_messages=6, max_chars=1000):
        self.max_messages = max_messages
        self.max_chars = max_chars
        self.messages = deque()
        self.total_chars = 0

    def add(self, role: str, content: str) -> None:
        if role not in {"user", "assistant", "system"}:
            raise ValueError("role 錯誤")
        message = {"role": role, "content": content}
        self.messages.append(message)
        self.total_chars += len(content)

        while (
            len(self.messages) > self.max_messages
            or self.total_chars > self.max_chars
        ):
            removed = self.messages.popleft()
            self.total_chars -= len(removed["content"])

    def get(self) -> list[dict]:
        return list(self.messages)
```


#### 複雜度

每則攤銷 O(1)；空間受上限限制


#### 常見錯誤與延伸

系統提示通常不應被一般淘汰策略移除；正式設計會把 system policy 與對話歷史分開管理。


### 039. 法遵文件分塊


#### 核心原理

法規 RAG 應以條文作語義邊界，而不是任意固定字元切割。overlap 可保留跨塊上下文，
但也會增加索引與重複內容。


#### Python 解答

```python
def chunk_articles(articles, source_id, max_chars=800, overlap_chars=100):
    if max_chars <= 0 or overlap_chars < 0 or overlap_chars >= max_chars:
        raise ValueError("chunk 參數錯誤")
    chunks = []
    current = []
    current_len = 0

    def flush():
        nonlocal current, current_len
        if not current:
            return
        text = "\n".join(f'{a["article"]} {a["text"]}' for a in current)
        chunks.append({
            "source_id": source_id,
            "start_article": current[0]["article"],
            "end_article": current[-1]["article"],
            "text": text,
        })
        tail_text = text[-overlap_chars:] if overlap_chars else ""
        current = [{"article": "（承上）", "text": tail_text}] if tail_text else []
        current_len = len(tail_text)

    for article in articles:
        piece = f'{article["article"]} {article["text"]}'
        if current and current_len + 1 + len(piece) > max_chars:
            flush()
        current.append(article)
        current_len += len(piece) + 1
    flush()
    return chunks
```


#### 複雜度

O(n) 時間、O(n) 輸出空間


#### 常見錯誤與延伸

若單一條文本身超過 max_chars，還需第二層句子切分；本簡化版可能產生超長 chunk。


### 040. 法規條文相似度比對


#### 核心原理

這類模型可縮小人工比對範圍，但相似度不代表法律上已符合。最終仍需法遵人員判斷。


#### Python 解答

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_regulations(external, internal, threshold=0.25):
    ext_texts = [item["text"] for item in external]
    int_texts = [item["text"] for item in internal]
    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 5))
    matrix = vectorizer.fit_transform(ext_texts + int_texts)
    ext_matrix = matrix[:len(ext_texts)]
    int_matrix = matrix[len(ext_texts):]
    similarities = cosine_similarity(ext_matrix, int_matrix)

    results = []
    for i, row in enumerate(similarities):
        top = row.argsort()[::-1][:3]
        if len(top) == 0 or row[top[0]] < threshold:
            results.append({
                "external_id": external[i]["id"],
                "internal_id": None,
                "score": float(row[top[0]]) if len(top) else 0.0,
                "status": "NO_MATCH",
            })
            continue
        for j in top:
            results.append({
                "external_id": external[i]["id"],
                "internal_id": internal[j]["id"],
                "score": float(row[j]),
                "status": "CANDIDATE",
            })
    return results
```


#### 複雜度

向量化與相似度約 O((E+I)·d + E·I·d_sparse)，空間依稀疏特徵而定


#### 常見錯誤與延伸

不得把 CANDIDATE 自動等同合規；還需版本、法源位階、生效日與人工簽核。


### 041. 外規與內規變更差異


#### 核心原理

版本差異是法遵追蹤的基礎。`difflib.unified_diff` 提供人類可讀的上下文差異。


#### Python 解答

```python
from difflib import unified_diff

def compare_rule_versions(old_text: str, new_text: str) -> dict:
    old_lines = [line.strip() for line in old_text.splitlines()]
    new_lines = [line.strip() for line in new_text.splitlines()]
    diff = list(unified_diff(
        old_lines,
        new_lines,
        fromfile="old",
        tofile="new",
        lineterm="",
    ))
    added = [line[1:] for line in diff if line.startswith("+") and not line.startswith("+++")]
    removed = [line[1:] for line in diff if line.startswith("-") and not line.startswith("---")]
    return {
        "added_lines": added,
        "removed_lines": removed,
        "unified_diff": "\n".join(diff),
    }
```


#### 複雜度

最差 O(n·m) 依序列比對演算法而定；空間亦依差異大小


#### 常見錯誤與延伸

法律文件中的重新編號可能造成大量 diff；可搭配條文 ID 與語義比對改善。


### 042. 客訴情緒關鍵詞基線


#### 核心原理

中文情緒有否定、程度、副詞與反諷。規則 baseline 需明確標註限制，適合快速建樣本與監控。


#### Python 解答

```python
def sentiment_baseline(text: str) -> dict:
    positive = ["好", "滿意", "方便", "快速", "感謝"]
    negative = ["差", "生氣", "失望", "慢", "錯誤", "無法"]
    negations = ["不", "沒", "無", "未"]

    score = 0
    hits = []
    for word, value in [(w, 1) for w in positive] + [(w, -1) for w in negative]:
        start = 0
        while True:
            index = text.find(word, start)
            if index == -1:
                break
            prefix = text[max(0, index - 3):index]
            adjusted = -value if any(n in prefix for n in negations) else value
            score += adjusted
            hits.append((word, adjusted))
            start = index + len(word)

    label = "POSITIVE" if score > 0 else "NEGATIVE" if score < 0 else "NEUTRAL"
    return {"score": score, "label": label, "hits": hits}
```


#### 複雜度

O(n·k) 時間、O(h) 空間


#### 常見錯誤與延伸

規則無法可靠理解「不是不好」或反諷；重大客訴不可僅依自動情緒分數處理。


### 043. 釣魚簡訊特徵擷取


#### 核心原理

釣魚偵測可先建立可解釋特徵，再訓練分類器。短碼格式只能作一項訊號，仍需查核實際核配清單。


#### Python 解答

```python
import re

def sms_features(text: str, sender: str) -> dict:
    urls = re.findall(r"https?://\S+|www\.\S+", text, flags=re.IGNORECASE)
    urgency_words = ["立即", "逾期", "停權", "驗證", "異常", "最後通知"]
    otp_words = ["otp", "驗證碼", "一次性密碼"]
    digit_count = sum(ch.isdigit() for ch in text)
    return {
        "has_url": bool(urls),
        "url_count": len(urls),
        "urgency_hits": sum(word in text for word in urgency_words),
        "asks_for_otp": any(word.lower() in text.lower() for word in otp_words),
        "certified_short_code": re.fullmatch(r"68\d{3}", sender or "") is not None,
        "digit_ratio": digit_count / len(text) if text else 0.0,
        "exclamation_count": text.count("!") + text.count("！"),
    }
```


#### 複雜度

O(n) 時間、O(u) 空間，u 為 URL 數


#### 常見錯誤與延伸

不能只因 sender 看似 68005 就完全信任；訊息通道、電信驗證與官方通知政策也要驗證。


### 044. 官方短碼驗證


#### 核心原理

格式驗證與權威白名單必須同時成立。單靠字串外觀可能被偽造或誤認。


#### Python 解答

```python
def is_official_sender(
    sender: str,
    institution_code: str,
    registry: set[str],
) -> bool:
    if len(institution_code) != 3 or not institution_code.isdigit():
        raise ValueError("institution_code 必須是三位數")
    expected = f"68{institution_code}"
    return sender == expected and sender in registry
```


#### 複雜度

O(1) 平均時間、O(1) 空間


#### 常見錯誤與延伸

registry 應來自可信來源並定期更新；快取也需有版本與失效策略。


### 045. TF-IDF 關鍵詞抽取


#### 核心原理

TF-IDF 高分表示某特徵在該文件常見、但在整體文件較少見。中文可用字元 n-gram 避免分詞依賴。


#### Python 解答

```python
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_tfidf_terms(documents, k=5):
    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 4))
    matrix = vectorizer.fit_transform(documents)
    terms = vectorizer.get_feature_names_out()
    results = []
    for row in matrix:
        pairs = [
            (terms[index], float(score))
            for index, score in zip(row.indices, row.data)
            if re.search(r"[\w\u4e00-\u9fff]", terms[index])
        ]
        results.append(sorted(pairs, key=lambda x: (-x[1], x[0]))[:k])
    return results
```


#### 複雜度

約 O(n·d_sparse log d_sparse) 時間、O(n·d_sparse) 空間


#### 常見錯誤與延伸

高 TF-IDF 不一定是業務上重要詞；需搭配停用詞、人工語庫與領域知識。


### 046. 金融文字欄位擷取


#### 核心原理

regex 可做格式固定的實體擷取，但不是完整 NER。金額需去除逗號，日期需再做合法性驗證。


#### Python 解答

```python
import re
from datetime import datetime
from decimal import Decimal

def extract_entities(text: str) -> dict:
    account_match = re.search(r"帳號末四碼\s*(\d{4})", text)
    amount_match = re.search(r"(?:新臺幣|NT\$?)\s*([\d,]+(?:\.\d{1,2})?)\s*元?", text, re.I)
    date_match = re.search(r"(\d{4}[/-]\d{1,2}[/-]\d{1,2})", text)

    parsed_date = None
    if date_match:
        raw = date_match.group(1).replace("/", "-")
        try:
            parsed_date = datetime.strptime(raw, "%Y-%m-%d").date().isoformat()
        except ValueError:
            parsed_date = None

    return {
        "account_last4": account_match.group(1) if account_match else None,
        "amount": (
            Decimal(amount_match.group(1).replace(",", ""))
            if amount_match else None
        ),
        "date": parsed_date,
    }
```


#### 複雜度

O(n) 時間、O(1) 額外空間


#### 常見錯誤與延伸

自由文字可能同時包含多個帳號、金額與日期；正式介面應回傳實體列表與字元位置。


### 047. Logistic Regression 詐欺模型


#### 核心原理

Pipeline 可保證訓練與推論採相同前處理，避免手動縮放錯置。PR-AUC 對稀少正類通常比 ROC-AUC 更具辨識力。


#### Python 解答

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support, average_precision_score

def train_fraud_logistic(train_df, val_df):
    features = ["amount", "tx_count_1h", "new_beneficiary", "device_changed"]
    X_train = train_df[features]
    y_train = train_df["is_fraud"]
    X_val = val_df[features]
    y_val = val_df["is_fraud"]

    model = Pipeline([
        ("scale", StandardScaler()),
        ("clf", LogisticRegression(
            class_weight="balanced",
            max_iter=1000,
            random_state=42,
        )),
    ])
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_val)[:, 1]
    predictions = (probabilities >= 0.5).astype(int)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_val, predictions, average="binary", zero_division=0
    )
    metrics = {
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "pr_auc": float(average_precision_score(y_val, probabilities)),
    }
    return model, metrics
```


#### 複雜度

訓練約 O(n·d·iterations)，空間 O(n·d)


#### 常見錯誤與延伸

0.5 不一定是最佳閾值；正式流程應在 validation 選閾值，test 只做一次最終評估。


### 048. 決策樹與特徵重要度


#### 核心原理

淺樹較容易說明規則路徑，也降低過度擬合。內建 impurity importance 可能偏好高基數或可切分點較多的特徵。


#### Python 解答

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def train_fraud_tree(train_df, features):
    model = DecisionTreeClassifier(
        max_depth=4,
        min_samples_leaf=20,
        class_weight="balanced",
        random_state=42,
    )
    model.fit(train_df[features], train_df["is_fraud"])
    importance = (
        pd.DataFrame({
            "feature": features,
            "importance": model.feature_importances_,
        })
        .sort_values("importance", ascending=False)
        .reset_index(drop=True)
    )
    return model, importance
```


#### 複雜度

最差約 O(n·d·depth)，空間依節點數


#### 常見錯誤與延伸

特徵重要度不是因果關係；高度相關特徵也會分攤或搶走重要度。


### 049. Stratified Cross-Validation


#### 核心原理

StratifiedKFold 盡量維持各折正負類比例。把 scaler 放在 Pipeline 內可避免驗證折資訊洩漏到訓練前處理。


#### Python 解答

```python
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def stratified_cv_scores(df, features):
    model = Pipeline([
        ("scale", StandardScaler()),
        ("clf", LogisticRegression(
            class_weight="balanced",
            max_iter=1000,
            random_state=42,
        )),
    ])
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(
        model,
        df[features],
        df["is_fraud"],
        cv=cv,
        scoring="average_precision",
    )
    return {
        "scores": scores.tolist(),
        "mean": float(np.mean(scores)),
        "std": float(np.std(scores)),
    }
```


#### 複雜度

約 5 倍單次訓練成本


#### 常見錯誤與延伸

若資料有時間順序或同客戶多筆資料，隨機 stratified split 可能洩漏；應改用時間切分或 group split。


### 050. 機率校準


#### 核心原理

分類排序能力與機率校準是不同問題。Brier score 衡量機率誤差；可靠度圖檢查預測機率與實際比例。


#### Python 解答

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss

def calibrated_fraud_model(train_df, val_df, features):
    base = RandomForestClassifier(
        n_estimators=200,
        class_weight="balanced_subsample",
        random_state=42,
        n_jobs=-1,
    )
    model = CalibratedClassifierCV(base, method="sigmoid", cv=3)
    model.fit(train_df[features], train_df["is_fraud"])
    prob = model.predict_proba(val_df[features])[:, 1]

    table = pd.DataFrame({"prob": prob, "label": val_df["is_fraud"].to_numpy()})
    table["bin"] = pd.cut(table["prob"], bins=10, include_lowest=True)
    reliability = (
        table.groupby("bin", observed=True)
        .agg(
            mean_predicted_probability=("prob", "mean"),
            fraction_positive=("label", "mean"),
            count=("label", "size"),
        )
        .reset_index()
    )
    return model, {
        "brier_score": float(brier_score_loss(val_df["is_fraud"], prob)),
        "reliability": reliability,
    }
```


#### 複雜度

約基礎模型訓練的數倍成本


#### 常見錯誤與延伸

校準資料也必須與最終 test 分開；小樣本 bin 的 fraction_positive 會很不穩定。


### 051. ROC-AUC 與 PR-AUC 比較


#### 核心原理

ROC-AUC 衡量隨機正例排在隨機負例之前的機率；在極度不平衡資料上可能看起來很高。
PR-AUC 更聚焦正類，隨機模型 baseline 約等於正類比例。


#### Python 解答

```python
from sklearn.metrics import roc_auc_score, average_precision_score

def ranking_metrics(y_true, probabilities):
    labels = set(y_true)
    if labels != {0, 1}:
        raise ValueError("y_true 必須同時包含 0 與 1")
    positive_rate = sum(y_true) / len(y_true)
    return {
        "roc_auc": float(roc_auc_score(y_true, probabilities)),
        "pr_auc": float(average_precision_score(y_true, probabilities)),
        "pr_baseline": positive_rate,
    }
```


#### 複雜度

O(n log n) 時間、O(n) 空間


#### 常見錯誤與延伸

任何 AUC 都不能取代特定閾值下的誤報、漏報、調查容量與金額損失評估。


### 052. 群體公平性檢查


#### 核心原理

金融 AI 指引要求注意公平性與以人為本。群體指標能發現差異，但差異不必然代表不公平，
也不能只靠單一數字判定合法性或合理性。


#### Python 解答

```python
import pandas as pd
import numpy as np

def fairness_report(df: pd.DataFrame):
    rows = []
    for group, g in df.groupby("group", dropna=False):
        tp = ((g["y_true"] == 1) & (g["y_pred"] == 1)).sum()
        fn = ((g["y_true"] == 1) & (g["y_pred"] == 0)).sum()
        fp = ((g["y_true"] == 0) & (g["y_pred"] == 1)).sum()
        tn = ((g["y_true"] == 0) & (g["y_pred"] == 0)).sum()
        rows.append({
            "group": group,
            "sample_count": len(g),
            "positive_rate": g["y_pred"].mean(),
            "tpr": tp / (tp + fn) if tp + fn else np.nan,
            "fpr": fp / (fp + tn) if fp + tn else np.nan,
        })
    metrics = pd.DataFrame(rows)
    gaps = {}
    for column in ["positive_rate", "tpr", "fpr"]:
        values = metrics[column].dropna()
        gaps[f"{column}_gap"] = (
            float(values.max() - values.min()) if not values.empty else np.nan
        )
    return metrics, gaps
```


#### 複雜度

O(n) 時間、O(g) 空間


#### 常見錯誤與延伸

受保護屬性本身受法規與隱私限制；公平分析需要合法目的、適當治理與足夠樣本。


### 053. 單筆預測理由


#### 核心原理

線性模型的 log-odds 可拆成截距與各特徵貢獻，具有局部可加性。前提是使用與模型完全相同的前處理。


#### Python 解答

```python
import pandas as pd
import numpy as np

def explain_logistic_prediction(pipeline, row, feature_names):
    scaler = pipeline.named_steps["scale"]
    clf = pipeline.named_steps["clf"]
    X = pd.DataFrame([row], columns=feature_names)
    scaled = scaler.transform(X)[0]
    coefficients = clf.coef_[0]
    contributions = scaled * coefficients
    result = pd.DataFrame({
        "feature": feature_names,
        "scaled_value": scaled,
        "coefficient": coefficients,
        "contribution": contributions,
    })
    result["abs_contribution"] = np.abs(result["contribution"])
    return result.sort_values("abs_contribution", ascending=False).reset_index(drop=True)
```


#### 複雜度

O(d) 時間、O(d) 空間


#### 常見錯誤與延伸

相關特徵、非線性與代理變數會影響解讀；說明應使用「推升/降低模型分數」，不是「造成詐欺」。


### 054. 模型保存與版本資訊


#### 核心原理

模型不是只有序列化檔；還需要資料版本、特徵 schema、指標、時間與 checksum，才能追溯與部署。


#### Python 解答

```python
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import joblib

def save_model_bundle(model, path: str, metadata: dict) -> dict:
    required = {
        "model_version", "training_data_version",
        "features", "metrics",
    }
    if not required.issubset(metadata):
        raise ValueError("metadata 缺少必要欄位")

    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    model_path = directory / "model.joblib"
    metadata_path = directory / "metadata.json"

    joblib.dump(model, model_path)
    digest = hashlib.sha256(model_path.read_bytes()).hexdigest()

    document = dict(metadata)
    document["created_at"] = datetime.now(timezone.utc).isoformat()
    document["model_sha256"] = digest
    metadata_path.write_text(
        json.dumps(document, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return {
        "model_path": str(model_path),
        "metadata_path": str(metadata_path),
        "model_sha256": digest,
    }
```


#### 複雜度

序列化時間與空間約 O(model_size)


#### 常見錯誤與延伸

joblib/pickle 不可載入不可信檔案，因可能執行任意程式碼；部署前需驗證來源與 checksum。


### 055. 推論輸入 Schema 驗證


#### 核心原理

模型 API 邊界必須做 schema、型別、範圍與未知欄位檢查。Python 中 bool 是 int 子類，
因此整數欄位要明確排除 bool。


#### Python 解答

```python
def validate_prediction_payload(payload: dict) -> dict:
    allowed = {
        "transaction_id", "amount", "tx_count_1h",
        "new_beneficiary", "device_changed",
    }
    unknown = set(payload) - allowed
    missing = allowed - set(payload)
    if unknown:
        raise ValueError(f"未知欄位: {sorted(unknown)}")
    if missing:
        raise ValueError(f"缺少欄位: {sorted(missing)}")

    tx_id = payload["transaction_id"]
    if not isinstance(tx_id, str) or not tx_id.strip():
        raise ValueError("transaction_id 錯誤")

    amount = payload["amount"]
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("amount 型別錯誤")
    if not 0 <= amount <= 1_000_000_000:
        raise ValueError("amount 範圍錯誤")

    count = payload["tx_count_1h"]
    if isinstance(count, bool) or not isinstance(count, int) or not 0 <= count <= 10_000:
        raise ValueError("tx_count_1h 錯誤")

    for field in ["new_beneficiary", "device_changed"]:
        if not isinstance(payload[field], bool):
            raise ValueError(f"{field} 必須為 bool")

    return {
        **payload,
        "transaction_id": tx_id.strip(),
        "amount": float(amount),
    }
```


#### 複雜度

O(k) 時間、O(k) 空間，k 為欄位數


#### 常見錯誤與延伸

嚴格拒絕未知欄位可避免 silent failure，但 API 升級時要有版本策略。


### 056. FastAPI 模型推論端點


#### 核心原理

模型應在應用啟動時載入，request 路徑只做驗證與推論。回應需可追蹤但不暴露敏感特徵或內部錯誤。


#### Python 解答

```python
from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()
model = None  # 啟動時由受信任的模型載入流程設定
FEATURES = ["amount", "tx_count_1h", "new_beneficiary", "device_changed"]

@app.post("/predict")
def predict(payload: dict):
    if model is None:
        raise HTTPException(status_code=503, detail="model unavailable")
    try:
        data = validate_prediction_payload(payload)
        X = pd.DataFrame([{name: data[name] for name in FEATURES}])
        probability = float(model.predict_proba(X)[0, 1])
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        # 實務應寫入內部安全日誌，不把 stack trace 回傳客戶端
        raise HTTPException(status_code=500, detail="prediction failed") from exc

    return {
        "transaction_id": data["transaction_id"],
        "fraud_probability": probability,
        "decision": "REVIEW" if probability >= 0.7 else "PASS",
    }
```


#### 複雜度

單次推論通常 O(d) 至 O(t·depth)，視模型而定


#### 常見錯誤與延伸

真實服務需加上驗證授權、TLS、rate limit、request ID、timeout、監控與模型版本回傳。


### 057. 批次評分管線


#### 核心原理

chunked read 控制記憶體；輸出要包含模型版本與時間。錯誤處理需明確區分整批 schema 錯誤與逐列資料錯誤。


#### Python 解答

```python
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

def batch_score_csv(
    input_path, output_path, error_path,
    model, model_version,
):
    output_path = Path(output_path)
    error_path = Path(error_path)
    first_output = True
    error_frames = []
    features = ["amount", "tx_count_1h", "new_beneficiary", "device_changed"]

    for chunk_no, chunk in enumerate(pd.read_csv(input_path, chunksize=50_000), start=1):
        valid_rows = []
        invalid_rows = []
        for index, row in chunk.iterrows():
            try:
                payload = validate_prediction_payload(row.to_dict())
                valid_rows.append(payload)
            except ValueError as exc:
                bad = row.to_dict()
                bad["chunk_no"] = chunk_no
                bad["source_index"] = index
                bad["error"] = str(exc)
                invalid_rows.append(bad)

        if invalid_rows:
            error_frames.append(pd.DataFrame(invalid_rows))
        if not valid_rows:
            continue

        valid = pd.DataFrame(valid_rows)
        valid["fraud_probability"] = model.predict_proba(valid[features])[:, 1]
        valid["model_version"] = model_version
        valid["scored_at"] = datetime.now(timezone.utc).isoformat()

        # Parquet append 依引擎支援不同；此示範每批輸出獨立 partition
        partition = output_path / f"part-{chunk_no:05d}.parquet"
        partition.parent.mkdir(parents=True, exist_ok=True)
        valid.to_parquet(partition, index=False)
        first_output = False

    if error_frames:
        pd.concat(error_frames, ignore_index=True).to_csv(error_path, index=False)
    if first_output:
        raise RuntimeError("沒有任何有效資料被評分")
```


#### 複雜度

O(n·model_cost) 時間、O(chunk_size) 記憶體


#### 常見錯誤與延伸

逐列 iterrows 較慢但便於示範錯誤隔離；正式管線可採向量化 schema 驗證或專用驗證框架。


### 058. Population Stability Index


#### 核心原理

PSI 將兩期分布離散化比較。bin 必須由 reference 建立，不能每期各自重算，否則失去可比性。


#### Python 解答

```python
import numpy as np
import pandas as pd

def population_stability_index(reference, current, bins=10):
    ref = np.asarray(reference, dtype=float)
    cur = np.asarray(current, dtype=float)
    if ref.size == 0 or cur.size == 0:
        raise ValueError("資料不可為空")
    edges = np.unique(np.quantile(ref, np.linspace(0, 1, bins + 1)))
    if len(edges) < 2:
        raise ValueError("reference 無足夠變異")
    edges[0], edges[-1] = -np.inf, np.inf

    ref_counts, _ = np.histogram(ref, bins=edges)
    cur_counts, _ = np.histogram(cur, bins=edges)
    epsilon = 1e-6
    ref_pct = np.clip(ref_counts / ref_counts.sum(), epsilon, None)
    cur_pct = np.clip(cur_counts / cur_counts.sum(), epsilon, None)
    contributions = (cur_pct - ref_pct) * np.log(cur_pct / ref_pct)

    table = pd.DataFrame({
        "left": edges[:-1],
        "right": edges[1:],
        "reference_pct": ref_pct,
        "current_pct": cur_pct,
        "psi_contribution": contributions,
    })
    return float(contributions.sum()), table
```


#### 複雜度

O((n+m) log n) 主要來自分位數、O(bins) 額外空間


#### 常見錯誤與延伸

PSI 不告訴你漂移原因或是否影響模型績效；需搭配特徵、標籤與業務監控。


### 059. Kolmogorov–Smirnov 漂移檢定


#### 核心原理

KS statistic 衡量兩個經驗累積分布最大差距。結合顯著性與效果量門檻，比只看 p-value 更實用。


#### Python 解答

```python
import numpy as np
from scipy.stats import ks_2samp

def ks_drift_test(reference, current, alpha=0.01, min_effect=0.1):
    ref = np.asarray(reference, dtype=float)
    cur = np.asarray(current, dtype=float)
    ref = ref[np.isfinite(ref)]
    cur = cur[np.isfinite(cur)]
    if len(ref) < 20 or len(cur) < 20:
        raise ValueError("樣本數不足")
    result = ks_2samp(ref, cur, alternative="two-sided", method="auto")
    return {
        "statistic": float(result.statistic),
        "p_value": float(result.pvalue),
        "drifted": result.pvalue < alpha and result.statistic >= min_effect,
    }
```


#### 複雜度

約 O((n+m) log(n+m)) 時間、O(n+m) 空間


#### 常見錯誤與延伸

多特徵同時檢定會有多重比較問題；可採 FDR 控制並配合業務重要性排序。


### 060. 模型績效監控


#### 核心原理

詐欺真實標籤常延遲數週或數月，監控必須揭露 label coverage 與延遲，否則近期績效可能失真。


#### Python 解答

```python
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

def monthly_model_performance(scored, labels):
    s = scored.copy()
    l = labels.copy()
    s["scored_at"] = pd.to_datetime(s["scored_at"], errors="raise")
    l["label_at"] = pd.to_datetime(l["label_at"], errors="raise")
    data = s.merge(l, on="tx_id", how="left", validate="one_to_one")
    data["month"] = data["scored_at"].dt.to_period("M").astype(str)
    data["label_delay_days"] = (
        data["label_at"] - data["scored_at"]
    ).dt.total_seconds() / 86400

    rows = []
    for month, group in data.groupby("month"):
        labeled = group.dropna(subset=["label"])
        row = {
            "month": month,
            "scored_count": len(group),
            "labeled_count": len(labeled),
            "coverage": len(labeled) / len(group) if len(group) else 0,
            "avg_label_delay_days": labeled["label_delay_days"].mean(),
        }
        if len(labeled):
            y_true = labeled["label"].astype(int)
            y_pred = labeled["prediction"].astype(int)
            row.update({
                "precision": precision_score(y_true, y_pred, zero_division=0),
                "recall": recall_score(y_true, y_pred, zero_division=0),
                "f1": f1_score(y_true, y_pred, zero_division=0),
            })
        else:
            row.update({"precision": None, "recall": None, "f1": None})
        rows.append(row)
    return pd.DataFrame(rows).sort_values("month").reset_index(drop=True)
```


#### 複雜度

O(n log n) 以 join/groupby 為主、O(n) 空間


#### 常見錯誤與延伸

標籤回補可能有選擇偏誤，例如只有被調查的告警有標籤；需設計抽樣與回饋機制。


### 061. 不可竄改稽核日誌雜湊鏈


#### 核心原理

雜湊鏈能偵測內容被修改或刪改順序，但不能防止有權限者重寫整條鏈；仍需外部時間戳、權限與備份。


#### Python 解答

```python
import hashlib
import json

def _record_hash(record_without_hash):
    payload = json.dumps(
        record_without_hash,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

def append_audit_record(records, event):
    record = {
        "timestamp": event["timestamp"],
        "actor": event["actor"],
        "action": event["action"],
        "object_id": event["object_id"],
        "details": event.get("details", {}),
        "prev_hash": records[-1]["hash"] if records else "GENESIS",
    }
    record["hash"] = _record_hash(record)
    records.append(record)
    return record

def verify_chain(records) -> bool:
    previous = "GENESIS"
    for record in records:
        if record.get("prev_hash") != previous:
            return False
        content = {k: v for k, v in record.items() if k != "hash"}
        if record.get("hash") != _record_hash(content):
            return False
        previous = record["hash"]
    return True
```


#### 複雜度

O(n) 驗證時間、O(1) 額外空間


#### 常見錯誤與延伸

日誌 details 不應直接放敏感資料；應記錄必要摘要、識別碼與權限受控的查詢連結。


### 062. 客戶識別碼假名化


#### 核心原理

一般 SHA-256 對可猜測 ID 容易字典反推；HMAC 使用秘密金鑰，適合穩定假名化。
假名化仍屬可重新連結資料，不等同匿名化。


#### Python 解答

```python
import hashlib
import hmac

def pseudonymize_customer_id(customer_id: str, secret_key: bytes) -> str:
    if not customer_id:
        raise ValueError("customer_id 不可為空")
    if not isinstance(secret_key, bytes) or len(secret_key) < 32:
        raise ValueError("secret_key 至少 32 bytes")
    digest = hmac.new(
        secret_key,
        customer_id.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return digest[:24]
```


#### 複雜度

O(n) 時間，n 為 ID 長度；O(1) 空間


#### 常見錯誤與延伸

金鑰需交由 KMS/HSM 管理與輪替；不可硬編碼在原始碼或 notebook。


### 063. 角色權限檢查


#### 核心原理

預設拒絕（deny by default）與最小權限是金融系統基本原則。權限表應由集中政策管理並有稽核。


#### Python 解答

```python
PERMISSIONS = {
    "ANALYST": {
        ("read", "masked_transactions"),
        ("run", "model"),
    },
    "REVIEWER": {
        ("read", "masked_transactions"),
        ("review", "alert"),
    },
    "ADMIN": {
        ("manage", "model"),
        ("read", "audit"),
    },
}

def authorize(role: str, action: str, resource: str) -> dict:
    allowed = (action, resource) in PERMISSIONS.get(role, set())
    return {
        "allowed": allowed,
        "reason": "ALLOWED_BY_ROLE" if allowed else "DENY_BY_DEFAULT",
    }
```


#### 複雜度

O(1) 平均時間、O(1) 額外空間


#### 常見錯誤與延伸

角色名稱本身必須由可信身份系統驗證；不能接受客戶端自行傳入 role 就相信。


### 064. RPA 重試與冪等性


#### 核心原理

金融自動化最怕重複執行。冪等 key 先查成功紀錄；重試只針對可恢復錯誤，並限制次數。


#### Python 解答

```python
import time

class TemporaryError(Exception):
    pass

class PermanentError(Exception):
    pass

def execute_with_retry(
    operation,
    idempotency_key,
    store,
    max_attempts=3,
):
    if idempotency_key in store:
        return store[idempotency_key]

    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            result = operation(idempotency_key)
            store[idempotency_key] = result
            return result
        except PermanentError:
            raise
        except TemporaryError as exc:
            last_error = exc
            if attempt == max_attempts:
                break
            time.sleep(2 ** (attempt - 1))
    raise TemporaryError("已達最大重試次數") from last_error
```


#### 複雜度

成功平均 O(1) 外加外部 operation 成本；空間 O(k) 儲存成功 key


#### 常見錯誤與延伸

單機 dict 無法提供跨程序原子性。正式系統需資料庫唯一鍵、交易或具原子操作的 idempotency store。


### 065. 端到端可疑交易決策管線


#### 核心原理

銀行 AI 應用通常不是單一模型，而是資料驗證、規則、模型、人工覆核、日誌與降級策略的組合。
此題綜合考察安全邊界、可解釋性、可靠性與治理。


#### Python 解答

```python
from datetime import datetime, timezone
import pandas as pd

FEATURES = ["amount", "tx_count_1h", "new_beneficiary", "device_changed"]

def decide_transaction(payload, model, model_version, audit_sink):
    timestamp = datetime.now(timezone.utc).isoformat()
    try:
        data = validate_prediction_payload(payload)
    except ValueError as exc:
        result = {
            "transaction_id": payload.get("transaction_id"),
            "decision": "REJECT_DATA",
            "reason_codes": ["INVALID_SCHEMA"],
            "detail": str(exc),
            "model_version": model_version,
        }
        audit_sink.append({"timestamp": timestamp, **result})
        return result

    rule_result = fraud_rule_score({
        "amount": data["amount"],
        "hour": payload.get("hour", 12),
        "is_new_beneficiary": data["new_beneficiary"],
        "device_changed": data["device_changed"],
        "country_risk": payload.get("country_risk", "LOW"),
    })
    probability = None
    model_error = None
    if model is not None:
        try:
            X = pd.DataFrame([{name: data[name] for name in FEATURES}])
            probability = float(model.predict_proba(X)[0, 1])
        except Exception as exc:
            model_error = type(exc).__name__

    reasons = list(rule_result["reasons"])
    if model_error:
        reasons.append("MODEL_UNAVAILABLE")
        decision = (
            "REVIEW" if rule_result["score"] >= 60
            else "PASS_WITH_MODEL_UNAVAILABLE"
        )
    elif rule_result["score"] >= 80:
        decision = "BLOCK_AND_REVIEW"
        reasons.append("RULE_SCORE_CRITICAL")
    elif probability >= 0.7 or rule_result["score"] >= 60:
        decision = "REVIEW"
        if probability >= 0.7:
            reasons.append("MODEL_HIGH_RISK")
    else:
        decision = "PASS"

    result = {
        "transaction_id": data["transaction_id"],
        "decision": decision,
        "rule_score": rule_result["score"],
        "model_probability": probability,
        "reason_codes": reasons,
        "model_version": model_version,
    }
    audit_sink.append({"timestamp": timestamp, **result})
    return result
```


#### 複雜度

單筆成本為 O(model inference)；額外空間 O(1)


#### 常見錯誤與延伸

示範閾值與規則不可直接用於生產。正式設計需雙人覆核、申訴/救濟、壓力測試、監控、變更審批與事故應變。

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
