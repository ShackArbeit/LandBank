# 2026 土地銀行 AI 人員等考試：AI應用規劃師科目1重點架構整理

**目標**：通過 2026/8/22 土地銀行 AI 人員等考試  
**每日讀書時間**：1 小時  
**準備比重**：專業科目 90%，共同科目 10%（考前最後一週處理）  
**本檔定位**：把附件 PDF 的「AI應用規劃師：人工智慧技術應用與規劃」改寫成符合「土地銀行 AI 人員」可能命題方向的重點架構。

---

## 0. 先講結論：土地銀行 AI 人員考試最可能考什麼？

這份 PDF 不只是背名詞，它的核心是：

> **你能不能把 AI 技術，放進銀行真實業務流程中，並說清楚價值、資料、模型、部署、風險與治理。**

因此，準備方向不要只背「BERT、CNN、RAG、LoRA 是什麼」，而要能回答：

1. **這個銀行場景有什麼痛點？**
2. **適合用哪種 AI 技術？為什麼不是別種？**
3. **資料從哪裡來？資料品質、個資、標註怎麼處理？**
4. **模型如何選擇、訓練、評估、部署、監控？**
5. **若用在金融業，如何控管公平性、可解釋性、資安、法遵、第三方風險？**
6. **若要寫 Python/Java，如何把資料處理、模型推論、API 串接寫成清楚流程？**

---

## 1. 土地銀行近期 AI / 數位金融案例：命題連結地圖

| 土銀公開案例 | 可能考點 | 對應 PDF 重點 | 你要會寫出的關鍵字 |
|---|---|---|---|
| 智能客服：24小時線上業務諮詢、金融專業語庫、常問問題推薦 | NLP、FAQ分類、意圖辨識、RAG、客服知識庫、人工轉接 | 3.1 NLP、3.3 生成式 AI、4.3 風險管理、5.2 系統部署 | Tokenization、Embedding、BERT/GPT、RAG、Hallucination、Fallback、客服紀錄去識別化 |
| ATM 導入 AI 臉部辨識防詐模組 | 電腦視覺、臉部遮蔽偵測、邊緣部署、防詐 | 3.2 電腦視覺、4.1 AI導入評估、4.3 AI風險管理 | CNN、Object Detection、False Positive/Negative、模型偏誤、Edge AI、個資保護 |
| RPA 流程自動化：報表產製、數據統計、稅務申報、人事管理 | 流程自動化、AI與RPA差異、內部效率提升 | 4.1 導入評估、4.2 導入規劃、5.2 系統整合 | As-Is/To-Be、流程盤點、ROI、人為錯誤降低、例外處理 |
| 大數據分析：Tableau 視覺化訓練、爬網擷取稅籍登記資料 | 資料收集、資料清理、BI、資料視覺化、授信資料補全 | 5.1 數據準備與模型選擇 | ETL、Data Quality、Missing Value、Data Warehouse、Dashboard |
| ATM 7國語言、智能客服 QR-Code、推播 OTP、FIDO | 多語系、身份驗證、普惠金融、UX、資安 | 3.1 NLP、3.4 多模態、4.3 風險、5.2 部署 | Multilingual NLP、Authentication、FIDO、生物特徵、可近用性 |
| 預計推出 Robo Advisor | 推薦系統、投資適性、模型可解釋性、金融消費者保護 | 機器學習、風險治理、金融 AI 指引 | Suitability、Explainability、Fairness、Model Monitoring |
| AI 應用競賽：程式開發、採購、信用評分、理財、客服、宣導影片 | 生成式 AI、內部創新、POC、AI導入規劃 | 4.1、4.2、4.3 | POC、Prompt Engineering、Cost-Benefit、Change Management |

---

## 2. PDF 三大主軸與土地銀行考試準備方向

附件 PDF 的科目一主要分為三大主軸：

1. **AI 相關技術應用**
   - NLP
   - 電腦視覺
   - 生成式 AI
   - 多模態 AI

2. **AI 導入評估規劃**
   - AI 導入評估
   - AI 導入規劃
   - AI 風險管理

3. **AI 技術應用與系統部署**
   - 數據準備與模型選擇
   - AI 技術系統集成與部署

對土地銀行 AI 人員考試而言，建議這樣解讀：

