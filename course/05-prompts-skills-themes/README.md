# 05 Prompt Templates、Skills、Themes，8 小時

## 本章情境

你已經能使用 Pi 完成任務，接下來要把常用工作流程變成可重複使用的 prompt template 或 skill，讓團隊成員不必每次重新輸入同一大段提示詞。

## 學習目標

完成本模組後，學員能夠：

- 建立 reusable prompt template
- 用 slash command 形式啟動常用任務
- 理解 skills 的用途與設計方式
- 調整 terminal theme
- 了解 pi package 如何共享設定與能力

## 官方文件對應

- `docs/prompt-templates.md`
- `docs/skills.md`
- `docs/themes.md`
- `docs/packages.md`

## 放置位置

### Prompt templates

Pi 會載入：

| 範圍 | 位置 |
|---|---|
| 全域 | `~/.pi/agent/prompts/*.md` |
| 專案 | `.pi/prompts/*.md` |
| 套件 | package 中的 `prompts/` 或 `pi.prompts` |

檔名就是 slash command 名稱。例如：

```text
.pi/prompts/review.md
```

在 Pi 中可輸入：

```text
/review
```

### Skills

Pi 會載入：

| 範圍 | 位置 |
|---|---|
| 全域 | `~/.pi/agent/skills/` |
| 專案 | `.pi/skills/` |
| 相容 Agent Skills | `.agents/skills/` |

常見 skill 結構：

```text
.pi/skills/test-writer/
└─ SKILL.md
```

## Prompt template 完整流程：建立 `/review`

### 步驟 1：切到 sample project

```bash
cd /path/to/pi-coding-agent-100h/sample-project
```

PowerShell：

```powershell
cd C:\path\to\pi-coding-agent-100h\sample-project
```

### 步驟 2：建立 prompt 目錄

```bash
mkdir -p .pi/prompts
```

PowerShell：

```powershell
New-Item -ItemType Directory -Force .pi\prompts
```

### 步驟 3：建立 `.pi/prompts/review.md`

內容可參考：

```markdown
請用資深工程師角度 review 目前變更。

請檢查：

1. 正確性
2. 可讀性
3. 安全性
4. 效能
5. 測試覆蓋

請用「必修 / 建議 / 可忽略」分類，並使用繁體中文、台灣習慣用語。
```

### 步驟 4：重新載入 Pi

在 Pi 裡輸入：

```text
/reload
```

### 步驟 5：執行 template

```text
/review
```

預期輸出：Pi 會依照 review template 檢查目前專案或變更。

## Skill 最小範例

建立：

```text
.pi/skills/test-writer/SKILL.md
```

內容：

```markdown
---
name: test-writer
description: 協助根據既有 JavaScript 程式碼產生或改善單元測試。
---

# Test Writer Skill

當使用者要求補測試、改善測試覆蓋或分析測試案例時，請使用本 skill。

## 工作流程

1. 先閱讀目標檔案與既有測試
2. 找出尚未覆蓋的正常、邊界與錯誤情境
3. 先提出測試計畫
4. 經使用者同意後再修改測試檔案
5. 執行測試並回報結果
```

使用：

```text
/skill:test-writer 請幫 src/index.js 補測試
```

## Theme

Theme 用來調整 Pi 的終端機外觀。學員第一輪只需要知道可以透過設定或 theme 檔調整外觀即可，詳細製作可作為延伸挑戰。

## 實作任務

請建立一個團隊常用工作流，擇一：

1. Code review prompt template
2. 測試產生 skill
3. 文件摘要 skill
4. Release note prompt template

## 驗收標準

- [ ] 能說明 prompt template 與 skill 差異
- [ ] 有一個可重複使用的 prompt 或 skill
- [ ] 能用 slash command 或 `/skill:name` 叫用
- [ ] 有實際執行紀錄
- [ ] 能說明如何共享給團隊

## 常見錯誤與排除

### Q1：輸入 `/review` 沒反應

確認檔案是否放在 `.pi/prompts/review.md`，並執行 `/reload`。

### Q2：Skill 沒出現在可用清單

確認 `SKILL.md` 是否有 frontmatter，且 `description` 不可空白。

### Q3：專案 prompt template 沒載入

專案可能尚未被 trust。請確認 Pi 是否信任此專案。

## 我學會了嗎？

- [ ] 我能建立 `.pi/prompts/review.md`
- [ ] 我能用 `/review` 執行 prompt template
- [ ] 我能建立含 `SKILL.md` 的 skill
- [ ] 我能說明什麼情況用 prompt，什麼情況用 skill
