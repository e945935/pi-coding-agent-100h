# Pi Coding Agent 100 小時課程大綱

## 01 基礎入門，10 小時

### 學習目標

- 知道 Pi Coding Agent 的定位與使用情境
- 完成安裝、登入與第一個 session
- 理解基本工具：read、write、edit、bash
- 能建立專案指示檔 AGENTS.md

### 官方文件對應

- README.md
- docs/quickstart.md
- docs/usage.md
- docs/providers.md

### 建議課次

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Pi 介紹、安裝與啟動 | 2 |
| 2 | 登入、provider 與模型選擇 | 2 |
| 3 | 基本工具與第一個任務 | 3 |
| 4 | AGENTS.md 與專案規範 | 2 |
| 5 | 綜合練習 | 1 |

---

## 02 互動模式與 Session 工作流，15 小時

### 學習目標

- 熟悉互動模式、slash commands、檔案引用
- 能管理 session、分支、恢復與 compaction
- 能使用 print / json 模式做一次性任務

### 官方文件對應

- docs/usage.md
- docs/sessions.md
- docs/compaction.md
- docs/session-format.md
- docs/json.md

### 建議課次

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Interactive mode 與編輯器操作 | 3 |
| 2 | @file、貼上圖片/文字與 shell command | 3 |
| 3 | Session 儲存、resume、命名 | 3 |
| 4 | tree、fork、clone 與 compaction | 4 |
| 5 | print mode / json mode 實作 | 2 |

---

## 03 設定、安全與平台環境，10 小時

### 學習目標

- 能設定全域與專案設定
- 理解安全邊界、project trust 與 sandbox
- 能在 Windows / terminal / tmux 等環境穩定使用

### 官方文件對應

- docs/settings.md
- docs/security.md
- docs/containerization.md
- docs/windows.md
- docs/terminal-setup.md
- docs/tmux.md
- docs/shell-aliases.md
- docs/environment-variables.md

### 建議課次

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Settings 與環境變數 | 2 |
| 2 | Windows 與 Terminal 設定 | 2 |
| 3 | Shell aliases 與 tmux | 2 |
| 4 | Security、trust 與 secrets 管理 | 2 |
| 5 | Containerization 與安全工作流 | 2 |

---

## 04 Provider、模型與本地模型，10 小時

### 學習目標

- 理解 subscription provider 與 API-key provider
- 能新增與切換模型
- 能理解本地模型與 llama.cpp 整合概念

### 官方文件對應

- docs/providers.md
- docs/models.md
- docs/llama-cpp.md
- docs/custom-provider.md

### 建議課次

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Provider 類型與登入方式 | 2 |
| 2 | API key 與雲端 provider | 2 |
| 3 | 模型選擇與 model catalog | 2 |
| 4 | Custom models | 2 |
| 5 | llama.cpp 與本地模型 | 2 |

---

## 05 Prompt Templates、Skills、Themes，15 小時

### 學習目標

- 能建立可重複使用的 prompt template
- 能設計與使用 skills
- 能調整 themes
- 能理解 pi package 的共享方式

### 官方文件對應

- docs/prompt-templates.md
- docs/skills.md
- docs/themes.md
- docs/packages.md

### 建議課次

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Prompt template 基礎 | 3 |
| 2 | Slash command 型 prompt 實作 | 3 |
| 3 | Skills 概念與實作 | 4 |
| 4 | Themes 與使用者體驗 | 2 |
| 5 | Pi packages 與團隊共享 | 3 |

---

## 06 Extensions 開發，20 小時

### 學習目標

- 能撰寫 TypeScript extension
- 能註冊 custom tool 與 custom command
- 能攔截 tool call、處理 lifecycle events
- 能建立簡單自訂 UI 與安全防護 extension

### 官方文件對應

- docs/extensions.md
- docs/tui.md
- examples/extensions/

### 建議課次

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Extension 架構與放置位置 | 2 |
| 2 | 第一個 /hello command | 3 |
| 3 | registerTool 自訂工具 | 4 |
| 4 | Lifecycle events | 3 |
| 5 | 攔截危險 tool call | 3 |
| 6 | 自訂 UI 與互動流程 | 3 |
| 7 | Extension 專題實作 | 2 |

---

## 07 SDK、RPC 與 JSON 整合，15 小時

### 學習目標

- 能用 Node.js 建立 Pi SDK 應用
- 能訂閱 event stream 並顯示輸出
- 能使用 RPC / JSON 模式整合自動化流程

### 官方文件對應

- docs/sdk.md
- docs/rpc.md
- docs/json.md
- examples/sdk/

### 建議課次

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | SDK 核心概念 | 3 |
| 2 | createAgentSession 實作 | 3 |
| 3 | Event stream 與 streaming output | 3 |
| 4 | RPC mode | 3 |
| 5 | JSON mode 與自動化 CLI | 3 |

---

## 08 總整專題，5 小時

### 學習目標

- 整合前面所學，完成一個可展示的 Pi 客製化專案

### 專題方向

1. 團隊版 Pi 開發環境
2. 安全防護 extension
3. 自動 code review workflow
4. SDK-based 小型 coding assistant
5. Pi package 套件化發佈

### 成果要求

- README
- 安裝步驟
- Demo script
- 至少一個實作功能
- 說明使用到的官方文件概念