| PDF章節 | 考試重要度 | 土銀命題化方向 |
|---|---:|---|
| 3.1 NLP | ★★★★★ | 智能客服、金融文件問答、FAQ分類、客服對話摘要、RAG |
| 3.2 電腦視覺 | ★★★★☆ | ATM臉部遮蔽防詐、OCR、文件影像辨識、櫃台/ATM安全 |
| 3.3 生成式 AI | ★★★★★ | 內部知識助理、程式輔助、客服回覆、宣導影片與文案生成 |
| 3.4 多模態 AI | ★★★☆☆ | ATM畫面+語音+文字客服、OCR+文件問答、影像+文字風控 |
| 4.1 AI導入評估 | ★★★★★ | 是否值得導入？ROI、痛點、可行性、資料成熟度 |
| 4.2 AI導入規劃 | ★★★★★ | POC、時程、團隊、資源、專案管理、利害關係人 |
| 4.3 AI風險管理 | ★★★★★ | 金融法遵、個資、偏誤、公平性、可解釋、第三方模型 |
| 5.1 數據準備與模型選擇 | ★★★★★ | 資料清理、特徵工程、分類/回歸/分群、模型評估 |
| 5.2 系統集成與部署 | ★★★★★ | API、資料管線、MLOps、監控、模型漂移、版本控管 |

---

## 3. 專業科目五大考科：讀書架構

你給的土地銀行專業科目包含：

- AI基礎與概念
- 機器學習
- NLP
- 數據分析
- 程式設計（Java 或 Python）

這五科可以整合成一條主線：

```text
業務問題
  ↓
資料取得與清理
  ↓
特徵工程與資料分析
  ↓
模型選擇與訓練
  ↓
AI應用：NLP / CV / GenAI / 多模態
  ↓
系統部署：API / 資料管線 / 監控
  ↓
金融風險治理：個資 / 公平 / 解釋 / 法遵 / 資安
```

### 3.1 AI 基礎與概念

必背重點：

| 概念 | 你要會怎麼解釋 |
|---|---|
| AI | 讓系統模擬人類感知、理解、推論、決策與生成能力 |
| ML | 從資料中學習規律，用於預測、分類、推薦、分群 |
| DL | 使用多層神經網路學習特徵，適合影像、語音、文字等非結構化資料 |
| GenAI | 根據提示或條件生成文字、圖片、語音、程式碼等內容 |
| Multimodal AI | 同時處理文字、影像、語音等多種資料型態 |
| AI Lifecycle | 需求釐清 → 資料 → 模型 → 評估 → 部署 → 監控 → 改善 |

申論答題時，不要只定義名詞，要接到銀行場景：

> 例如智能客服不是單純「聊天機器人」，而是 NLP、知識庫、客服流程、個資控管、人工轉接與持續監控的整合系統。

---

### 3.2 機器學習

#### 3.2.1 任務類型

| 任務 | 常見演算法 | 土銀可能情境 |
|---|---|---|
| 分類 Classification | Logistic Regression、Decision Tree、Random Forest、XGBoost、SVM、BERT Classifier | 詐騙風險分類、客服問題分類、授信風險分類 |
| 回歸 Regression | Linear Regression、Random Forest Regressor、Gradient Boosting | 貸款違約機率、客戶價值、交易金額預測 |
| 分群 Clustering | K-Means、DBSCAN、Hierarchical Clustering | 客戶分群、異常交易群聚 |
| 異常偵測 Anomaly Detection | Isolation Forest、One-Class SVM、Autoencoder | 防詐、洗錢異常行為偵測 |
| 推薦系統 | Collaborative Filtering、Content-Based、Hybrid | Robo Advisor、金融商品推薦 |
| NLP | TF-IDF、BERT、GPT、RAG | 智能客服、文件問答、客服摘要 |
| CV | CNN、YOLO、ViT | ATM臉部遮蔽、防詐、文件影像辨識 |

#### 3.2.2 訓練與評估必背

| 名詞 | 重點 |
|---|---|
| Train / Validation / Test | 避免模型只記住訓練資料 |
| Overfitting | 訓練分數高、測試分數低；可用正則化、交叉驗證、資料增加處理 |
| Confusion Matrix | TP、FP、TN、FN |
| Precision | 預測為正的樣本中，有多少是真的正 |
| Recall | 真正為正的樣本中，有多少被抓出來 |
| F1-score | Precision 與 Recall 的平衡 |
| ROC-AUC | 衡量分類排序能力 |
| Drift | 線上資料分布改變造成模型效果下降 |

