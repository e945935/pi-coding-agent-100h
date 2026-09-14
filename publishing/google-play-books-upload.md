# Google Play Books 上架操作指南

## 帳號

請使用出版者自己的 Google 帳號登入：

```text
t945935@gmail.com
```

> 請勿將密碼、雙重驗證碼或付款資料提供給任何人。建議由帳號持有人親自登入。

## 上傳檔案

EPUB：

```text
dist/pi-coding-agent-100h.epub
```

書目資料：

```text
publishing/metadata.yaml
publishing/store-description.md
```

## 操作步驟

1. 開啟 Google Play Books Partner Center：
   <https://play.google.com/books/publish/>
2. 使用 `t945935@gmail.com` 登入。
3. 建立新書或新增書籍。
4. 填入：
   - 書名：Pi Coding Agent 100 小時實戰教材
   - 副標題：從入門、工作流、客製化到 SDK 與系統整合
   - 語言：繁體中文（台灣）／`zh-TW`
   - 作者：Pi Coding Agent 100 小時教材編輯團隊
   - 出版者：Pi Coding Agent 100 小時教材編輯團隊
5. 上傳 `dist/pi-coding-agent-100h.epub`。
6. 上傳封面：
   - 原始封面：`assets/cover.svg`
   - 若平台不接受 SVG，請將封面另存為高解析度 JPG 或 PNG 後上傳。
7. 貼上 `publishing/store-description.md` 的長版簡介。
8. 設定分類、關鍵字、銷售地區、價格與預覽比例。
9. 檢查預覽器中的：
   - 封面
   - 目錄
   - 表格細框線
   - 程式碼區塊
   - 超連結
   - 繁體中文字元
10. 儲存並送出審核。

## 上架前確認

- [ ] ISBN 已填入，或已選擇平台識別碼流程
- [ ] 沒有 API key、token 或私人路徑
- [ ] EPUB 是最新版本
- [ ] 書名與封面一致
- [ ] 作者、語言與出版者資料一致
- [ ] 價格與銷售地區已確認
- [ ] 預覽器沒有排版錯誤

> Google Play Books 的介面、資格與檔案規格可能變更，實際操作時請以 Partner Center 畫面與官方說明為準。
