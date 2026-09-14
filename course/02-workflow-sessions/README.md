# 02 互動模式與 Session 工作流，15 小時

## 本章情境

你已經會啟動 Pi，接下來要學會管理一段較長的開發任務：引用檔案、執行指令、恢復 session，並針對同一個問題建立兩個分支比較解法。

## 學習目標

完成本模組後，學員能夠：

- 熟悉互動模式與常用 slash commands
- 使用 `@file` 引用檔案
- 使用 `!` 與 `!!` 執行 shell 指令
- 管理 session、resume、fork、clone、tree
- 理解 compaction 的使用時機
- 使用 print / JSON mode 完成一次性任務

## 官方文件對應

- `docs/usage.md`
- `docs/sessions.md`
- `docs/compaction.md`
- `docs/session-format.md`
- `docs/json.md`

## 課程安排

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Interactive mode 與編輯器操作 | 3 |
| 2 | `@file`、貼上內容與 shell command | 3 |
| 3 | Session 儲存、resume 與命名 | 3 |
| 4 | tree、fork、clone 與 compaction | 4 |
| 5 | print mode / JSON mode 實作 | 2 |

## 指令比較表

| 指令 | 用途 | 使用時機 |
|---|---|---|
| `pi -c` | 繼續最近 session | 昨天的任務今天繼續 |
| `pi -r` | 瀏覽先前 session | 不確定要恢復哪一段工作 |
| `/resume` | 在互動模式中恢復 session | 已在 Pi 裡，想切換舊任務 |
| `/new` | 建立新 session | 要開始全新任務 |
| `/fork` | 從目前節點分支 | 想嘗試不同解法 |
| `/clone` | 複製目前 session | 想保留完整上下文另開版本 |
| `/tree` | 查看 session tree | 比較分支與回到特定節點 |

## `!` 與 `!!` 使用情境

| 寫法 | 會不會放入模型上下文 | 適合情境 |
|---|---|---|
| `!npm test` | 會 | 讓 Pi 根據測試錯誤修正問題 |
| `!!npm install` | 不會 | 安裝套件、清快取等不需要模型知道細節的操作 |

## 完整實作劇本：同一個 bug 兩種解法

### 步驟 1：切到 sample project

Git Bash：

```bash
cd /path/to/pi-coding-agent-100h/sample-project
```

PowerShell：

```powershell
cd C:\path\to\pi-coding-agent-100h\sample-project
```

### 步驟 2：建立任務 session

```bash
pi --name "email validation experiment"
```

### 步驟 3：引用檔案並提出任務

在 Pi 中輸入：

```text
@src/index.js @test/index.test.js
目前 isEmail 實作太簡單，請提出改善方案，但先不要修改檔案。
```

預期輸出：Pi 會說明目前只檢查 `@` 與 `.`，並提出改善方向。

### 步驟 4：方案 A，小幅改善

```text
請用最小修改改善 isEmail，並補一到兩個測試。完成後執行 npm test。
```

預期輸出：

- 修改 `src/index.js`
- 修改 `test/index.test.js`
- 執行測試並回報結果

### 步驟 5：建立分支

```text
/fork
```

### 步驟 6：方案 B，使用更嚴格規則

```text
請改用較嚴格但仍可讀的 email validation 寫法，並補更多邊界測試。完成後執行 npm test。
```

### 步驟 7：查看 session tree

```text
/tree
```

比較兩條分支：

- 方案 A 是否簡單、安全、容易維護？
- 方案 B 是否更完整，但可能過度設計？

### 步驟 8：記錄結果

將結果填入：

```text
submissions/assignment-02-template.md
```

## Print mode 練習

在一般終端機執行：

```bash
pi -p "請摘要這個 repo，列出測試、lint、build 指令。"
```

JSON mode：

```bash
pi --mode json "請用一句話摘要這個 repo" 2>/dev/null
```

預期 JSON mode 會輸出多行 JSON events，例如 `session`、`agent_start`、`message_update`、`agent_end`。

## 實作任務

選一個小型 bug 或 refactor 任務，請 Pi 用兩種方案處理，並記錄：

- 兩個方案差異
- 測試結果
- 最終採用方案
- 採用理由

## 驗收標準

- [ ] 能恢復 session
- [ ] 能使用 fork 或 clone
- [ ] 能用 `@file` 指定脈絡
- [ ] 能用 print mode 完成一次性摘要
- [ ] 能填寫 `assignment-02-template.md`

## 常見錯誤與排除

### Q1：`@README.md` 找不到檔案

請確認 Pi 是在專案根目錄啟動。可先用 `pwd` 或 `Get-Location` 確認目前路徑。

### Q2：不確定 fork 成功沒有

使用 `/tree` 查看目前 session 結構。

### Q3：測試失敗後不知道怎麼辦

把測試輸出交給 Pi：

```text
!npm test
```

然後請 Pi 根據錯誤修正。

## 我學會了嗎？

- [ ] 我知道 `!` 與 `!!` 的差異
- [ ] 我知道何時該使用 `/fork`
- [ ] 我能用 `/tree` 查看分支
- [ ] 我能用 print mode 完成一次性任務
