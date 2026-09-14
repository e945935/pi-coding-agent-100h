# 資深編輯逐章審閱意見

## 編輯定位

本書目前是一份結構完整的「實作型課程教材」，不是單純的官方文件翻譯。整體方向正確，但若要成為可長期維護、可自學、可出版的讀者服務書籍，仍需要加強：

- 讀者分流
- 術語一致性
- 每章的學習閉環
- 指令與版本可重現性
- 章節之間的銜接
- 技術範例的完整驗證

## 總體評價

### 優點

1. 從使用、客製化到整合，學習路徑合理。
2. 有 sample project、作業、評量與專題，不只是概念介紹。
3. 已考慮 Windows、PowerShell、Git Bash 與安全問題。
4. 有針對其他 coding agent 使用者的遷移指南，定位比一般入門教材更完整。
5. 讀者服務資源齊全：檢查表、問題排除、作業範本與範例程式。

### 目前最重要的編輯問題

1. 章節名稱有時稱「模組」、有時稱「章」，應統一。
2. 中英文術語尚未完全一致，例如 provider、model、session、prompt template、skill、extension。
3. 「100 小時」與實際文字量、練習量還沒有完全對齊，部分章節更像 2～4 小時講義。
4. 各章的格式不一致：有些有本章情境、常見問題、小測驗，有些沒有。
5. 多個指令仍使用固定路徑 `C:/Users/user/...`，不適合公開讀者直接複製。
6. README 說明與真正的閱讀入口、進階路線、讀者服務入口可以再整合。

---

# 逐章建議

## 第 1 章：基礎入門

### 編輯評價：最完整，可作為全書樣板

這一章已具備情境、目標、操作步驟、預期輸出、驗收標準、常見問題與小測驗，應作為其他章節的格式標準。

### 建議修改

1. 將固定路徑改成變數或相對路徑。

目前：

```bash
cd C:/Users/user/pi-coding-agent-100h/sample-project
```

建議：

```bash
cd path/to/pi-coding-agent-100h/sample-project
```

並在 Windows、PowerShell、Git Bash 對照表中提供實際寫法。

2. 補一個「開始前檢查」：

```text
node --version
npm --version
git --version
pi --version
```

3. `AGENTS.md` 範例應明確說明這是學習範例，不是安全保證。
4. 補「不要讓 Pi 讀取 secrets」的具體案例。
5. 小測驗增加參考答案連結。
6. 「預設提供四個工具」的敘述應註明以目前版本文件為準，避免版本更新造成誤導。

### 優先級：P0

這一章是全書入口，必須確保所有複製貼上的步驟都能在公開 repo 使用。

---

## 第 2 章：互動模式與 Session 工作流

### 編輯評價：概念重要，但需要更強的敘事與操作銜接

這是 Pi 與其他 coding agent 很有差異、也很有價值的一章。session tree、fork、clone 不應只列為指令，而應建立清楚的心智模型。

### 建議修改

1. 在操作劇本之前先放 session tree 圖：

```text
原始任務
├─ 方案 A：小幅修改
└─ 方案 B：嚴格驗證
```

2. 明確說明 `/fork` 是「從目前節點分支」，不是複製 Git branch。
3. 明確說明 Pi session 分支和 Git branch 是兩套不同機制。
4. 補 `git status` 與 session 操作的搭配流程。
5. `/clone` 與 `/fork` 的差異需要各給一個使用情境。
6. compaction 目前只在學習目標出現，建議加入實際觸發情境。
7. `pi -p`、`--mode json` 建議加入「何時不要用」的說明。

### 建議新增小節

```markdown
## Session 與 Git 的關係

Session 管理對話脈絡；Git 管理檔案變更。兩者不能互相取代。
```

### 優先級：P0

---

## 第 3 章：設定、安全與平台環境

### 編輯評價：主題重要，但章節現在像清單，缺少決策情境

安全章節不應只說「要小心」，應讓讀者能依情境做決策。

### 建議修改

1. 增加「風險情境表」：

| 情境 | 風險 | 建議 |
|---|---|---|
| 公開開源 repo | 不可信設定或 extension | 先檢查再 trust |
| 含 `.env` 的 repo | secrets 外洩 | 加入 ignore、限制讀取 |
| production workspace | 誤刪或誤部署 | 不直接使用 agent 操作 |
| 未提交變更 | 無法回復 | 先 commit 或建立 checkpoint |

2. 具體區分：
   - project trust
   - extension trust
   - shell command risk
   - API key protection
   - container / sandbox
