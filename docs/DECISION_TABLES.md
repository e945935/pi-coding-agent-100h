# 決策表：Pi 能力怎麼選

## Prompt Template vs Skill vs Extension

| 需求 | 建議選擇 | 原因 |
|---|---|---|
| 一段固定提示詞 | Prompt Template | 最簡單，檔案即 slash command |
| Code review checklist | Prompt Template | 多數情況不需要程式碼 |
| 複雜 SOP 或教學流程 | Skill | 可寫完整工作手冊與輔助文件 |
| 特定領域能力，例如 PDF 處理流程 | Skill | 讓 agent 按需載入能力 |
| 新增 LLM 可呼叫工具 | Extension | 可用 `registerTool` |
| 新增互動式命令 | Extension | 可用 `registerCommand` 與 UI |
| 阻擋危險指令 | Extension | 可攔截 `tool_call` |
| 改 terminal 外觀 | Theme | 用 theme 處理，不要寫 extension |
| 分享整套工作流 | Pi Package | 可包 prompts、skills、extensions、themes |

## Extension vs SDK vs RPC vs JSON mode

| 需求 | 建議選擇 |
|---|---|
| 想改變 Pi 在 TUI 裡的行為 | Extension |
| 想新增工具給 Pi 裡的模型用 | Extension |
| 想在 Node.js app 內直接建立 agent session | SDK |
| 想從 Python / Go / Rust 等語言控制 Pi | RPC |
| 想把一次性任務接到 shell pipeline | JSON mode |
| 想保存完整 session 並自訂 runtime | SDK |
| 只想取得結構化事件 | JSON mode |

## Session 操作怎麼選

| 需求 | 指令 |
|---|---|
| 繼續最近一次工作 | `pi -c` |
| 從清單選 session | `pi -r` 或 `/resume` |
| 開新任務 | `/new` |
| 從目前點嘗試另一種解法 | `/fork` |
| 複製完整 session 另開版本 | `/clone` |
| 查看或切換分支 | `/tree` |
| 上下文太長但要繼續 | compaction |

## Model 選擇策略

| 任務 | 建議模型類型 |
|---|---|
| 複雜架構分析 | 高品質 reasoning model |
| 大型 refactor | 高品質、高 context model |
| 文件摘要 | 快速、低成本模型 |
| 批次產生文件 | 成本可控模型 |
| 本地敏感資料 | local model / llama.cpp |
| 實驗與教學 | 成本低、速度快模型 |
