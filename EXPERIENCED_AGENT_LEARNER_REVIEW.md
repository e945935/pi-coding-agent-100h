# 有其他 Agent 經驗學習者角度試讀與實作回饋

## 角色假設

本次以「已用過其他 coding agent」的學習者角度檢視教材，例如曾使用：

- Claude Code
- OpenAI Codex CLI / ChatGPT coding workflow
- GitHub Copilot Coding Agent
- Cursor / Windsurf
- Aider
- Continue / Cline 類工具

這類學習者通常已懂：

- AI 可讀寫檔案與執行 shell
- repo 摘要、修 bug、補測試、code review
- 使用 `AGENTS.md` / rules / memories / prompts 管理 agent 行為
- 需要 Git 與安全邊界

因此他們真正需要的是：

1. Pi 跟其他 agent 的差異
2. Pi 的專屬心智模型
3. 對應既有經驗的遷移路徑
4. 哪些功能是 Pi 特別強或特別不同
5. 實作時的最短路徑與坑點

---

## 實作檢查結果

### sample project

已執行：

```bash
cd sample-project
npm test
npm run lint
npm run build
```

結果：全部通過。

### SDK example

已執行：

```bash
cd examples/sdk
npm install --package-lock-only
```

結果：相依套件解析成功，沒有 vulnerability。

### 尚未完整互動驗證

以下項目需要真實登入 provider 並進入 Pi TUI 後驗證：

- `/login`
- `/model`
- `/fork`
- `/tree`
- `/review`
- `/skill:test-writer`
- `/hello`
- extension confirm UI
- SDK 真正送 prompt 給模型
- RPC 實際 stdin/stdout 流程

---

# 總體觀察

目前教材對「完全新手」友善，但對「已有其他 agent 經驗的人」來說，會覺得前面 40 小時有點慢，而且沒有直接回答：

> 我已經會 Claude Code / Codex / Cursor，為什麼還要學 Pi？Pi 的操作模型差在哪？

建議新增一條「有經驗者快速路線」與一章「從其他 Agent 遷移到 Pi」。

---

# 逐章卡關點與建議

## 00 全書入口

### 可能卡關

1. 學習路線有使用者、客製化、系統整合，但沒有「已有 agent 經驗者路線」。
2. 沒有一頁快速對照 Pi 和其他 agent 的差異。
3. 沒有說明 Pi 的核心設計哲學：minimal harness、可擴充、非大而全。

### 建議

新增：

```text
docs/AGENT_MIGRATION_GUIDE.md
```

內容包含：

- Claude Code / Codex / Cursor / Aider 使用者如何對應到 Pi
- 常用功能對照
- 30 分鐘快速上手路線
- 3 小時進階遷移路線

---

## 01 基礎入門

### 可能卡關

1. 有經驗者會覺得安裝、登入、repo 摘要太基本。
2. 沒有明確說 `AGENTS.md` 載入優先順序與 `AGENTS.override.md`。
3. 沒有比較 `AGENTS.md` 與其他工具 rules 的差異，例如 Claude Code 的 instructions、Cursor rules。
4. 沒有說明 Pi 預設工具集是刻意保持小核心，不是功能不足。

### 建議

- 新增「有經驗者快速完成」區塊：

```markdown
如果你已用過其他 coding agent，本章只需確認：
1. pi --version
2. /login
3. /model
4. 建立 AGENTS.md
5. pi -p "Summarize this repo"
```

- 補 `AGENTS.md` / `CLAUDE.md` / `AGENTS.override.md` 載入規則。
- 加一張「Pi context files vs 其他 agent rules」對照表。

---

## 02 互動模式與 Session 工作流

### 可能卡關

1. 對有經驗者來說，`/fork`、`/tree` 是 Pi 很有價值的功能，但目前教材沒有強調它和一般 chat history 的差異。
2. 沒有說明 session 檔案實際存在哪、如何備份、是否可分享。
3. 沒有說明 compaction 和其他 agent 的 compact / summarize context 差異。
4. `方案 A -> /fork -> 方案 B` 的劇本可用，但學員可能不確定 fork 是從哪個節點開始。

