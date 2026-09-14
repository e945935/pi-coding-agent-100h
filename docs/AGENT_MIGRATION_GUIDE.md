# 從其他 Coding Agent 遷移到 Pi

本指南給已經用過 Claude Code、Codex、Cursor、Windsurf、Aider、Copilot Coding Agent、Cline / Continue 類工具的讀者。

## 你需要先知道的 Pi 心智模型

Pi 是一個 minimal terminal coding harness。它刻意保持核心小，透過下列方式擴充：

- Context files：`AGENTS.md`、`CLAUDE.md`
- Prompt templates：可重複使用的 slash prompt
- Skills：可按需載入的工作手冊
- Extensions：TypeScript 擴充，能新增工具、指令、事件攔截與 UI
- SDK / RPC / JSON mode：嵌入或整合到其他系統

## 90 分鐘快速遷移 Lab

| 步驟 | 任務 | 時間 |
|---|---|---:|
| 1 | 確認安裝：`pi --version` | 5 分 |
| 2 | 登入：`/login`，選模型：`/model` | 10 分 |
| 3 | 建立 `AGENTS.md` | 10 分 |
| 4 | 對 sample project 做 repo summary | 10 分 |
| 5 | 使用 `/fork` 比較兩種修法 | 20 分 |
| 6 | 建立 `.pi/prompts/review.md` 並執行 `/review` | 15 分 |
| 7 | 載入 hello extension，測試 `/hello` | 15 分 |
| 8 | 用 JSON mode 看事件流 | 5 分 |

## 常見功能對照

| 需求 | 其他 agent 常見做法 | Pi 做法 |
|---|---|---|
| 專案規則 | Cursor rules、Claude instructions、Codex instructions | `AGENTS.md` / `CLAUDE.md` |
| 重新載入規則 | 重啟或 reload rules | `/reload` |
| 快速引用檔案 | @file、context picker | `@file` |
| 對話續接 | Chat history | `pi -c`、`pi -r`、`/resume` |
| 嘗試不同解法 | 複製對話、開新 chat | `/fork`、`/clone`、`/tree` |
| 固定提示詞 | Custom command、prompt snippets | Prompt templates |
| 可重複工作流程 | Rules、playbook、skills | Skills |
| 新增工具 | MCP、外掛、tool server | Extensions 或 SDK |
| 攔截危險操作 | Approval / sandbox | Extension `tool_call` 攔截、project trust、containerization |
| 程式化整合 | API / CLI | SDK、RPC、JSON mode |

## Context files 對照

Pi 會載入：

- `~/.pi/agent/AGENTS.md`：全域指示
- 專案或父層的 `AGENTS.md` / `CLAUDE.md`
- 若同層有 `AGENTS.override.md`，會取代該層 `AGENTS.md` 或 `CLAUDE.md`

建議把跨專案偏好放全域，把專案規則放專案根目錄。

## Prompt、Skill、Extension、SDK、RPC 怎麼選？

| 需求 | Prompt Template | Skill | Extension | SDK | RPC / JSON |
|---|---:|---:|---:|---:|---:|
| 固定提示詞 | ✅ |  |  |  |  |
| 多步驟工作手冊 |  | ✅ |  |  |  |
| 新增 slash command | ✅ | ✅ | ✅ |  |  |
| 新增 LLM 可呼叫工具 |  |  | ✅ | ✅ |  |
| 攔截 tool call |  |  | ✅ |  |  |
| 自訂 UI |  |  | ✅ | ✅ |  |
| 嵌入 Node.js app |  |  |  | ✅ |  |
| 跨語言程序整合 |  |  |  |  | ✅ |
| 一次性結構化事件輸出 |  |  |  |  | ✅ |

## Pi Extension vs MCP Server

| 項目 | Pi Extension | MCP Server |
|---|---|---|
| 執行位置 | Pi process 內 | 外部 server/process |
| 主要用途 | 改變 Pi 行為、註冊工具、指令、事件攔截 | 提供跨工具可用的外部工具 |
| 可攔截 Pi tool call | ✅ | 通常不行 |
| 可自訂 Pi TUI | ✅ | 通常不行 |
| 跨 agent 共用 | 較低 | 較高 |
| 權限風險 | 高，等同執行本機程式碼 | 視 server 權限而定 |

## Pi 的獨特賣點

- 核心工具少，讀寫與執行行為容易理解
- Session tree / fork 適合比較不同解法
- TypeScript extension 可直接擴充與攔截 Pi 行為
- SDK / RPC / JSON mode 讓 Pi 不只是一個 TUI 工具
- Skills、prompt templates、themes、packages 可逐步組合成團隊工作流

## 建議遷移順序

1. 先把既有 rules 轉成 `AGENTS.md`
2. 把常用 prompt 轉成 `.pi/prompts/*.md`
3. 把多步驟 SOP 轉成 `.pi/skills/*/SKILL.md`
4. 需要工具或安全攔截時，再寫 extension
5. 需要整合到產品或 pipeline 時，再用 SDK / RPC / JSON mode