3. 補 `.pi/settings.json` 的最小實作範例，並連到 `docs/SETTINGS_EXAMPLES.md`。
4. shell alias 不應放在主線太早，建議改成附錄或短節。
5. tmux 與 containerization 可能對初學者太重，標示為「進階選讀」。

### 優先級：P1

---

## 第 4 章：Provider、模型與本地模型

### 編輯評價：內容方向對，但讀者的成本與環境差異處理不足

這一章最容易因 provider、帳號、地區與模型清單變動而過期，因此編輯上要把「固定知識」和「會變動的資訊」分開。

### 建議修改

1. 將「三個模型比較」改成「至少兩個模型；若環境允許再比較三個」。
2. 增加無法使用多模型時的替代作業：
   - 比較不同 thinking level
   - 比較不同 prompt
   - 比較同模型的 interactive / print mode
3. 明確區分：
   - subscription provider
   - API-key provider
   - custom model
   - custom provider
   - local model
4. `pi update --models` 應放進主要操作步驟，而不只在附錄。
5. 增加模型比較紀錄表，欄位至少包含：品質、速度、成本、工具呼叫、錯誤率。
6. llama.cpp 建議標示「進階實驗」，不要讓它成為入門者的必要依賴。
7. 所有模型名稱、價格、支援清單都應避免寫死，改連官方文件。

### 優先級：P0

---

## 第 5 章：Prompt Templates、Skills、Themes

### 編輯評價：本章是工作流價值的核心，定位可再收斂

Prompt template 與 Skill 的比較已經有雛形，但 theme 在本章比例偏低，容易讓讀者以為三者同等重要。

### 建議修改

1. 章名改成：

```text
Prompt Templates 與 Skills：建立可重複工作流
```

Theme 移到附錄或延伸閱讀。

2. 先放決策表，再進入實作。
3. 明確說明 prompt template 的 discovery 是 non-recursive，避免讀者把檔案放在任意子資料夾後找不到。
4. 補 template 參數或輸入展開的限制與範例，若目前版本不支援則明確說明。
5. Skill 範例的 frontmatter 必須說明 `name` 與 `description` 是必要欄位。
6. 建議提供「錯誤的 skill 範例」與修正前後比較。
7. Pi package 應以「分享與版本管理」為主，不要只停留在定義。

### 優先級：P1

---

## 第 6 章：Extensions 開發

### 編輯評價：技術含量最高，應成為全書最嚴謹的一章

目前有 hello command、安全攔截與開發骨架，方向很好；但 extension 涉及 API、型別、權限與模式差異，需要更像真正的開發文件。

### 建議修改

1. 先明確區分三個層次：
   - `registerCommand`
   - `registerTool`
   - event interception
2. 加入 Extension vs MCP 對照，並將其放在本章，不只放遷移指南。
3. 增加事件速查表：
   - session lifecycle
   - agent lifecycle
   - model lifecycle
   - tool lifecycle
4. `greet-tool.ts` 需要說明 `typebox` 的相依來源與安裝方法。
5. 開發骨架加入：
   - `npm install`
   - `npm run typecheck`
   - 如何複製到 `.pi/extensions`
   - 如何用 `/reload` 驗證
6. 安全範例要加醒目警告：字串比對不是完整安全策略，不能取代 sandbox 或人工確認。
7. 增加非互動模式注意事項：TUI UI、RPC UI、print mode 的行為可能不同。
8. 加入最小單元測試或至少「手動測試案例表」。

### 優先級：P0

---

## 第 7 章：SDK、RPC 與 JSON 整合

### 編輯評價：讀者價值高，但目前 SDK 與 RPC 的完成度不一致

SDK 已有 minimal example；RPC client 目前雖然可作為入門範例，但仍需標示其限制，避免讀者當成 production-ready code。

### 建議修改

1. 先提供決策流程：

```text
只要一次性結構化輸出？JSON mode
要從其他程式控制 Pi？RPC
要在 Node.js 內嵌 agent？SDK
要改 Pi 本身行為？Extension
```

2. 明確說明 SDK `SessionManager.inMemory()` 的限制。
3. SDK 範例加入：
   - timeout
   - abort
   - error handling
   - provider 不可用時的訊息
4. RPC 範例加入：
   - 等待 `agent_end`
   - process exit
   - timeout
   - JSON parse error
   - stdin 每筆資料必須以 LF 結尾