### 建議

- 補「Pi session tree 心智模型」。
- 加入簡圖：

```text
root
 ├─ 方案 A
 └─ 方案 B
```

- 補 session 管理對照：

| 需求 | 其他 agent 常見做法 | Pi 做法 |
|---|---|---|
| 回到舊任務 | chat history | `pi -r` / `/resume` |
| 嘗試分支解法 | 複製對話 | `/fork` / `/tree` |
| 壓縮上下文 | compact | compaction |

---

## 03 設定、安全與平台環境

### 可能卡關

1. 有經驗者會想知道 Pi 的 permission model，但本章仍偏概念。
2. 沒有明確列出「Pi 預設會不會每次問權限」。
3. 沒有和 Claude Code / Codex 的 approvals、sandbox、trust model 對照。
4. settings 缺實際範例，進階使用者會想直接改設定檔。

### 建議

- 新增「Pi 安全模型速讀」。
- 補 settings 範例。
- 補：project-local extensions 必須 trust project 後才載入。
- 加入「不同 agent 安全模型比較表」。

---

## 04 Provider、模型與本地模型

### 可能卡關

1. 有經驗者會想知道模型設定檔在哪裡、catalog 如何更新、如何 pin model。
2. 沒有說明 `pi update --models`。
3. 沒有比較 subscription login 與 API key 在限制、費用、模型可用性上的差異。
4. llama.cpp 只提概念，對想跑 local-first 工作流的人資訊不足。

### 建議

- 補「模型管理 quick reference」。
- 補 `pi update --models`。
- 補 model picker 中 Ctrl+S 儲存預設模型的說明。
- llama.cpp 可獨立成 advanced lab。

---

## 05 Prompt Templates、Skills、Themes

### 可能卡關

1. 有經驗者會問：Prompt template、Skill、Extension 的邊界到底在哪？
2. 對 Claude Code 或 Codex 使用者來說，Skill 可能類似「可載入的專業操作手冊」，但教材沒有對照。
3. Prompt template 有路徑，但沒有說 non-recursive discovery。
4. 沒有示範 template 是否支援參數、變數或 input expansion。
5. Theme 對有經驗者不是主線，放在同章可能分散焦點。

### 建議

- 加一張決策表：

| 需求 | 用 Prompt | 用 Skill | 用 Extension |
|---|---|---|---|
| 固定提示詞 | ✅ |  |  |
| 多步驟工作手冊 |  | ✅ |  |
| 新增工具或攔截行為 |  |  | ✅ |

- 補 prompt templates discovery 是 non-recursive。
- 補 `/skill:name` 強制載入 skill 的意義。
- Theme 移到附錄或延伸挑戰。

---

## 06 Extensions 開發

### 可能卡關

1. 對有經驗者來說，Extension 是 Pi 最值得學的部分，但目前還缺「完整開發環境」。
2. 沒有 `tsconfig.json`、typecheck script、測試方式。
3. `greet-tool.ts` 使用 `typebox`，但沒有說這個 import 來源與相依管理。
4. 沒有事件清單摘要，學員需要一直回官方 docs 查。
5. 沒有說明 extension 在 print/json/rpc/tui mode 下行為是否不同。
6. 對做過 MCP / tool server 的人，會想知道 Pi extension 與 MCP 的差異。

### 建議

- 新增：

```text
examples/extensions-dev-project/
```

包含：

```text
package.json
tsconfig.json
src/hello.ts
src/safety-guard.ts
README.md
```

- 加入 Extension vs MCP 對照：

| 項目 | Pi Extension | MCP Server |
|---|---|---|
| 執行位置 | Pi process 內 | 外部 server |
| 權限 | 本機完整權限 | 視 server 而定 |
| 可攔截 Pi 事件 | ✅ | 通常否 |
| 可跨工具共用 | 較低 | 較高 |

- 補事件速查表：`session_start`、`tool_call`、model/tool lifecycle。

---

## 07 SDK、RPC 與 JSON 整合

### 可能卡關

