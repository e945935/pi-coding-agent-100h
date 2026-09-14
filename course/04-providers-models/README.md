# 04 Provider、模型與本地模型，10 小時

## 學習目標

完成本模組後，學員能夠：

- 理解 subscription provider 與 API-key provider
- 使用 `/model` 選擇模型
- 設定預設模型與 thinking level
- 新增 custom model
- 理解 llama.cpp 與本地模型整合情境

## 官方文件對應

- `docs/providers.md`
- `docs/models.md`
- `docs/llama-cpp.md`
- `docs/custom-provider.md`

## 課程安排

| 課次 | 主題 | 時數 |
|---|---|---:|
| 1 | Provider 類型與登入方式 | 2 |
| 2 | API key 與雲端 provider | 2 |
| 3 | 模型選擇與 model catalog | 2 |
| 4 | Custom models | 2 |
| 5 | llama.cpp 與本地模型 | 2 |

## 核心觀念

不同模型適合不同任務。高品質模型適合架構分析、複雜 refactor；速度快或成本低的模型適合摘要、文件整理、簡單修改。

選模型時可以考慮：

- 任務複雜度
- context 長度
- 工具使用能力
- 成本
- 延遲
- 是否可用本地模型

## 操作練習

### 選擇模型

```text
/model
```

在 model picker 中可選擇模型，並可儲存為預設。

### 設定 thinking level

```text
/thinking
```

或使用快捷鍵切換。

## 實作任務

用三個不同模型完成同一個任務，例如：

```text
請閱讀這個 repo，找出最適合新增單元測試的三個地方。
```

記錄：

- 回答品質
- 執行時間
- 工具使用情況
- 適合使用情境

## 驗收標準

- [ ] 能使用 `/model` 切換模型
- [ ] 能說明 subscription 與 API-key 差異
- [ ] 能設計模型選用策略
- [ ] 理解 custom model 與 local model 用途
