# 術語表

## Agent

能根據使用者目標，自主使用工具完成任務的 AI 系統。

## AGENTS.md

專案指示檔，用來告訴 Pi 在這個專案中應遵守的規則，例如測試指令、禁止修改的檔案、回覆語言等。

## Context

模型在回答與操作時可看到的脈絡，包含對話、檔案內容、工具輸出與 context files。

## Context File

Pi 啟動時會載入的指示檔，例如全域或專案中的 `AGENTS.md`。

## Extension

TypeScript 模組，可擴充 Pi 的工具、指令、事件處理、UI 與安全控制。

## Skill

可重複使用的 agent 能力描述，通常用來封裝一套工作方法或流程。

## Prompt Template

可重複使用的提示詞模板，通常可透過 slash command 啟動。

## Provider

模型服務來源，例如 Anthropic、OpenAI、GitHub Copilot、Gemini、Mistral 或本地模型服務。

## Model

實際執行推理的語言模型。

## Session

Pi 的工作會話，包含對話、工具呼叫、分支與狀態。Session 會自動保存，可恢復或分支。

## Compaction

將過長的上下文摘要壓縮，讓 session 可以繼續進行。

## JSON Mode

Pi 的一種輸出模式，會輸出結構化事件，方便其他程式處理。

## RPC Mode

以 stdin/stdout JSONL 方式與 Pi 整合的模式，適合跨程序控制。

## SDK

Pi 提供的 Node.js 程式化介面，可建立 agent session 並整合到自訂應用。
