# 小測驗參考答案

## 模組 01

1. `read`、`write`、`edit`、`bash`。
2. 告訴 Pi 專案規則、限制與驗證方式。
3. 確保變更可追蹤、可比較、必要時可回復。
4. 重新載入 context files、prompts、skills 或 extensions。
5. 不應該。API key 可能洩漏，應使用環境變數或安全的認證機制。

## 模組 02

1. `!` 的輸出會交給模型；`!!` 執行但不加入模型上下文。
2. `/fork` 從目前工作點建立另一條分支。
3. `/tree` 用來查看或切換 session tree。
4. print mode 適合一次性、非互動任務。

## 模組 03

1. 不要把 secrets、production 設定或不可信程式碼交給 agent 任意處理。
2. 使用 Git、AGENTS.md、確認流程與必要的 sandbox。
3. API key 不應提交到 Git。

## 模組 04

1. Subscription 透過帳號方案使用；API key 由使用者或團隊管理金鑰與費用。
2. `/model` 選擇模型。
3. `pi update --models` 強制更新模型清單。
4. 模型要依複雜度、context、工具能力、成本與延遲選擇。

## 模組 05

1. Prompt template 是固定提示詞；skill 是可按需載入的完整能力與工作流程。
2. 固定提示詞用 template，多步驟 SOP 用 skill。
3. 專案 prompt 通常放在 `.pi/prompts/`。

## 模組 06

1. Extension 可以註冊工具、指令、事件處理與 UI。
2. project-local extension 放在 `.pi/extensions/`。
3. Extension 具有本機權限，只能載入可信任來源。

## 模組 07

1. SDK 適合 Node.js 內嵌；RPC 適合跨程序或跨語言；JSON mode 適合結構化事件流。
2. JSONL 是一行一個 JSON 物件。
3. session 結束後應釋放資源，例如呼叫 `dispose()`。