銀行防詐題目常考「Precision / Recall 權衡」：

- 若太重視 Recall：能抓更多可疑交易，但可能誤擋正常客戶。
- 若太重視 Precision：誤擋少，但可能漏掉詐騙。
- 銀行應依風險等級設計分層處理，例如低風險提醒、中風險二次驗證、高風險人工覆核。

---

### 3.3 NLP：土地銀行智能客服必考區

#### 3.3.1 NLP / NLU / NLG

| 概念 | 重點 | 銀行應用 |
|---|---|---|
| NLP | 文字/語音的理解、處理、生成總稱 | 智能客服、文件查詢、摘要 |
| NLU | 理解使用者意圖、實體、情緒 | 判斷客戶問「信用卡帳單補寄」或「匯率查詢」 |
| NLG | 生成自然語言回覆 | 自動回覆、報表摘要、客服話術 |

#### 3.3.2 NLP 常見技術演進

| 階段 | 技術 | 優點 | 限制 |
|---|---|---|---|
| 規則式 | Keyword、Rule-based | 可解釋、穩定 | 維護成本高、泛化差 |
| 統計式 | N-gram、HMM、CRF、TF-IDF | 易實作、可用於分類 | 語意理解弱 |
| 深度學習 | RNN、LSTM、GRU | 可處理序列 | 長距離依賴與平行化不足 |
| Transformer | BERT、GPT | 語意理解與生成能力強 | 算力高、風險高 |
| RAG | Retriever + Generator | 可接企業內部知識庫 | 檢索品質與權限控管重要 |
| Agent | 工具使用、規劃、執行 | 可自動處理多步驟任務 | 需要嚴格權限、審計與人工覆核 |

#### 3.3.3 智能客服申論答題架構

遇到「請設計土地銀行智能客服」類題目，可用：

```text
1. 需求：24小時金融諮詢、降低客服負荷、提升一致性
2. 資料：FAQ、產品說明、客服紀錄、法規文件、分行資訊
3. NLP流程：清理 → 去識別化 → 分詞/Embedding → 意圖辨識 → 檢索/生成
4. 架構：前端聊天介面 + NLU + RAG知識庫 + 回覆生成 + 人工轉接
5. 評估：答案正確率、解決率、人工轉接率、客戶滿意度、回覆延遲
6. 風險：個資、錯誤建議、幻覺、資安、越權查詢
7. 控制：權限控管、資料最小化、人工覆核、日誌審計、版本控管
```

---

### 3.4 電腦視覺：ATM AI 臉部辨識防詐

#### 3.4.1 電腦視覺流程

```text
影像取得
  ↓
影像前處理：resize、normalization、noise reduction
  ↓
特徵擷取：CNN / ViT
  ↓
任務模型：分類、偵測、分割、辨識
  ↓
推論結果：是否遮蔽臉部、是否異常
  ↓
業務流程：警示、二次驗證、紀錄、人工處理
```

#### 3.4.2 ATM 防詐可能考點

| 問題 | 答題重點 |
|---|---|
| 為何適合用電腦視覺？ | ATM 本身有影像情境，可即時判斷帽子、口罩、墨鏡等遮蔽 |
| 部署在哪裡？ | 可能採 Edge AI 降低延遲與個資傳輸風險；必要時才回傳事件摘要 |
| 風險是什麼？ | 誤判正常客戶、不同族群/光線偏差、個資保護、模型漂移 |
| 如何降低風險？ | 多場景資料、定期評估、人工申訴、只保留必要事件紀錄、加密與權限控管 |
| 指標怎麼設計？ | 遮蔽偵測準確率、誤警率、漏警率、平均推論延遲、防詐攔阻率 |

---

### 3.5 生成式 AI：會考，但不能只寫「提高效率」

生成式 AI 在銀行不能只追求「會生成」，更要重視：

1. **正確性**
2. **可追溯性**
3. **保密性**
4. **權限控管**
5. **人工覆核**
6. **不可直接做高風險金融決策**

#### 3.5.1 生成式 AI 在土地銀行可用場景

