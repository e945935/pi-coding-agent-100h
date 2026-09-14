# 講師備課筆記

## 教學節奏建議

這門課建議以實作為主，講解為輔。

每 2 小時課程可採用：

1. 20 分鐘：核心觀念
2. 30 分鐘：講師示範
3. 50 分鐘：學員實作
4. 20 分鐘：檢討與 Q&A

## 常見學員問題

### 1. Pi 會不會亂改檔案？

會，只要你授權它使用工具，它就可能修改檔案。因此務必使用 Git、AGENTS.md、extension 防護與人工 review。

### 2. Prompt template 和 skill 差在哪？

Prompt template 適合簡單固定提示詞；skill 適合更完整、可重複、需要說明文件或資源的能力。

### 3. Extension 安全嗎？

Extension 是程式碼，具備本機權限。只載入可信任來源。

### 4. SDK 和 RPC 怎麼選？

Node.js 應用優先用 SDK。非 Node.js 或跨程序整合可考慮 RPC。只需要結構化輸出時可用 JSON mode。

## 示範專案建議

- 小型 Node.js 專案
- Python CLI 專案
- 文件型 repo
- 有測試但規模不大的開源專案

## 課前準備

- 確認 Node.js / npm 可用
- 確認 Pi 可啟動
- 準備至少一個可用 provider
- 準備一個示範 repo
- 確認終端機可正確顯示中文
