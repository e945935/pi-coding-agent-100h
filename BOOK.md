# Pi Coding Agent 100 小時實戰教材

## 使用說明

這本教材以「能實際上手、能客製化、能整合到工作流」為目標，將 Pi Coding Agent 官方文件整理成 100 小時課程。

建議學習方式：

1. 每個模組先閱讀「學習目標」與「核心觀念」
2. 跟著「操作練習」實作
3. 完成「作業」與「延伸挑戰」
4. 最後完成總整專題

## 課程總覽

| 模組 | 主題 | 時數 |
|---|---|---:|
| 01 | 基礎入門 | 10 |
| 02 | 互動模式與 Session 工作流 | 15 |
| 03 | 設定、安全與平台環境 | 10 |
| 04 | Provider、模型與本地模型 | 10 |
| 05 | Prompt Templates、Skills、Themes | 15 |
| 06 | Extensions 開發 | 20 |
| 07 | SDK、RPC 與 JSON 整合 | 15 |
| 08 | 總整專題 | 5 |
|  | **合計** | **100** |

## 學習路線

本教材可依需求拆成三種路線：

| 路線 | 適合對象 | 建議模組 | 時數 |
|---|---|---|---:|
| 使用者路線 | 想把 Pi 用在日常開發的人 | 01～04 | 45 |
| 客製化路線 | 想建立團隊工作流的人 | 01～06 | 80 |
| 系統整合路線 | 想用 SDK/RPC 整合系統的人 | 01～08 | 100 |
| 有經驗者快速路線 | 已用過 Claude Code、Codex、Cursor、Aider 等 agent 的人 | docs/AGENT_MIGRATION_GUIDE.md + 02 + 05 + 06 + 07 | 6～12 |

## 給有其他 Agent 經驗的讀者

如果你已熟悉其他 coding agent，建議先讀：

1. [docs/AGENT_MIGRATION_GUIDE.md](docs/AGENT_MIGRATION_GUIDE.md)
2. [docs/DECISION_TABLES.md](docs/DECISION_TABLES.md)
3. [course/02-workflow-sessions](course/02-workflow-sessions/README.md)
4. [course/05-prompts-skills-themes](course/05-prompts-skills-themes/README.md)
5. [course/06-extensions](course/06-extensions/README.md)
6. [course/07-sdk-rpc-json](course/07-sdk-rpc-json/README.md)

## 最低環境需求

- Node.js 與 npm
- Git
- 可正常顯示中文的終端機
- Pi Coding Agent
- 至少一個可用 provider 或 API key
- 一個可練習的程式專案

## 建議先備知識

- 會使用終端機基本指令
- 熟悉 Git 基本操作
- 有至少一種程式語言經驗
- 若要學 Extension / SDK，建議具備 TypeScript 或 JavaScript 基礎

## 評量方式

- 平時實作：40%
- 單元作業：30%
- 總整專題：30%

## 學習成果

完成後，學員應能：

- 在專案中安全使用 Pi Coding Agent
- 建立適合團隊的 AGENTS.md 與工作規範
- 管理 session、分支與任務脈絡
- 客製 prompt templates、skills、themes
- 開發 extension 擴充工具、指令與事件處理
- 用 SDK / RPC / JSON 模式整合自動化流程
