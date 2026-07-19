# 2026 土地銀行 AI 應用人員：Python 應用實作題


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


## 二、AI 應用人員 Code 題重點架構

| 模組 | 土地銀行情境 | 主要 Python 能力 |
|---|---|---|
| 資料工程 | 報表、稅籍資料、客戶 360、RPA | pandas、schema、清洗、join、groupby、對帳 |
| 異常／識詐 | 鷹眼聯盟、可疑交易、ATM 防詐 | 規則、滑動視窗、圖論、Isolation Forest、閾值 |
| NLP／智能客服 | 金融語庫、FAQ、熱搜、客服轉人工 | Unicode、regex、TF-IDF、cosine、信心門檻 |
| 法令遵循 | CRA 外規與內規比對 | 文件分塊、相似度、diff、來源與版本 |
| 模型開發 | ML/DL 建模、評估與優化 | Pipeline、CV、PR-AUC、校準、公平性、解釋 |
| MLOps／治理 | 模型上線與金融 AI 指引 | API、版本、漂移、監控、RBAC、稽核、降級 |

### 應用題的高分回答框架

1. **先界定問題是規則、統計、ML、NLP 還是系統題。**
2. **資料先於模型**：schema、缺失、重複、時間順序、資料洩漏。
3. **模型不等於決策**：明確寫出 threshold、人工覆核、fallback。
4. **不平衡分類要談 Precision、Recall、PR-AUC 與錯誤成本。**
5. **金融系統要談可追溯**：reason code、model version、audit log。
6. **金融 AI 要談治理**：公平、隱私、安全、第三方、申訴與人類可控。



## ??????

? **40 ?**???????? **80 ?**??????? 3 ??? 27 ????

- [ ] 001. 交易資料清洗管線?初階?
- [ ] 002. 分行月度 KPI 報表?初階?
- [ ] 003. 重複交易偵測?初階?
- [ ] 004. 餘額序列一致性檢查?初階?
- [ ] 005. 滾動平均與異常尖峰?初階?
- [ ] 006. 信用額度使用率告警?初階?
- [ ] 007. 客戶 360 彙總?初階?
- [ ] 008. 規則式詐欺風險分數?初階?
- [ ] 009. 短時間大量交易 Velocity Rule?初階?
- [ ] 010. 拆單（Structuring）偵測?中階?
- [ ] 011. 深夜 ATM 提款異常?初階?
- [ ] 012. 不可能移動（Impossible Travel）?中階?
- [ ] 013. 新受款人高額轉帳?初階?
- [ ] 014. ATM 臉部遮蔽判定邏輯?初階?
- [ ] 015. 混淆矩陣實作?初階?
- [ ] 016. Precision、Recall、F1?初階?
- [ ] 017. 成本敏感閾值選擇?中階?
- [ ] 018. Isolation Forest 異常偵測?中階?
- [ ] 019. Robust Z-score（MAD）?中階?
- [ ] 020. 交易特徵工程?中階?
- [ ] 021. 時間序列切分?中階?
- [ ] 022. 即時告警去重與冷卻時間?中階?
- [ ] 023. 智能客服意圖規則分類器?初階?
- [ ] 024. 中文文字正規化?初階?
- [ ] 025. FAQ TF-IDF 檢索?中階?
- [ ] 026. 客服日誌敏感資料遮罩?中階?
- [ ] 027. Prompt Injection 基礎防護?中階?
- [ ] 028. 低信心回答轉人工?中階?
- [ ] 029. 釣魚簡訊特徵擷取?中階?
- [ ] 030. 官方短碼驗證?初階?
- [ ] 031. Logistic Regression 詐欺模型?中階?
- [ ] 032. Stratified Cross-Validation?中階?
- [ ] 033. ROC-AUC 與 PR-AUC 比較?中階?
- [ ] 034. 群體公平性檢查?中階?
- [ ] 035. 推論輸入 Schema 驗證?中階?
- [ ] 036. 模型績效監控?中階?
- [ ] 037. 不可竄改稽核日誌雜湊鏈?中階?
- [ ] 038. 客戶識別碼假名化?中階?
- [ ] 039. 角色權限檢查?中階?
- [ ] 040. 端到端可疑交易決策管線?進階?

---

## ?????


### 001. 交易資料清洗管線


- **難度：** 初階
- **案例對應：** 大數據分析、資料清洗


#### 題目

