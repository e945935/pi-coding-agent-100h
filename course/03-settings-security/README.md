# 03 設定、安全與平台環境，10 小時

## 學習目標

完成本模組後，學員能夠：

- 設定 Pi 的全域與專案設定
- 管理環境變數與 API key
- 理解 project trust 與安全邊界
- 在 Windows、Terminal、tmux 等環境穩定使用
- 建立較安全的 agent 工作流程

## 官方文件對應

- `docs/settings.md`
- `docs/security.md`
- `docs/containerization.md`
- `docs/windows.md`
- `docs/terminal-setup.md`
- `docs/tmux.md`
- `docs/shell-aliases.md`
- `docs/environment-variables.md`

## 課程安排

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Settings 與環境變數 | 2 |
| 2 | Windows 與 Terminal 設定 | 2 |
| 3 | Shell aliases 與 tmux | 2 |
| 4 | Security、trust 與 secrets 管理 | 2 |
| 5 | Containerization 與安全工作流 | 2 |

## 核心觀念

Coding agent 具備讀寫檔案與執行指令能力，因此安全設定非常重要。不要把 agent 放在沒有版本控管、沒有備份、或包含敏感資料的環境中任意操作。

建議原則：

- 使用 Git 做變更追蹤
- 專案中放 `AGENTS.md` 明確限制行為
- `.env`、credentials、production config 要保護
- 大型或危險操作前要求確認
- 不信任的專案不要載入 project-local extensions

## 操作練習

### 建立安全版 AGENTS.md

```markdown
# Project Instructions

- 修改前請先說明計畫。
- 不要修改 `.env`、金鑰、憑證或 production 設定。
- 執行刪除指令前必須先詢問。
- 修改程式碼後請執行測試。
```

### 建立 shell alias

```bash
alias pic='pi -c'
alias pir='pi -r'
```

## 實作任務

請為一個專案設計「安全使用 Pi」規範，內容包含：

1. 哪些檔案禁止修改
2. 哪些指令需要先確認
3. 修改後要跑哪些檢查
4. 如何回復變更

## 驗收標準

- [ ] 有安全版 `AGENTS.md`
- [ ] 有環境變數管理策略
- [ ] 知道 project trust 的風險
- [ ] 知道如何用 Git 回復變更
