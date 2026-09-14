# 06 Extensions 開發，12 小時

## 本章情境

你想讓 Pi 更符合團隊工作流，例如新增 `/hello` 指令、提供自訂工具，或在 Pi 嘗試執行危險指令時跳出確認。本章會從安裝、載入到測試 extension 完整走一次。

## 學習目標

完成本模組後，學員能夠：

- 撰寫 TypeScript extension
- 註冊 custom command
- 註冊 custom tool
- 監聽 lifecycle events
- 攔截與封鎖危險 tool call
- 使用簡單 UI 互動
- 設計專案或團隊用 extension

## 官方文件對應

- `docs/extensions.md`
- `docs/tui.md`
- `examples/extensions/`

## Extension 放置位置

| 位置 | 範圍 |
|---|---|
| `~/.pi/agent/extensions/*.ts` | 全域 |
| `~/.pi/agent/extensions/*/index.ts` | 全域子目錄 |
| `.pi/extensions/*.ts` | 專案 |
| `.pi/extensions/*/index.ts` | 專案子目錄 |

> 注意：Extension 是程式碼，具備完整系統權限，只能載入可信來源。

## 完整流程：載入 `/hello` command

### 步驟 1：切到 sample project

```bash
cd /path/to/pi-coding-agent-100h/sample-project
```

PowerShell：

```powershell
cd C:\path\to\pi-coding-agent-100h\sample-project
```

### 步驟 2：建立專案 extension 目錄

Git Bash / macOS / Linux：

```bash
mkdir -p .pi/extensions
```

PowerShell：

```powershell
New-Item -ItemType Directory -Force .pi\extensions
```

### 步驟 3：複製 hello extension

Git Bash：

```bash
cp /c/Users/user/pi-coding-agent-100h/examples/extensions/hello.ts .pi/extensions/hello.ts
```

PowerShell：

```powershell
Copy-Item C:\Users\user\pi-coding-agent-100h\examples\extensions\hello.ts .pi\extensions\hello.ts
```

### 步驟 4：啟動或重新載入 Pi

```bash
pi
```

若 Pi 已經開啟，輸入：

```text
/reload
```

### 步驟 5：測試 command

在 Pi 中輸入：

```text
/hello Taiwan
```

預期結果：畫面出現類似 `Hello Taiwan!` 的通知。

## 完整流程：測試安全防護 extension

### 步驟 1：複製 extension

Git Bash：

```bash
cp /c/Users/user/pi-coding-agent-100h/examples/extensions/safety-guard.ts .pi/extensions/safety-guard.ts
```

PowerShell：

```powershell
Copy-Item C:\Users\user\pi-coding-agent-100h\examples\extensions\safety-guard.ts .pi\extensions\safety-guard.ts
```

### 步驟 2：重新載入

```text
/reload
```

### 步驟 3：要求 Pi 執行危險任務

請用安全測試資料夾，不要使用真實重要路徑：

```text
請建立 test-danger 資料夾，然後嘗試刪除它。刪除前如果 extension 要求確認，請停下來等我選擇。
```

預期結果：當 Pi 嘗試執行包含危險片段的指令時，extension 會跳出確認；拒絕後操作會被封鎖。

## 自訂 Tool 範例

`examples/extensions/greet-tool.ts` 示範如何註冊 `greet` tool。它使用 `typebox` 定義參數 schema。Pi extension 可從 `@earendil-works/pi-coding-agent` 與文件允許的套件匯入 API；若你在獨立 TypeScript 專案中編輯，可能需要安裝相依套件以取得型別提示。

## 測試紀錄範本

```markdown
# Extension 測試紀錄

## 測試環境

- Pi 版本：
- Shell：
- Extension：

## 測試項目

| 項目 | 操作 | 預期結果 | 實際結果 |
|---|---|---|---|
| `/hello` | `/hello Taiwan` | 顯示通知 |  |
| 危險指令 | 要求刪除測試資料夾 | 跳出確認 |  |
| 保護路徑 | 要求修改 `.env` | 跳出確認 |  |
```

## 實作任務

請完成一個安全防護 extension，至少做到：

- 阻擋 `rm -rf`
- 修改 `.env` 前要求確認
- 阻擋寫入 `node_modules`
- 執行 `sudo` 前要求確認

## 驗收標準

- [ ] Extension 可被 Pi 載入
- [ ] 有一個 custom command 或 custom tool
- [ ] 能攔截至少一種危險操作
- [ ] 有測試紀錄

## 常見錯誤與排除

### Q1：`/hello` 找不到

確認 extension 是否放在 `.pi/extensions/hello.ts`，專案是否已 trust，並執行 `/reload`。

### Q2：TypeScript 編輯器顯示找不到型別

這不一定代表 Pi 無法載入。若要在編輯器中取得型別提示，可建立 Node.js 專案並安裝 `@earendil-works/pi-coding-agent`。

### Q3：安全防護沒有跳出確認

確認實際指令是否包含 extension 檢查的關鍵字，例如 `rm -rf`、`sudo`。不同 shell 的刪除指令可能不同。

## 我學會了嗎？

- [ ] 我能把 extension 放到正確位置
- [ ] 我能用 `/reload` 重新載入 extension
- [ ] 我能測試 custom command
- [ ] 我知道 extension 具有安全風險