輸入 pandas DataFrame，欄位為 `tx_id, account_id, timestamp, amount, channel`。
完成：移除完全重複列、tx_id 重複時保留 timestamp 較早者、timestamp 轉 datetime、
amount 轉數值並移除負數或缺失、channel 轉大寫。回傳 `(clean_df, rejected_df)`，
rejected_df 要保留被拒絕原因。


#### 建議函式／介面

```python
def clean_transactions(df):
```


### 002. 分行月度 KPI 報表


- **難度：** 初階
- **案例對應：** 大數據分析、Tableau 前處理


#### 題目

DataFrame 含 `branch, timestamp, amount, status`。只計算 status=`SUCCESS` 的交易，
輸出每分行每月：交易筆數、總金額、平均金額、月增率。月增率分母為上月總金額，首月為 NaN。


#### 建議函式／介面

```python
def branch_monthly_kpi(df):
```


### 003. 重複交易偵測


- **難度：** 初階
- **案例對應：** RPA 對帳、資料品質


#### 題目

交易含 `account_id, amount, timestamp, merchant`。若同帳戶、同商戶、同金額在 2 分鐘內出現，
視為可能重複交易。回傳所有被判定為後續重複的列，並加入 `previous_tx_id`。


#### 建議函式／介面

```python
def find_duplicate_transactions(df):
```


### 004. 餘額序列一致性檢查


- **難度：** 初階
- **案例對應：** 帳務驗證、資料品質


#### 題目

每筆紀錄含 `account_id, timestamp, type(DEBIT/CREDIT), amount, balance_after`。
檢查同帳戶相鄰交易是否符合：前餘額 ± amount = balance_after。
第一筆沒有前餘額時略過。回傳不一致紀錄及預期餘額。


#### 建議函式／介面

```python
def validate_balance_sequence(df):
```


### 005. 滾動平均與異常尖峰


- **難度：** 初階
- **案例對應：** 異常偵測、時間序列


#### 題目

依帳戶計算前 7 筆交易金額的平均與標準差（不含當前筆）。
若當前金額大於平均 + 3×標準差，標記 `is_spike=True`。歷史不足 3 筆不標記。


#### 建議函式／介面

```python
def flag_amount_spikes(df):
```


### 006. 信用額度使用率告警


- **難度：** 初階
- **案例對應：** 規則引擎、分級


#### 題目

輸入客戶額度與未償餘額，計算 utilization=balance/limit。
<70% NORMAL，70%~<90% WATCH，>=90% HIGH。limit<=0 視為資料錯誤。
回傳原資料加 utilization 與 alert_level。


#### 建議函式／介面

```python
def credit_utilization_alert(df):
```


### 007. 客戶 360 彙總


- **難度：** 初階
- **案例對應：** 資料整合、groupby、merge


#### 題目

customers、accounts、transactions 三張表。產出每位客戶：
帳戶數、近 90 日交易總額、近 90 日交易筆數、最後交易時間。
沒有交易的客戶也要保留，數值補 0。


#### 建議函式／介面

```python
def build_customer_360(customers, accounts, transactions, as_of):
```


### 008. 規則式詐欺風險分數


- **難度：** 初階
- **案例對應：** AI識詐、規則引擎


#### 題目

每筆交易有 amount、hour、is_new_beneficiary、device_changed、country_risk。
設計可設定權重的 risk score：
amount>=100000 +30；hour 0~5 +15；new beneficiary +20；device_changed +20；
country_risk HIGH +25。分數上限 100，>=60 需人工審查。


#### 建議函式／介面

```python
def fraud_rule_score(tx):
```


### 009. 短時間大量交易 Velocity Rule


- **難度：** 初階
- **案例對應：** 詐欺偵測、deque


#### 題目

交易流已依時間排序。對每個帳戶，在 10 分鐘視窗內若交易筆數 >=5 或總額 >=200000，
對當前交易產生告警。實作單機串流版本。


#### 建議函式／介面

```python
def velocity_alerts(transactions):
```


### 010. 拆單（Structuring）偵測


- **難度：** 中階
- **案例對應：** 洗錢防制、時間視窗


#### 題目

同帳戶在 24 小時內出現至少 3 筆、每筆介於 80,000~99,999，且總額 >=250,000，
標記為疑似拆單。輸出帳戶、視窗起訖、筆數、總額與交易 ID。


#### 建議函式／介面

```python
def detect_structuring(df):
```


### 011. 深夜 ATM 提款異常


- **難度：** 初階
- **案例對應：** ATM 防詐、行為基線


