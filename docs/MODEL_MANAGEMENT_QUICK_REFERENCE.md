# Model Management Quick Reference

## 常用指令

| 操作 | 指令 |
|---|---|
| 開啟模型選擇器 | `/model` 或 Ctrl+L |
| 儲存預設模型 | 在 model picker 中按 Ctrl+S |
| 切換 thinking level | `/thinking` |
| 儲存預設 thinking level | 在 thinking picker 中按 Ctrl+S |
| 強制更新 model catalog | `pi update --models` |

## Subscription vs API key

| 類型 | 優點 | 注意事項 |
|---|---|---|
| Subscription login | 不必手動管理 API key，適合個人使用 | 受帳號方案、provider 限制影響 |
| API key | 適合團隊、CI、自動化與明確成本控管 | 要管理金鑰、額度與安全 |

## 選模型建議

- 先用穩定、工具能力好的模型完成教學
- 批次摘要或文件任務可選低成本模型
- 複雜修改、架構分析、extension debug 建議選高品質模型
- 沒有多模型環境時，作業可改成比較不同 prompt 或 thinking level
