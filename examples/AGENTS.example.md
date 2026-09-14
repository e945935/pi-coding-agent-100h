# Project Instructions

請遵守以下規則：

## 語言與回覆

- 使用繁體中文，採用台灣習慣用語。
- 回覆要清楚、精簡，必要時用條列。

## 修改程式碼

- 修改前先簡短說明計畫。
- 優先使用最小修改，不要大規模重寫。
- 修改後說明改了哪些檔案與原因。

## 安全限制

- 不要修改 `.env`、憑證、金鑰或 production 設定。
- 不要刪除重要資料。
- 執行危險指令前必須先詢問。
- 不要在未確認前執行 migration、deploy、publish。

## 驗證

修改後請依序嘗試：

```bash
npm run lint
npm test
npm run build
```

如果指令不存在，請先檢查 `package.json` 或專案文件。
