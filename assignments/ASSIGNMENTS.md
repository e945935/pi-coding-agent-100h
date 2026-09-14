# 作業與實作題

## 作業 1：建立第一個 Pi 專案工作流

### 目標

讓學員熟悉 Pi 的基本使用方式。

### 任務

1. 選擇一個既有程式專案
2. 啟動 Pi
3. 請 Pi 摘要專案架構
4. 請 Pi 找出測試、lint、build 指令
5. 建立 `AGENTS.md`

### 繳交內容

請使用：

```text
submissions/assignment-01-template.md
```

需包含：

- 專案摘要
- 找到的指令
- `AGENTS.md` 內容
- 使用 Pi 過程中的觀察

---

## 作業 2：Session 分支比較

### 目標

練習 session、fork、tree 的使用。

### 任務

1. 找一個小型 bug 或 refactor 任務
2. 用兩種不同做法請 Pi 處理
3. 使用 session 分支管理兩種方案
4. 比較優缺點

### 繳交內容

請使用：

```text
submissions/assignment-02-template.md
```

需包含：

- 任務描述
- 兩種方案摘要
- 測試結果
- 最終採用方案與理由

---

## 作業 3：Prompt Template 或 Skill

### 目標

建立可重複使用的工作流。

### 任務

擇一完成：

- 建立 code review prompt template
- 建立文件整理 skill
- 建立測試產生 skill

### 繳交內容

- 檔案內容
- 使用方式
- 實際執行範例

---

## 作業 4：安全防護 Extension

### 目標

練習 extension 與 tool call 攔截。

### 任務

建立一個 extension，至少做到其中一項：

- 阻擋 `rm -rf`
- 修改 `.env` 前要求確認
- 阻擋寫入 `node_modules`
- 執行 `sudo` 前要求確認

### 繳交內容

- extension 程式碼
- 測試方式
- 測試結果截圖或文字記錄

---

## 作業 5：SDK 小型整合

### 目標

使用 Pi SDK 建立最小應用。

### 任務

用 Node.js 建立一個 CLI，可以：

1. 建立 Pi agent session
2. 送出 prompt
3. 顯示 streaming output

### 繳交內容

- 程式碼
- 執行方式
- Demo 結果
