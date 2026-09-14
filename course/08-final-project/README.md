# 08 總整專題，4 小時

## 學習目標

完成本模組後，學員能夠整合前面所學，完成一個可展示、可說明、可交付的 Pi Coding Agent 專題。

## 專題規模

請先依時間與能力選擇規模：

| 規模 | 建議內容 | 適合對象 |
|---|---|---|
| S | AGENTS.md + prompt template | 一般使用者 |
| M | skill 或 extension | 進階客製化 |
| L | SDK / RPC / package 化 | 系統整合 |

若課程只有 5 小時總整專題，建議選 S 或 M；若要做 L 規模，建議額外安排 8～10 小時。

## 專題方向

請擇一完成：

1. 團隊版 Pi 開發環境
2. 安全防護 extension
3. 自動 code review workflow
4. SDK-based 小型 coding assistant
5. Pi package 套件化發佈

## 專題 Proposal

開始實作前，請先填寫：

```text
final-project/PROJECT_PROPOSAL_TEMPLATE.md
```

## 成果要求

每組或每位學員需繳交：

- `README.md`
- 安裝步驟
- 使用方式
- Demo script
- 至少一個實作功能
- 測試紀錄
- 使用到哪些 Pi 官方文件概念

## 評分規準

| 項目 | 比例 |
|---|---:|
| 功能完整度 | 30% |
| 官方文件概念運用 | 25% |
| 安全性與穩定性 | 20% |
| 文件清楚度 | 15% |
| Demo 表現 | 10% |

## 建議專題一：團隊版 Pi 開發環境

內容包含：

- 團隊 `AGENTS.md`
- 常用 prompt templates
- 安全使用規範
- provider / model 建議
- onboarding 文件

## 建議專題二：安全防護 Extension

內容包含：

- 阻擋危險 bash 指令
- 保護敏感檔案
- 修改重要檔案前要求確認
- 測試案例

## 建議專題三：自動 Code Review Workflow

內容包含：

- code review prompt template
- review checklist
- 測試與 lint 指令整合
- 輸出 review 報告

## 建議專題四：SDK 小型 Coding Assistant

內容包含：

- Node.js CLI
- streaming output
- 可指定資料夾或檔案
- 自動產生摘要或改善建議

## Demo Checklist

展示前請使用：

```text
final-project/DEMO_CHECKLIST.md
```

## 繳交格式

```text
final-project/
├─ README.md
├─ src/
├─ examples/
├─ demo.md
└─ notes.md
```

## 我學會了嗎？

- [ ] 我能說明專題解決的問題
- [ ] 我能展示至少一個 Pi 客製化或整合成果
- [ ] 我能說明安全限制
- [ ] 我能提供可重現的安裝與 demo 步驟
