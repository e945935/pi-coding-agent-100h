# 學習者角度試讀與實作回饋

## 試讀方式

本次以第一次接觸教材的學習者角度，依序閱讀：

- `SUMMARY.md`
- `BOOK.md`
- `course/01-basic` ～ `course/08-final-project`
- `assignments/ASSIGNMENTS.md`
- `examples/`

並實際執行 sample project 的測試、lint、build。

## 實作確認

在 `sample-project/` 中已確認：

```bash
npm test
npm run lint
npm run build
```

結果：全部通過。

環境：

```text
Node.js v22.23.2
npm 10.9.8
Pi 0.85.1
```

> 注意：互動式指令如 `/login`、`/model`、`/fork`、`/tree`、extension 載入與 SDK 實際呼叫模型，需在真實 Pi 互動環境與已登入 provider 的狀態下驗證。

---

# 逐章卡關點與建議

## 01 基礎入門

### 可能卡關

1. `cd C:/Users/user/pi-coding-agent-100h/sample-project` 對不同 shell 不一定都適用。
2. 教材有 API key 範例 `sk-ant-...`，初學者可能誤以為要貼進檔案。
3. `pi --version` 可執行，但如果使用者沒有 provider，下一步 `/login` 仍會卡住。
4. `AGENTS.md` 建立後，學員可能不知道要放在哪個目錄。
5. `git checkout -- <file>` 對初學者來說有風險，且 Git 新版更建議知道 `git restore`。

### 建議

- 增加「依作業系統切換資料夾」表格。
- 明確提醒：API key 範例不可寫入 repo、不可提交 Git。
- 在本章前面加入「登入前檢查表」。
- 補一句：`AGENTS.md` 請放在專案根目錄。
- Git 回復指令補 `git restore <file>`。

---

## 02 互動模式與 Session 工作流

### 可能卡關

1. `/fork`、`/clone`、`/tree` 的差異不明顯。
2. 沒有完整操作劇本，學員不知道何時該 fork。
3. `!npm test` 和 `!!npm install` 的差異有說，但缺少情境。
4. print mode 範例太少，缺少預期輸出。

### 建議

- 補一個完整案例：「同一個 bug 用兩種解法處理」。
- 加入比較表：`/resume`、`/fork`、`/clone`、`/tree`。
- 為 `!` 與 `!!` 補實際使用情境。
- 補 print mode 練習：產生 repo 摘要、產生 changelog。

---

## 03 設定、安全與平台環境

### 可能卡關

1. 提到 settings，但沒有示範設定檔位置與範例。
2. 提到 project trust，但沒有畫出風險流程。
3. shell alias 範例只適合 bash/zsh，不適合 PowerShell。
4. containerization 對初學者太抽象。

### 建議

- 補 `settings` 範例檔與常用設定說明。
- 補 PowerShell alias：`Set-Alias` 或 function 寫法。
- 補「哪些狀況不要 trust project」清單。
- containerization 放成進階閱讀，不要放在主線第一輪實作。

---

## 04 Provider、模型與本地模型

### 可能卡關

1. 要求用三個模型比較，但學員可能只有一個 provider。
2. custom model 與 custom provider 的界線不清楚。
3. llama.cpp 本地模型需要額外環境，對初學者門檻高。
4. 沒有提供模型比較記錄表。

### 建議

- 把「三個模型」改為「至少兩個，若環境允許可三個」。
- 補模型比較表範本。
- 先教 `/model` 與預設模型，再把 llama.cpp 放進延伸挑戰。
- 補：沒有多模型時如何完成作業。

---

## 05 Prompt Templates、Skills、Themes

### 可能卡關

1. 教材說明概念，但沒有明確說檔案要放哪裡。
2. 範例是普通 markdown，學員不確定如何變成 Pi 可用的 prompt template。
3. skill 的實際檔案結構沒有範例。
4. theme 的操作步驟不足。

### 建議

- 補 prompt templates 的實際放置路徑與命名範例。
- 建立 `examples/skills/` 範例。
- 建立 `examples/themes/` 範例。
- 本章新增一個從零建立 `/review` prompt template 的完整流程。

---

## 06 Extensions 開發

### 可能卡關

