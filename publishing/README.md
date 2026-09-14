# 出版檔案

本資料夾存放 Google Play Books 與 Kobo Writing Life 上架所需的書目資料、商店簡介與檢查表。

## 檔案

- `metadata.yaml`：書目與出版資訊
- `../assets/cover.jpg`：平台上傳用 JPG 封面
- `../assets/cover.svg`：可編輯的向量封面原稿
- `store-description.md`：商店短版、長版簡介
- `upload-checklist.md`：上架前檢查表
- `google-play-books-upload.md`：Google Play Books 操作指南

## 封面

產生 JPG 封面：

```bash
python scripts/build_cover_jpg.py
```

目前封面規格：1600 × 2560 px、RGB、JPG。

## EPUB

建置指令：

```bash
python scripts/build_epub.py
```

輸出位置：

```text
dist/pi-coding-agent-100h.epub
```

## ISBN

`metadata.yaml` 目前標示「待申請」。正式上架前，請依出版與平台需求填入 ISBN，或使用平台提供的識別機制。