#### 題目

每個客戶有歷史常用提款時段 `usual_start, usual_end` 與平均提款金額。
若 ATM 提款發生在常用時段外，且金額 > 2×平均，標記。
需正確處理常用時段跨午夜（例如 22 到 6）。


#### 建議函式／介面

```python
def is_unusual_atm_withdrawal(tx, profile):
```


### 012. 不可能移動（Impossible Travel）


- **難度：** 中階
- **案例對應：** 地理異常、Haversine


#### 題目

同一帳戶連續兩筆交易有經緯度與時間。計算球面距離與所需平均速度，
若速度 > 900 km/h 且時間差 >0，標記異常。實作 Haversine。


#### 建議函式／介面

```python
def impossible_travel(prev_tx, current_tx):
```


### 013. 新受款人高額轉帳


- **難度：** 初階
- **案例對應：** 防詐規則、集合


#### 題目

輸入客戶歷史受款人集合與新交易。若受款人第一次出現且金額 >=100000，回傳告警與原因；
否則不告警。受款人 ID 缺失視為資料錯誤。


#### 建議函式／介面

```python
def new_beneficiary_alert(tx, known_beneficiaries):
```


### 014. ATM 臉部遮蔽判定邏輯


- **難度：** 初階
- **案例對應：** AI臉部辨識、防詐模組


#### 題目

已知上游視覺模型輸出：face_detected、occlusion_ratio、confidence。
若未偵測到臉，或 occlusion_ratio>=0.4，或 confidence<0.7，回傳 `RETRY`；
連續 3 次 RETRY 後回傳 `ESCALATE`，其餘 `PASS`。只實作決策層，不訓練影像模型。


#### 建議函式／介面

```python
def atm_face_decision(result, retry_count):
```


### 015. 混淆矩陣實作


- **難度：** 初階
- **案例對應：** 模型評估、分類


#### 題目

給定 y_true 與 y_pred（0/1），計算 TP、FP、TN、FN。長度不一致或含其他值要拋出錯誤。


#### 建議函式／介面

```python
def confusion_counts(y_true, y_pred):
```


### 016. Precision、Recall、F1


- **難度：** 初階
- **案例對應：** 模型評估、不平衡資料


#### 題目

使用 TP、FP、FN 計算 precision、recall、F1。分母為 0 時回傳 0，不得拋 ZeroDivisionError。


#### 建議函式／介面

```python
def classification_metrics(tp, fp, fn):
```


### 017. 成本敏感閾值選擇


- **難度：** 中階
- **案例對應：** threshold、期望成本


#### 題目

輸入真實標籤、預測機率、候選閾值、FP 成本與 FN 成本。
計算每個閾值總成本 `FP*fp_cost + FN*fn_cost`，回傳成本最低閾值；
成本相同時選較高閾值。


#### 建議函式／介面

```python
def choose_threshold(y_true, probabilities, thresholds, fp_cost, fn_cost):
```


### 018. Isolation Forest 異常偵測


- **難度：** 中階
- **案例對應：** 異常帳戶分析、機器學習


#### 題目

以特徵 `amount, tx_count_1h, new_beneficiary, device_age_days` 訓練 IsolationForest。
回傳原資料加 `anomaly_score` 與 `is_anomaly`。設定 random_state，並讓 contamination 可傳入。


#### 建議函式／介面

```python
def isolation_forest_flags(df, contamination=0.01):
```


### 019. Robust Z-score（MAD）


- **難度：** 中階
- **案例對應：** 異常偵測、穩健統計


#### 題目

實作 `modified_z_scores(values)`，使用 median 與 MAD：
`0.6745*(x-median)/MAD`。MAD=0 時，與 median 相同者分數 0，不同者回傳正負 infinity。


#### 建議函式／介面

```python
def modified_z_scores(values):
```


### 020. 交易特徵工程


- **難度：** 中階
- **案例對應：** 特徵工程、時間與行為


#### 題目

DataFrame 已按帳戶與時間排序。新增：
`hour`、`is_weekend`、`time_since_prev_min`、`amount_vs_account_median`、
`beneficiary_seen_before`。第一筆時間差為 NaN。


#### 建議函式／介面

```python
def engineer_transaction_features(df):
```


### 021. 時間序列切分


- **難度：** 中階
- **案例對應：** train/validation/test、資料洩漏


#### 題目

依 timestamp 把資料切成最早 70% train、中間 15% validation、最後 15% test。
同一 timestamp 的資料不得被拆到不同集合；回傳三個 DataFrame。