5. 說明 stdout 必須維持 JSONL 純輸出，診斷訊息應走 stderr。
6. `npm install` 應使用 lockfile，並標示測試過的 Pi / Node.js 版本。
7. 增加 SDK / RPC / Extension 的選擇案例。

### 優先級：P0

---

## 第 8 章：總整專題

### 編輯評價：有基本框架，但 5 小時與專題期待不完全相稱

S/M/L 規模是很好的修正，但專題應該更像產品交付，而不只是最後一份作業。

### 建議修改

1. 加入專題時程：

| 階段 | 產出 | 建議時間 |
|---|---|---:|
| 題目與範圍 | Proposal | 30 分 |
| 設計 | 流程圖與驗收標準 | 45 分 |
| 實作 | 可展示 MVP | 2～6 小時 |
| 驗證 | 測試與安全檢查 | 1 小時 |
| Demo | 展示與回顧 | 30 分 |

2. 明確說明 5 小時只適合 S / 小型 M 專題。
3. 增加「不做什麼」的 scope control 欄位。
4. Proposal 增加：利害關係人、成功指標、風險、後續維護人員。
5. Demo 評分加入可重現性與失敗情境處理。
6. 建議每個專題至少提交一段錄製或逐步 demo 紀錄。

### 優先級：P1

---

# 全書編輯規範建議

## 1. 統一章節模板

每章固定使用：

1. 本章情境
2. 學習目標
3. 先備知識
4. 官方文件對應
5. 課程安排
6. 核心觀念
7. 詳細操作步驟
8. 預期輸出
9. 實作任務
10. 驗收標準
11. 常見錯誤與排除
12. 小測驗
13. 我學會了嗎？
14. 延伸閱讀

## 2. 統一術語

建議首次出現時使用：

- 提示詞模板（prompt template）
- 技能（skill）
- 擴充功能（extension）
- 供應商（provider）
- 模型（model）
- 工作階段（session）
- 工具呼叫（tool call）

後續可使用英文簡稱，但不要同一段落混用「工作流 / workflow」、「技能 / skills」而不說明。

## 3. 統一台灣用語

建議全書固定使用：

| 避免 | 建議 |
|---|---|
| 文件夾 | 資料夾 |
| 軟件 | 軟體 |
| 程序 | 程式 |
| 配置 | 設定 |
| 鏈接 | 連結 |
| 調用 | 叫用 |
| 交互 | 互動 |
| 運行 | 執行 |
| 輸出結果 | 輸出 |
| 優化 | 最佳化 |

## 4. 指令可重現性

所有會改檔案或呼叫模型的章節，建議標示：

```text
測試環境：Windows / PowerShell
Node.js：22.x
Pi：0.x.x
Provider：任一可用 provider
```

所有固定路徑改用：

- repo 相對路徑
- `$env:PI_COURSE_ROOT`
- `<教材根目錄>` 佔位符

## 5. 每章加入學習閉環

每章至少要讓讀者留下三項成果：

1. 一個可執行結果
2. 一份紀錄或設定檔
3. 一個可驗收的作業

## 6. 連結與維護

- 每章官方文件連結應使用相對連結或固定版本連結。
- 需要隨版本變動的資訊集中放在版本備註，不要散落各章。
- GitHub repo 首頁應優先引導讀者到 `SUMMARY.md`、快速開始、問題排除與 issue 回報方式。
- 建議加入 GitHub Issue template，讓讀者依環境、指令、錯誤訊息格式回報問題。

---

# 建議修訂順序

## 第一輪：可讀與可執行，P0

1. 統一所有公開指令的路徑寫法。
2. 補第 2、4、6、7 章的關鍵操作與限制。
3. 每章補上預期輸出、常見錯誤、小測驗與答案連結。
4. 統一章節模板與術語。
5. 加入版本與測試環境標示。

## 第二輪：教學品質，P1

1. 補講師版教案。
2. 補每章學習成果紀錄。
3. 補專題時程與 scope control。
4. 補圖表、session tree 與選擇流程。

## 第三輪：出版品質，P2

1. 全書校稿與台灣用語檢查。
2. 加入目錄、索引與交叉引用。
3. 加入截圖與影片補充資料。
4. 建立版本化發布流程。

## 最終編輯結論

本書已經具備很好的教材骨架與讀者服務意識。下一階段不建議再大量增加主題，而應優先讓現有內容：

- 更一致
- 更容易複製
- 更容易驗證
- 更不受版本變動影響
- 更清楚呈現 Pi 與其他 agent 的差異

完成上述 P0 修訂後，教材即可進入正式試讀與小規模授課階段。