1. 有經驗者會把這章拿來做真正整合，但目前 RPC 仍是「示意」，不是完整可執行範例。
2. SDK 範例沒有處理使用者中斷、錯誤、timeout。
3. 沒有說明何時該用 SDK，何時該做 extension。
4. 沒有說明 SDK 會載入哪些 resource：extensions、skills、prompt templates、context files。
5. 沒有說明 sessionManager in-memory 與持久化 session 的差異。

### 建議

- 新增「SDK vs Extension vs RPC」決策表。
- 新增完整 RPC client 範例，至少做到：
  - spawn `pi --mode rpc`
  - 發送 prompt
  - 讀 response
  - 等 agent_end 後結束 process
- SDK 範例補 try/catch、abort、timeout。
- 補 `SessionManager.inMemory()` 適合 demo，不適合需要保存歷史的應用。

---

## 08 總整專題

### 可能卡關

1. 有經驗者可能想直接做 extension / SDK 專案，但沒有提供技術選型引導。
2. S/M/L 規模有了，但缺「估時與交付物差異」。
3. 沒有提供範例題目與完成標準。

### 建議

新增專題選型表：

| 專題 | 建議規模 | 技術 | 預估時數 |
|---|---|---|---:|
| Team workflow pack | S | AGENTS.md + prompts | 3～5 |
| Safety guard | M | Extension | 5～8 |
| Repo analyzer CLI | L | SDK / JSON | 8～12 |

---

# 有經驗學習者最容易卡住的共通點

## 1. 缺少「功能對照」

他們會自然問：

- Claude Code 的 slash commands 對應 Pi 的什麼？
- Cursor rules 對應 Pi 的什麼？
- MCP server 對應 Pi extension 嗎？
- Aider 的 repo map 在 Pi 裡有類似概念嗎？
- Codex approval mode 和 Pi trust model 差在哪？

建議新增專章或附錄處理。

## 2. 缺少「最快上手路線」

已有經驗者不需要 10 小時才完成 repo 摘要。建議給：

```markdown
# 90 分鐘 Pi 快速遷移 Lab

1. 安裝與登入，10 分鐘
2. AGENTS.md，10 分鐘
3. repo summary，10 分鐘
4. session fork，20 分鐘
5. prompt template，15 分鐘
6. hello extension，15 分鐘
7. JSON mode，10 分鐘
```

## 3. 缺少「Pi 的獨特賣點」

教材應明確強調：

- 核心工具少而清楚
- TypeScript extensions 可直接改 agent 行為
- session tree / fork 適合探索不同解法
- SDK / RPC / JSON mode 讓它可被嵌入
- skills / prompt templates / packages 可組合分享

## 4. 缺少「可比較的實驗」

有經驗者喜歡比較工具。建議加入實驗：

```text
同一個 sample-project 任務，分別用：
1. 一般 prompt
2. AGENTS.md
3. prompt template
4. skill
5. extension 防護
比較結果。
```

---

# 優先修改建議

## P0

1. 新增 `docs/AGENT_MIGRATION_GUIDE.md`。
2. 在 `BOOK.md` 補「有其他 agent 經驗者路線」。
3. 補 Prompt / Skill / Extension / SDK / RPC 決策表。
4. 補 Extension vs MCP 對照。
5. 補完整 RPC client 範例。

## P1

1. 補 session tree 心智模型圖。
2. 補 settings 範例。
3. 補 model management quick reference。
4. 補 extension 開發專案骨架。
5. 補有經驗者 90 分鐘快速 Lab。

## P2

1. 補 Claude Code / Codex / Cursor / Aider 個別遷移案例。
2. 補企業導入時的工具比較說明。
3. 補 benchmarking 任務與記錄表。

---

# 總結

從有其他 agent 經驗的學習者角度，這本教材已經能帶人理解 Pi，但還沒有充分利用這類學員的既有知識。

最重要的補強方向是：

- 不要只教「怎麼用 Pi」
- 要教「你熟悉的 agent 概念在 Pi 裡叫什麼」
- 要教「Pi 哪些地方不一樣」
- 要提供「快速遷移路線」

如果補上遷移指南與決策表，這本教材會更適合進階學員與企業導入。