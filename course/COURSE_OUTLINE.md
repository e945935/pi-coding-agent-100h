# Pi Coding Agent 核心自學課程大綱（60 小時）

> 若加入講師授課、完整作業、團隊實驗與延伸專題，整體課程可擴充至 80～100 小時。

## 01 基礎入門，6 小時

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
| 1 | Pi 介紹、安裝與啟動 | 1 |
| 2 | 登入、provider 與模型選擇 | 1 |
| 3 | 基本工具與第一個任務 | 2 |
| 4 | AGENTS.md 與專案規範 | 1 |
| 5 | 綜合練習 | 1 |

---

## 02 互動模式與 Session 工作流，8 小時

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
| 1 | Interactive mode 與編輯器操作 | 1 |
| 2 | @file、貼上圖片/文字與 shell command | 2 |
| 3 | Session 儲存、resume、命名 | 2 |
| 4 | tree、fork、clone 與 compaction | 2 |
| 5 | print mode / json mode 實作 | 1 |

---

## 03 設定、安全與平台環境，6 小時

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
| 1 | Settings 與環境變數 | 1 |
| 2 | Windows 與 Terminal 設定 | 1 |
| 3 | Shell aliases 與 tmux | 1 |
| 4 | Security、trust 與 secrets 管理 | 2 |
| 5 | Containerization 與安全工作流 | 1 |

---

## 04 Provider、模型與本地模型，6 小時

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
| 1 | Provider 類型與登入方式 | 1 |
| 2 | API key 與雲端 provider | 1 |
| 3 | 模型選擇與 model catalog | 1 |
| 4 | Custom models | 1 |
| 5 | llama.cpp 與本地模型 | 2 |

---

## 05 Prompt Templates、Skills、Themes，8 小時

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
| 1 | Prompt template 基礎 | 1 |
| 2 | Slash command 型 prompt 實作 | 1 |
| 3 | Skills 概念與實作 | 3 |
| 4 | Themes 與使用者體驗 | 1 |
| 5 | Pi packages 與團隊共享 | 2 |

---

## 06 Extensions 開發，12 小時

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
| 1 | Extension 架構與放置位置 | 1 |
| 2 | 第一個 /hello command | 2 |
| 3 | registerTool 自訂工具 | 3 |
| 4 | Lifecycle events | 2 |
| 5 | 攔截危險 tool call | 2 |
| 6 | 自訂 UI 與互動流程 | 1 |
| 7 | Extension 專題實作 | 1 |

---

## 07 SDK、RPC 與 JSON 整合，10 小時

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
| 1 | SDK 核心概念 | 1 |
| 2 | createAgentSession 實作 | 2 |
| 3 | Event stream 與 streaming output | 2 |
| 4 | RPC mode | 2 |
| 5 | JSON mode 與自動化 CLI | 3 |

---

## 08 總整專題，4 小時

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
