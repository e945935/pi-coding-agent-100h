# Pi RPC Client 範例

這個範例示範如何從 Node.js 啟動 `pi --mode rpc`，送出一個 prompt，讀取 JSONL events，並在 `agent_end` 後結束。

## 執行

```bash
cd examples/rpc-client
npm run start -- "請用一句話摘要目前專案"
```

## 注意事項

- 執行前請先確認 `pi` 可執行。
- 請先在互動模式完成 `/login` 與 `/model`。
- 真實產品需處理 timeout、abort、extension UI request/response 與錯誤重試。
