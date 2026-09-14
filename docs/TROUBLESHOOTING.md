# 常見問題排除

## `pi` 找不到

```bash
pi --version
```

確認 Pi 已安裝，並重新開啟終端機。若用 npm 全域安裝，確認 npm global bin 在 PATH。

## 沒有可用模型

1. 執行 `/login`
2. 執行 `/model`
3. 確認 provider、帳號方案或 API key
4. 執行 `pi update --models`

## Pi 修改錯檔案

先不要繼續操作：

```bash
git status
git diff
```

確認後可回復單一檔案：

```bash
git restore <file>
```

## Prompt template 沒出現

確認：

- 檔案副檔名是 `.md`
- 檔案在 `.pi/prompts/` 或 `~/.pi/agent/prompts/`
- 檔名沒有空白或特殊字元
- 已執行 `/reload`
- 專案已 trust

## Skill 沒有載入

確認 `SKILL.md` 有 frontmatter：

```markdown
---
name: example-skill
description: 清楚說明 skill 用途與使用時機。
---
```

## Extension 沒有載入

確認：

- 放在 `.pi/extensions/` 或 `~/.pi/agent/extensions/`
- export default function 正確
- 已執行 `/reload`
- 專案已 trust
- 檢查 Pi 顯示的載入錯誤

## SDK / RPC 沒有回覆

- 確認 provider 可用
- 確認 `/model` 有可用模型
- 確認 stdin 每筆 JSON 後都有 `\n`
- 確認 stdout 沒混入非 JSON 訊息
- 檢查是否等待 `agent_end`

## 回報問題應附上

- 作業系統與 shell
- Node.js、npm、Pi 版本
- provider / model 名稱（不要附 API key）
- 執行指令
- 預期與實際結果
- 完整錯誤訊息
