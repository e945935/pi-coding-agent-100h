# 01 基礎入門，10 小時

## 本章情境

你剛加入一個陌生專案，需要快速了解專案架構、執行方式、測試方式，並建立一套讓 Pi Coding Agent 遵守的專案規則。本章會帶你從零開始完成第一個 Pi 工作流。

## 學習目標

完成本模組後，學員能夠：

- 安裝並啟動 Pi Coding Agent
- 使用 `/login` 或 API key 完成驗證
- 理解 Pi 預設工具 `read`、`write`、`edit`、`bash`
- 在專案中建立 `AGENTS.md`
- 完成第一個程式碼分析任務

## 先備知識

- 會使用終端機切換資料夾
- 知道 Git 基本概念
- 具備基本程式專案經驗

## 官方文件對應

- `README.md`
- `docs/quickstart.md`
- `docs/usage.md`
- `docs/providers.md`

## 課程安排

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Pi 介紹、安裝與啟動 | 2 |
| 2 | 登入、provider 與模型選擇 | 2 |
| 3 | 基本工具與第一個任務 | 3 |
| 4 | AGENTS.md 與專案規範 | 2 |
| 5 | 綜合練習 | 1 |

## 核心觀念

Pi 是一個終端機裡的 coding agent harness。它的核心很小，主要透過工具、設定、context files、extensions、skills 與 prompt templates 擴充。

預設情況下，Pi 會提供模型四個主要工具：

| 工具 | 用途 | 風險 |
|---|---|---|
| `read` | 讀取檔案 | 可能讀到敏感資訊 |
| `write` | 建立或覆寫檔案 | 可能覆蓋重要檔案 |
| `edit` | 精準修改檔案 | 可能修改錯誤位置 |
| `bash` | 執行 shell 指令 | 可能執行危險操作 |

因此，第一天就要建立兩個習慣：

1. 使用 Git 追蹤變更
2. 使用 `AGENTS.md` 明確告訴 Pi 專案規則

## 詳細操作步驟

### 步驟 1：準備練習專案

可以使用本教材內建的 sample project：

```bash
cd C:/Users/user/pi-coding-agent-100h/sample-project
```

若你使用 macOS/Linux，請換成自己的路徑。

### 步驟 2：確認 Pi 是否可執行

```bash
pi --version
```

預期輸出：

```text
<顯示 Pi 版本號>
```

若無法執行，請先回到官方 quickstart 安裝 Pi。

### 步驟 3：啟動 Pi

```bash
pi
```

啟動後，你會進入互動模式，可以直接輸入任務。

### 步驟 4：登入 provider

在 Pi 裡輸入：

```text
/login
```

選擇你可使用的 provider。

也可以在啟動前設定 API key。以下只是格式範例，請不要把真實 key 寫入 repo 或提交 Git：

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
pi
```

Windows PowerShell 可使用：

```powershell
$env:ANTHROPIC_API_KEY="sk-ant-..."
pi
```

更多 shell 指令差異請參考 `docs/SHELL_COMMANDS.md`。

### 步驟 5：請 Pi 摘要專案

在 Pi 裡輸入：

```text
請摘要這個專案的架構，並告訴我如何執行測試、lint 與 build。
```

預期 Pi 會使用 `read` 或 `bash` 檢查專案檔案，並回覆：

- 專案用途
- 主要檔案
- 使用的語言或框架
- 可用指令
- 下一步建議

### 步驟 6：建立 AGENTS.md

在專案根目錄建立：

```markdown
# Project Instructions

- 使用繁體中文，採用台灣習慣用語。
- 修改前請先說明計畫。
- 不要修改 `.env`、憑證、金鑰或 production 設定。
- 執行刪除、部署、發佈、migration 前必須先詢問。
- 修改程式碼後請執行測試。
```

建立後，在 Pi 裡輸入：

```text
/reload
```

讓 Pi 重新載入 context files。

### 步驟 7：請 Pi 根據規則重新檢查

```text
請根據 AGENTS.md 的規則，重新檢查這個專案是否有安全或維護風險。
```

## 預期輸出

完成本章後，你應該取得：

1. 一份專案摘要
2. 一份 `AGENTS.md`
3. 一份測試、lint、build 指令清單
4. 一份專案風險與改善建議

## 實作任務

請選擇一個現有專案，完成：

1. 啟動 Pi
2. 請 Pi 摘要專案
3. 找出測試與建置指令
4. 建立 `AGENTS.md`
5. 請 Pi 根據 `AGENTS.md` 重新檢查專案

## 驗收標準

- [ ] 能成功啟動 Pi
- [ ] 能切換或確認模型
- [ ] 有一份專案摘要
- [ ] 有一份可用的 `AGENTS.md`
- [ ] 知道修改前要確認 Git 狀態

## 常見錯誤與排除

### Q1：`pi` 指令找不到

請確認 Pi 是否已安裝，並重新開啟終端機。若使用 npm 安裝，確認 npm global bin 是否在 PATH 中。

### Q2：登入後還是不能使用模型

可能是 provider 權限、API key、地區或帳號方案問題。請先用 `/model` 確認可用模型。

### Q3：Pi 找不到測試指令

請讓 Pi 檢查 `package.json`、`README.md`、`Makefile`、CI 設定檔等常見位置。

### Q4：Pi 修改了不該改的檔案

請用 Git 檢查變更：

```bash
git diff
```

必要時回復：

```bash
git restore <file>
```

舊版 Git 也可使用：

```bash
git checkout -- <file>
```

## 小測驗

1. Pi 預設提供哪四個主要工具？
2. `AGENTS.md` 的用途是什麼？
3. 為什麼使用 coding agent 前建議先確認 Git 狀態？
4. `/reload` 的用途是什麼？
5. API key 應不應該寫進專案檔案？為什麼？

## 延伸挑戰

- 為你的團隊寫一份正式版 `AGENTS.md`
- 請 Pi 幫你建立新進工程師 onboarding 文件
- 比較有無 `AGENTS.md` 時，Pi 回答品質與行為差異

## 講師備註

本章重點不是讓學員記指令，而是建立正確工作習慣：先理解專案、再設定規則、最後才讓 agent 修改檔案。
