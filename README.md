# Pi Coding Agent 100 小時學習教材

本專案用來整理 Pi Coding Agent 官方文件，規劃成實作型學習教材。

核心自學內容約 60 小時；包含完整作業、講師授課、團隊實驗與延伸專題時，完整課程規模約 80～100 小時。詳細估算請參考 [TIME_ESTIMATE.md](TIME_ESTIMATE.md)。

讀者服務 repo：<https://github.com/e945935/pi-coding-agent-100h>

## 閱讀入口

建議從以下順序開始：

1. [SUMMARY.md](SUMMARY.md)
2. [PREFACE.md](PREFACE.md)
3. [BOOK.md](BOOK.md)
4. [course/COURSE_OUTLINE.md](course/COURSE_OUTLINE.md)
5. [assignments/ASSIGNMENTS.md](assignments/ASSIGNMENTS.md)
6. [LEARNING_CHECKLIST.md](LEARNING_CHECKLIST.md)
7. [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
8. [出版與上架資料](publishing/README.md)
9. [EPUB 電子書](dist/pi-coding-agent-100h.epub)
8. [ROADMAP.md](ROADMAP.md)
11. [BACKLOG.md](BACKLOG.md)
12. [VERSION_NOTES.md](VERSION_NOTES.md)

## 教材目標

- 學會安裝、設定與日常使用 Pi Coding Agent
- 熟悉 session、context、模型/provider 與安全設定
- 能使用 Prompt Templates、Skills、Themes 客製化工作流
- 能開發 Extensions 擴充工具、指令與事件處理
- 能透過 SDK、RPC、JSON 模式整合到其他系統

## 課程模組與時數

以下是一般讀者「閱讀、跟做範例、完成基本作業」的建議時數。

| 模組 | 主題 | 時數 |
|---|---|---:|
| 01 | 基礎入門 | 6 |
| 02 | 互動模式與 Session 工作流 | 8 |
| 03 | 設定、安全與平台環境 | 6 |
| 04 | Provider、模型與本地模型 | 6 |
| 05 | Prompt Templates、Skills、Themes | 8 |
| 06 | Extensions 開發 | 12 |
| 07 | SDK、RPC 與 JSON 整合 | 10 |
| 08 | 總整專題 | 4 |
|  | **核心自學合計** | **60** |

## 資料夾說明

```text
course/         各模組教材
assignments/    作業與實作題
examples/       範例程式與示範專案
sample-project/ 全書共用練習專案
submissions/    作業繳交範本
final-project/  總整專題範本
assets/         圖片、投影片素材
notes/          備課筆記
docs/           官方文件整理與摘要
```

## 官方文件來源

本教材主要參考本機 Pi Coding Agent 官方文件：

```text
C:\Users\user\AppData\Local\pi-node\current\node_modules\@earendil-works\pi-coding-agent\README.md
C:\Users\user\AppData\Local\pi-node\current\node_modules\@earendil-works\pi-coding-agent\docs
```

## 建議單元格式

每個單元建議包含：

1. 學習目標
2. 先備知識
3. 官方文件對應
4. 核心觀念
5. 操作步驟
6. 實作任務
7. 常見問題
8. 延伸挑戰