| 場景 | 合理應用 | 高風險點 |
|---|---|---|
| 客服回覆草稿 | 先產生建議回覆，由客服確認 | 幻覺、錯誤金融建議 |
| 內部知識助理 | 查詢作業規範、法遵文件 | 權限、資料外洩 |
| 程式開發輔助 | 產生測試、文件、SQL草稿 | 程式漏洞、授權風險 |
| 宣導影片/文案 | 防詐、金融教育素材 | 不實資訊、著作權 |
| 採購作業 | 摘要文件、比對條款 | 合約風險、責任歸屬 |
| 信用評分輔助 | 生成分析報告草稿 | 不可黑箱決策、需可解釋與人工覆核 |

#### 3.5.2 RAG 標準架構

```text
使用者問題
  ↓
權限檢查
  ↓
Query rewrite / Embedding
  ↓
向量資料庫檢索
  ↓
取回相關文件片段
  ↓
LLM根據文件生成答案
  ↓
引用來源與信心分數
  ↓
敏感內容過濾 / 人工覆核 / 日誌紀錄
```

---

### 3.6 多模態 AI

土地銀行可連到：

- ATM：畫面 + 語音 + QR客服 + 交易流程
- 防詐：影像 + 交易紀錄 + 帳戶風險分數
- 文件處理：掃描文件 + OCR文字 + 內部授信資料
- 智能客服：文字 + 語音 + 截圖 + 客戶操作步驟

申論答題要記得：

> 多模態 AI 的核心不是「很多資料丟進去」，而是「跨模態對齊、融合與判斷」。

---

## 4. AI 導入評估：土地銀行場景答題框架

### 4.1 As-Is / To-Be

| 階段 | 問題 |
|---|---|
| As-Is 現況 | 現在流程耗時、錯誤、重工、風險在哪裡？ |
| Pain Point 痛點 | 是人力不足、資料量大、判斷不一致、即時性不足，還是法遵壓力？ |
| To-Be 目標 | 導入 AI 後希望縮短時間、提升準確率、降低風險、改善服務？ |
| KPI | 如何量化成效？ |
| Risk | 會不會造成個資、偏誤、誤判、資安問題？ |

### 4.2 成本效益分析

AI 導入不只是模型成本，還包含：

- 資料清理成本
- 標註成本
- 模型訓練與算力成本
- 系統整合成本
- 維運與監控成本
- 法遵與資安審查成本
- 員工教育訓練成本
- 錯誤決策的營運與聲譽成本

建議答案寫法：

```text
我會先以 POC 驗證模型可行性與業務價值，不直接全面導入。
若 POC 能在可接受風險下提升關鍵 KPI，例如客服自助解決率、詐騙攔阻率、報表產製時間，才進入 MVP 與正式部署。
```

---

## 5. AI 導入規劃：POC 到正式上線

### 5.1 分階段導入

```text
需求確認
  ↓
資料盤點
  ↓
POC：小範圍驗證可行性
  ↓
MVP：可用版本，接近真實流程
  ↓
Pilot：限定分行、限定客群、限定通路試辦
  ↓
Production：正式上線
  ↓
Monitoring：持續監控、回訓、改善
```

### 5.2 POC 應該回答的問題

1. 資料是否足夠？
2. 資料品質是否可用？
3. 模型是否能達到最低可接受效果？
4. 是否能接進現有系統？
5. 是否符合個資與法遵？
6. 成本是否合理？
7. 業務單位是否願意使用？
8. 失敗時是否能安全停止？

---

## 6. AI 風險管理：金融業必考

### 6.1 風險類型

| 風險 | 說明 | 銀行例子 |
|---|---|---|
| 資料隱私 | 使用個資、交易資料、客服紀錄 | 客服對話輸入外部模型造成外洩 |
| 資料品質 | 錯誤、缺漏、偏差資料 | 授信資料欄位不一致 |
| 模型偏誤 | 不同族群效果不一 | 臉部辨識在不同光線/族群誤判 |
| 可解釋性不足 | 無法說明模型決策 | 信用評分無法向客戶說明 |
| 幻覺 | 生成錯誤資訊 | 客服回答錯誤貸款利率 |
| 模型漂移 | 線上資料變化造成效果下降 | 詐騙手法改變，舊模型失效 |
| 第三方風險 | 外部模型或廠商不可控 | SaaS AI服務資料存放與責任不清 |
| 資安風險 | Prompt injection、資料洩漏 | 使用者誘導客服機器人洩漏內規 |

### 6.2 金融 AI 風險治理答題模板

