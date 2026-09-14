# Settings 範例

> 實際設定項目可能隨 Pi 版本調整，請以官方 `docs/settings.md` 為準。

## 專案設定檔

常見位置：

```text
.pi/settings.json
```

## 範例：加入外部 skills 目錄

```json
{
  "skills": ["../.claude/skills"]
}
```

## 範例：明確加入 prompt templates

```json
{
  "prompts": [".pi/prompts", "../shared-prompts"]
}
```

## 建議管理方式

- 專案共用設定可提交 Git
- 個人 API key 不要提交 Git
- 團隊設定修改需 code review
- project-local extensions 應視為程式碼審查