#### 建議函式／介面

```python
def temporal_split(df, train_ratio=0.7, val_ratio=0.15):
```


### 022. 即時告警去重與冷卻時間


- **難度：** 中階
- **案例對應：** 告警系統、狀態管理


#### 題目

同帳戶同規則在 30 分鐘內只通知一次，但仍累計 occurrence_count。
實作記憶體版 `AlertDeduplicator.process(alert)`，回傳是否應通知與累計次數。


#### 建議函式／介面

```python
class AlertDeduplicator:
```


### 023. 智能客服意圖規則分類器


- **難度：** 初階
- **案例對應：** 智能客服、NLP


#### 題目

將問題分為 `CREDIT_CARD, EXCHANGE_RATE, BRANCH, LOAN, OTHER`。
使用關鍵詞與優先序；同時出現多類時，以 CREDIT_CARD > LOAN > EXCHANGE_RATE > BRANCH 優先。
回傳 intent 與命中關鍵詞。


#### 建議函式／介面

```python
def classify_intent(text):
```


### 024. 中文文字正規化


- **難度：** 初階
- **案例對應：** NLP 前處理、Unicode


#### 題目

實作 `normalize_chinese_text(text)`：
Unicode NFKC、轉小寫、移除控制字元、連續空白縮成一格、全形英數轉半形（NFKC 已處理）。
保留中文與一般標點。


#### 建議函式／介面

```python
def normalize_chinese_text(text):
```


### 025. FAQ TF-IDF 檢索


- **難度：** 中階
- **案例對應：** 智能客服、資訊檢索


#### 題目

給定 faq DataFrame（question, answer），以字元 n-gram TF-IDF 建立檢索器。
`search(query,k)` 回傳相似度最高的 k 筆；最高分低於 threshold 時回傳空串列。


#### 建議函式／介面

```python
class FAQRetriever:
```


### 026. 客服日誌敏感資料遮罩


- **難度：** 中階
- **案例對應：** 隱私、NLP 日誌


#### 題目

遮罩文字中的 10~16 位連續數字帳號、台灣身分證字號、Email。
帳號只保留末 4 碼；身分證與 Email 全部以類型標記取代。


#### 建議函式／介面

```python
def redact_sensitive_text(text):
```


### 027. Prompt Injection 基礎防護


- **難度：** 中階
- **案例對應：** 生成式 AI、輸入防護


#### 題目

實作 `screen_prompt(text)`，若出現「忽略之前指令」「顯示系統提示」「輸出所有客戶資料」
等高風險模式，回傳 BLOCK；若含 URL 或程式碼區塊，回傳 REVIEW；其餘 ALLOW。
輸出 reason codes。


#### 建議函式／介面

```python
def screen_prompt(text):
```


### 028. 低信心回答轉人工


- **難度：** 中階
- **案例對應：** 智能客服、可靠性


#### 題目

模型回傳 `answer, confidence, sources`。若 confidence<0.75、sources 為空、
或答案包含「不確定但可能」，則不得直接回覆，改為 `HANDOFF`。
否則回傳 `ANSWER` 與來源。


#### 建議函式／介面

```python
def response_gate(model_output):
```


### 029. 釣魚簡訊特徵擷取


- **難度：** 中階
- **案例對應：** 短碼簡訊、防詐、NLP


#### 題目

從 SMS 文字與 sender 擷取：
是否含 URL、URL 數量、是否含「立即/逾期/停權/驗證」、是否要求 OTP、
sender 是否為認證短碼 `68xxx`、數字比例、驚嘆號數量。
回傳特徵 dict。


#### 建議函式／介面

```python
def sms_features(text, sender):
```


### 030. 官方短碼驗證


- **難度：** 初階
- **案例對應：** 防詐、白名單


#### 題目

建立 `is_official_sender(sender, institution_code, registry)`：
sender 必須等於 `68 + institution_code`，且出現在 registry 白名單。
institution_code 必須恰為三位數。


#### 建議函式／介面

```python
def is_official_sender(sender, institution_code, registry):
```


### 031. Logistic Regression 詐欺模型


- **難度：** 中階
- **案例對應：** 機器學習、詐欺偵測


#### 題目

使用欄位 `amount, tx_count_1h, new_beneficiary, device_changed` 訓練 LogisticRegression。
建立含 StandardScaler 的 Pipeline，設定 class_weight="balanced"、random_state=42，
回傳模型與 validation 的 precision、recall、F1、PR-AUC。


