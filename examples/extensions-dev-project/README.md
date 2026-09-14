# Extension 開發專案骨架

這個資料夾提供較完整的 TypeScript extension 開發環境。

## 安裝

```bash
cd examples/extensions-dev-project
npm install
```

## Typecheck

```bash
npm run typecheck
```

## 複製到 sample project

```bash
npm run copy:sample
```

然後到 sample project：

```bash
cd ../../sample-project
pi
```

在 Pi 中測試：

```text
/reload
/hello Taiwan
```

## 檔案

- `src/hello.ts`：custom command 範例
- `src/safety-guard.ts`：攔截危險 bash 指令範例

## 注意事項

Extension 會在 Pi process 內執行，具有本機權限。請只載入可信任程式碼。