```text
1. 依風險為基礎分類：低、中、高風險
2. 資料治理：資料最小化、去識別化、權限控管、日誌紀錄
3. 模型治理：版本控管、評估指標、偏誤測試、可解釋性
4. 流程治理：人工覆核、例外處理、申訴機制
5. 供應商治理：契約責任、資料保存、退出機制、第三方稽核
6. 持續監控：模型漂移、效能下降、異常輸出、定期回訓
```

---

## 7. 數據準備與模型選擇

### 7.1 資料來源

| 資料來源 | 例子 |
|---|---|
| 內部結構化資料 | 帳戶資料、交易紀錄、授信資料、客服分類資料 |
| 內部非結構化資料 | 客服對話、申請書、合約、法規文件 |
| 外部資料 | 工商登記、稅籍資料、公開新聞、黑名單/警示帳戶資訊 |
| 即時資料 | ATM操作、網銀登入、FIDO驗證、交易流 |
| 衍生資料 | 風險分數、客戶分群、交易頻率特徵 |

### 7.2 資料清理重點

- 缺失值處理
- 重複資料刪除
- 格式標準化
- 異常值檢查
- 類別不平衡處理
- 個資去識別化
- 標註一致性檢查
- 資料版本控管

### 7.3 模型選擇邏輯

| 問題型態 | 模型方向 |
|---|---|
| 客服問題分類 | BERT / TF-IDF + SVM / LLM + RAG |
| 交易詐騙偵測 | XGBoost / Random Forest / Anomaly Detection |
| ATM臉部遮蔽 | CNN / YOLO / ViT |
| 報表產製 | RPA + BI / 自動化資料管線 |
| 文件問答 | OCR + Embedding + RAG |
| 投資建議 | 推薦系統 + 適合度規則 + 風險控管 |

---

## 8. 系統集成與部署：MLOps / LLMOps

### 8.1 AI 系統不是模型，而是一整條服務鏈

```text
資料來源
  ↓
ETL / ELT
  ↓
特徵工程 / Embedding
  ↓
模型訓練或模型服務
  ↓
API 推論
  ↓
前端或內部系統
  ↓
監控與日誌
  ↓
回饋資料
  ↓
再訓練 / 知識庫更新
```

### 8.2 部署必考關鍵字

| 關鍵字 | 解釋 |
|---|---|
| API | 讓模型服務與前端、ATM、網銀、客服系統串接 |
| Batch Inference | 批次推論，如每日風險分數更新 |
| Real-time Inference | 即時推論，如ATM遮蔽偵測、登入風險判斷 |
| Model Registry | 管理模型版本與上線狀態 |
| Monitoring | 監控準確率、延遲、錯誤率、漂移 |
| Rollback | 模型出問題時快速退回前一版本 |
| A/B Testing | 比較新舊模型效果 |
| Human-in-the-loop | 高風險情境保留人工覆核 |

---

## 9. 程式設計準備方向：Python / Java

### 9.1 Python 常考方向

你至少要會寫：

1. 讀 CSV / JSON
2. 缺失值處理
3. 文字清理
4. Train/Test Split
5. 訓練簡單分類模型
6. 計算 Accuracy、Precision、Recall、F1
7. 呼叫模型 API
8. 寫出簡單 Flask/FastAPI 推論服務概念

Python 範例骨架：

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("customer_service.csv")
df = df.dropna(subset=["question", "label"])