1. TypeScript extension 範例有程式碼，但沒有安裝依賴與測試方式。
2. `greet-tool.ts` 使用 `typebox`，學員可能不知道是否要安裝。
3. extension 要放到 `~/.pi/agent/extensions/` 或 `.pi/extensions/`，但沒有實際複製指令。
4. `event.input.command` 型別可能讓 TypeScript 嚴格模式報錯。
5. 安全防護 extension 要互動確認，非互動測試不容易驗證。

### 建議

- 補「如何安裝 extension 範例」步驟。
- 補 `package.json` 或說明 Pi extension 可用的 import。
- 補 Windows / macOS / Linux 複製 extension 的指令。
- 補「測試 extension 是否載入」的方法，例如 `/hello`。
- 安全範例補測試劇本：輸入要求 Pi 執行 `rm -rf test-folder`，預期跳確認。

---

## 07 SDK、RPC 與 JSON 整合

### 可能卡關

1. SDK 範例需要 provider 與模型可用，否則程式會卡在模型初始化或 prompt。
2. `npm install` 會安裝 latest，未來可能跟教材版本不一致。
3. 沒有 `.gitignore`，學員執行後可能產生 `node_modules`。
4. RPC mode 只有概念，沒有可執行的 request/response 範例。
5. JSON mode 沒有說明輸出事件長什麼樣子。

### 建議

- SDK 範例固定版本，或註明 tested with Pi 版本。
- 補 `.gitignore`。
- 補「沒有登入 provider 時的錯誤排除」。
- 補 JSON mode 預期輸出片段。
- 補 RPC 最小 JSONL 操作範例。

---

## 08 總整專題

### 可能卡關

1. 5 小時對完整專題偏短。
2. 沒有提供專題 proposal 範本。
3. 沒有提供 demo 評分檢查表。
4. 不同專題難度差很多，評分可能不一致。

### 建議

- 新增 `final-project/PROJECT_PROPOSAL_TEMPLATE.md`。
- 新增 `final-project/DEMO_CHECKLIST.md`。
- 將專題分成 S / M / L 三種規模。
- 若是 100 小時課，建議總整專題可增加到 8～10 小時。

---

# 全書共通卡關點

## 1. 缺少「我現在該做什麼」的學員導引

目前教材章節清楚，但每章還需要更明確的步驟，例如：

```text
請照做：
1. 開啟終端機
2. 切到 sample-project
3. 執行 pi
4. 輸入以下提示詞
5. 將結果貼到 notes/ch01-result.md
```

## 2. 範例尚未全部可執行驗證

sample project 可執行，但 prompt、extension、SDK 範例還需要更完整安裝與驗證方式。

## 3. Windows / PowerShell / Git Bash 差異需要統一處理

本教材使用者看起來是在 Windows 環境，建議全書指令都加上環境標籤。

## 4. 作業需要繳交範本

建議建立：

```text
submissions/
├─ assignment-01-template.md
├─ assignment-02-template.md
└─ final-project-template.md
```

## 5. 需要學習檢查表

建議每章最後加入：

```markdown
## 我學會了嗎？

- [ ] 我能自己操作 ...
- [ ] 我能解釋 ...
- [ ] 我能排除 ...
```

---

# 優先修改建議

## P0：最急

1. 補第 02 章完整 session 實作劇本。
2. 補第 05 章 prompt template / skill 實際放置位置。
3. 補第 06 章 extension 安裝與測試步驟。
4. 補第 07 章 JSON / RPC 可執行範例。
5. 建立作業繳交範本。

## P1：次重要

1. 補 Windows / PowerShell / Git Bash 指令對照表。
2. 補各章小測驗參考答案。
3. 補 final project proposal template。
4. 補 `.gitignore`。
5. 補常見錯誤排除索引。

## P2：加分

1. 補截圖。
2. 補投影片大綱。
3. 補課堂講師逐字稿。
4. 補企業導入案例。

---

# 總結

以學習者角度看，這本教材的方向是對的，路線清楚，sample project 也能正常執行。主要卡關不在概念，而在「從文件到操作」的落差。

下一步最值得補強的是：

- 每章完整操作劇本
- 可複製貼上的指令
- 預期輸出
- 作業繳交範本
- extension / SDK 的驗證步驟