#### 建議函式／介面

```python
def train_fraud_logistic(train_df, val_df):
```


### 032. Stratified Cross-Validation


- **難度：** 中階
- **案例對應：** 模型驗證、類別不平衡


#### 題目

使用 StratifiedKFold 做 5 折交叉驗證，評估 LogisticRegression Pipeline 的 average precision。
回傳每折分數、平均與標準差。不得先在全資料 fit scaler。


#### 建議函式／介面

```python
def stratified_cv_scores(df, features):
```


### 033. ROC-AUC 與 PR-AUC 比較


- **難度：** 中階
- **案例對應：** 模型評估、不平衡資料


#### 題目

給定 y_true 與 probabilities，計算 ROC-AUC、PR-AUC 與正類比例 baseline。
若 y_true 只有單一類別，拋出 ValueError。


#### 建議函式／介面

```python
def ranking_metrics(y_true, probabilities):
```


### 034. 群體公平性檢查


- **難度：** 中階
- **案例對應：** 金融 AI 治理、公平性


#### 題目

DataFrame 含 `group, y_true, y_pred`。對各 group 計算 sample_count、positive_rate、
TPR(recall)、FPR。再計算各指標最大最小差距。
分母為 0 時回傳 NaN。


#### 建議函式／介面

```python
def fairness_report(df):
```


### 035. 推論輸入 Schema 驗證


- **難度：** 中階
- **案例對應：** API、資料驗證、安全


#### 題目

使用 dataclass 或純 Python 實作 `validate_prediction_payload(payload)`。
必要欄位：transaction_id(str 非空)、amount(0~1e9)、tx_count_1h(int 0~10000)、
new_beneficiary(bool)、device_changed(bool)。拒絕未知欄位。


#### 建議函式／介面

```python
def validate_prediction_payload(payload):
```


### 036. 模型績效監控


- **難度：** 中階
- **案例對應：** MLOps、延遲標籤


#### 題目

給定 scored 資料（tx_id, probability, prediction, scored_at）與日後回補 labels（tx_id, label, label_at）。
依評分月份計算 coverage、precision、recall、F1、平均標籤延遲天數。
只對已回補標籤計算分類指標。


#### 建議函式／介面

```python
def monthly_model_performance(scored, labels):
```


### 037. 不可竄改稽核日誌雜湊鏈


- **難度：** 中階
- **案例對應：** AI 治理、稽核、hash chain


#### 題目

實作 append-only audit log。每筆包含 timestamp、actor、action、object_id、details、prev_hash、hash。
hash 為前述欄位 canonical JSON 的 SHA-256。再實作 `verify_chain(records)`。


#### 建議函式／介面

```python
def append_audit_record(records, event)):
```


### 038. 客戶識別碼假名化


- **難度：** 中階
- **案例對應：** 隱私、HMAC、資料最小化


#### 題目

實作 `pseudonymize_customer_id(customer_id, secret_key)`，
用 HMAC-SHA256 產生穩定 token，取前 24 個 hex 字元。空 ID 或太短 key 拋出錯誤。


#### 建議函式／介面

```python
def pseudonymize_customer_id(customer_id, secret_key):
```


### 039. 角色權限檢查


- **難度：** 中階
- **案例對應：** RBAC、最小權限


#### 題目

建立 `authorize(role, action, resource)`。角色：
ANALYST 可 read masked_transactions、run_model；
REVIEWER 可 read masked_transactions、review_alert；
ADMIN 可 manage_model、read_audit。
任何未明列組合拒絕。回傳 bool 與 reason。


#### 建議函式／介面

```python
def authorize(role, action, resource):
```


### 040. 端到端可疑交易決策管線


- **難度：** 進階
- **案例對應：** AI識詐、規則＋模型＋人工覆核


#### 題目

整合規則分數、模型機率與資料品質：
1. schema 無效 -> REJECT_DATA；
2. 規則分數>=80 -> BLOCK_AND_REVIEW；
3. 模型機率>=0.7 或規則分數>=60 -> REVIEW；
4. 其餘 PASS。
輸出 decision、rule_score、model_probability、reason_codes、model_version，
並寫入 audit sink。模型失效時採保守降級：規則>=60 REVIEW，否則 PASS_WITH_MODEL_UNAVAILABLE。


#### 建議函式／介面

```python
def decide_transaction(payload, model, model_version, audit_sink):
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