X_train, X_test, y_train, y_test = train_test_split(
    df["question"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

pred = model.predict(X_test_vec)
print(classification_report(y_test, pred))
```

### 9.2 Java 常考方向

若選 Java，重點不是深度學習底層，而是：

- 物件導向設計
- API 串接
- JSON 處理
- 資料驗證
- 例外處理
- 呼叫 AI 模型服務
- 資安與權限控管

Java 答題骨架：

```java
public class FraudCheckService {
    private final AiModelClient aiModelClient;

    public FraudCheckService(AiModelClient aiModelClient) {
        this.aiModelClient = aiModelClient;
    }

    public FraudResult check(Transaction tx) {
        validate(tx);

        FraudScore score = aiModelClient.predict(tx);

        if (score.getValue() >= 0.9) {
            return FraudResult.highRisk("Require manual review");
        } else if (score.getValue() >= 0.6) {
            return FraudResult.mediumRisk("Require OTP verification");
        }
        return FraudResult.lowRisk("Pass");
    }

    private void validate(Transaction tx) {
        if (tx == null || tx.getAccountId() == null) {
            throw new IllegalArgumentException("Invalid transaction data");
        }
    }
}
```

---

## 10. 考前 45 天，一天 1 小時讀書配置

> 因為專業科目權重 80%，且你設定 90% 準備專業科目，所以要把共同科目壓到最後一週。重點是：不要平均讀，要集中打高分區。

### 第 1 階段：7/8～7/14，建立總架構

每天 1 小時：

- 20 分鐘：AI 基礎與機器學習名詞
- 20 分鐘：NLP / GenAI / RAG
- 20 分鐘：申論題模板練習

目標：會用「場景 → 資料 → 模型 → 部署 → 風險」回答。

### 第 2 階段：7/15～7/24，主攻土地銀行場景

每天 1 小時：

- 智能客服
- ATM AI 臉部辨識防詐
- RPA / 大數據分析
- Robo Advisor
- 金融 AI 治理

目標：每個場景都能寫 600～900 字申論。

### 第 3 階段：7/25～8/3，機器學習與數據分析

每天 1 小時：

- 分類、回歸、分群、異常偵測
- Precision / Recall / F1 / AUC
- 資料清理、特徵工程
- Python / Java 程式題骨架

### 第 4 階段：8/4～8/11，AI 導入與系統部署

每天 1 小時：

- AI 導入評估
- POC / MVP / Pilot
- MLOps / API / 監控 / 漂移
- 第三方風險與資安

### 第 5 階段：8/12～8/15，申論題衝刺

每天 1 小時：

- 每天寫 2 題申論
- 每題限時 20～25 分鐘
- 寫完後用模板檢查是否有：場景、資料、模型、部署、風險、治理

### 第 6 階段：8/16～8/21，共同科目 + 專業科目總複習

- 30 分鐘：共同科目
- 30 分鐘：專業科目申論模板與程式骨架

---

## 11. 申論萬用架構

遇到任何 AI 應用題，直接套：

```text
一、業務問題與目標
二、資料來源與資料治理
三、AI技術與模型選擇
四、系統架構與導入流程
五、評估指標與效益
六、金融業風險與治理
七、結論：以POC逐步導入，並持續監控改善
```

範例結尾：

> 綜合而言，銀行導入 AI 不應以「技術先行」為目的，而應以業務痛點、風險可控與客戶權益保護為核心。建議先以 POC 驗證資料品質、模型效果與營運可行性，再逐步進入試辦與正式部署，並透過監控、回訓、人工覆核與治理制度確保長期穩定。

## 參考來源與使用範圍

> 本檔案以使用者提供之《AI應用規劃師（中級）學習指引：科目1 人工智慧技術應用與規劃》為核心，並結合土地銀行公開揭露之數位金融、AI與防詐應用案例整理。  
> 注意：附件 PDF 是 iPAS 學習指引，不等於土地銀行正式命題大綱；本整理是「考試準備導向」的重點改寫。

### 土地銀行與主管機關公開資料

1. 土地銀行「永續發展－客戶權益－數位金融」：智能客服、RPA、大數據分析、FIDO、Robo Advisor 等數位金融方向  
   https://www.landbank.com.tw/Category/Items/%E6%95%B8%E4%BD%8D%E9%87%91%E8%9E%8D-1

2. 土地銀行「ATM導入 AI臉部辨識防詐」：ATM AI臉部辨識、遮蔽臉部警示、防詐與異常帳戶風險交換  
   https://www.landbank.com.tw/Bulletin/Detail/0d614749-ec6f-42c3-bd36-b3d8003dde44

3. 土地銀行 ESG 新聞集錦：ATM 7國語言、智能客服 QR-Code、推播 OTP、AI應用競賽  
   https://www.landbank.com.tw/Category/Items/%E6%96%B0%E8%81%9E%E9%9B%86%E9%8C%A6

4. 土地銀行 2025 校園金融創意挑戰賽：金融防詐、永續金融、智能理財、數位金融  
   https://www.landbank.com.tw/Bulletin/Detail/5e8b2a07-7b6b-469d-9638-b375003b3044

5. 金管會「金融業運用人工智慧(AI)指引」新聞稿：風險基礎、AI生命週期、第三方管理、資料最小化、可解釋性、透明性  
   https://www.fsc.gov.tw/ch/home.jsp?dataserno=202406200001&dtable=News&id=96&mcustomize=news_view.jsp&parentpath=0%2C2