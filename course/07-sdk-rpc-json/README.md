# 07 SDK、RPC 與 JSON 整合，15 小時

## 本章情境

你想把 Pi 的能力放進自己的自動化流程，例如寫一個 CLI 自動摘要 repo，或讓其他程式用 JSONL 控制 Pi。本章整理 SDK、JSON mode、RPC mode 的最小可執行思路。

## 學習目標

完成本模組後，學員能夠：

- 用 Node.js 建立 Pi SDK 應用
- 建立 agent session 並送出 prompt
- 訂閱 event stream 顯示 streaming output
- 使用 JSON mode 整合自動化流程
- 理解 RPC mode 的用途

## 官方文件對應

- `docs/sdk.md`
- `docs/rpc.md`
- `docs/json.md`
- `examples/sdk/`

## SDK、RPC、JSON mode 怎麼選？

| 方式 | 適合情境 | 優點 | 注意事項 |
|---|---|---|---|
| SDK | Node.js 應用 | API 最完整 | 需處理套件版本與模型設定 |
| RPC | 跨程序整合 | 語言無關，JSONL 溝通 | 需要管理 stdin/stdout |
| JSON mode | 一次性任務、事件串流 | 最容易接 CLI pipeline | 主要是讀事件，不適合複雜互動 |

## SDK 實作

範例位置：

```text
examples/sdk/
```

### 步驟 1：安裝

```bash
cd /c/Users/user/pi-coding-agent-100h/examples/sdk
npm install
```

PowerShell：

```powershell
cd C:\Users\user\pi-coding-agent-100h\examples\sdk
npm install
```

### 步驟 2：確認已登入 provider

SDK 需要可用模型。請先確認互動模式可正常使用：

```bash
pi
```

在 Pi 裡執行：

```text
/model
```

### 步驟 3：執行 SDK 範例

```bash
npm run start -- "請用三點摘要目前資料夾"
```

預期輸出：終端機會 streaming 顯示模型回覆。

## JSON mode 可執行範例

```bash
cd /c/Users/user/pi-coding-agent-100h/sample-project
pi --mode json "請用一句話摘要這個 repo" 2>/dev/null
```

可能輸出片段：

```json
{"type":"session","version":3,"id":"...","timestamp":"...","cwd":"..."}
{"type":"agent_start"}
{"type":"turn_start"}
{"type":"message_update","assistantMessageEvent":{"type":"text_delta","delta":"這是一個..."}}
{"type":"agent_end","messages":[...]}
```

若有安裝 `jq`，可篩選最後訊息：

```bash
pi --mode json "請用一句話摘要這個 repo" 2>/dev/null | jq -c 'select(.type == "message_end")'
```

## RPC mode 最小概念範例

RPC mode 使用 JSONL，一行一個 JSON command。最核心的 prompt command 長這樣：

```json
{"id":"req-1","type":"prompt","message":"Hello, world!"}
```

Pi 接受後會回傳 response，後續事件會繼續 streaming：

```json
{"id":"req-1","type":"response","command":"prompt","success":true}
```

### Node.js RPC 示意程式

```javascript
import { spawn } from "node:child_process";

const agent = spawn("pi", ["--mode", "rpc"], {
  stdio: ["pipe", "pipe", "inherit"],
});

agent.stdout.on("data", (chunk) => {
  process.stdout.write(chunk);
});

agent.stdin.write(JSON.stringify({
  id: "req-1",
  type: "prompt",
  message: "請用一句話摘要目前專案。",
}) + "\n");
```

> 注意：RPC 是進階主題，真實產品中還要處理流程結束、錯誤、timeout、extension UI request/response 等問題。

## 沒有 provider 時怎麼辦？

如果尚未登入 provider，SDK / JSON / RPC 都可能無法完成模型呼叫。請先：

1. 執行 `pi`
2. 使用 `/login`
3. 使用 `/model` 確認可用模型
4. 再回來執行範例

## 實作任務

建立一個 Node.js CLI：

1. 接收使用者輸入 prompt
2. 建立 Pi agent session
3. 顯示 streaming output
4. 結束後釋放 session

## 驗收標準

- [ ] 可執行 SDK 程式
- [ ] 能送出 prompt
- [ ] 能顯示 streaming output
- [ ] 能用 JSON mode 看到事件流
- [ ] 能說明 SDK、RPC、JSON mode 差異

## 常見錯誤與排除

### Q1：SDK 執行後沒有回覆

確認已登入 provider，且 `/model` 中有可用模型。

### Q2：JSON mode 輸出混雜錯誤訊息

可先把 stderr 導到其他地方：

```bash
pi --mode json "prompt" 2>/dev/null
```

### Q3：`jq` 找不到

`jq` 只是輔助工具，不是必要。沒有安裝也可以直接看 JSONL。

## 我學會了嗎？

- [ ] 我能跑 SDK minimal example
- [ ] 我能用 JSON mode 取得事件
- [ ] 我知道 RPC command 是 JSONL
- [ ] 我知道沒有 provider 時要先 `/login` 與 `/model`
