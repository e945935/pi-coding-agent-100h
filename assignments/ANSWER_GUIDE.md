# 作業參考方向

這份文件不是唯一答案，而是協助學員自我檢查。

## 作業 1：專案工作流

合格成果至少應包含：

- 專案用途與主要目錄
- 可實際執行的 test / lint / build 指令
- 放在專案根目錄的 `AGENTS.md`
- 至少一段實際 Pi 操作紀錄
- 修改前後的 Git 狀態

## 作業 2：Session 分支比較

合格成果至少應包含：

- 同一任務的兩種方案
- 使用 `/fork` 或 `/clone` 的紀錄
- `/tree` 查看分支的紀錄
- 每個方案的測試結果
- 依維護性、風險、複雜度做選擇，而不是只看程式碼長度

## 作業 3：Prompt Template 或 Skill

檢查：

- Prompt template 是否放在可發現的位置
- Skill 是否有正確 frontmatter
- `description` 是否清楚說明用途
- 是否有實際用 `/name` 或 `/skill:name` 叫用
- 輸出格式是否固定且可驗收

## 作業 4：安全防護 Extension

檢查：

- extension 是否能載入
- 是否至少攔截一種危險操作
- 使用者拒絕後是否真的 block
- 是否用測試資料夾，不碰重要資料
- README 是否說明 extension 權限風險

## 作業 5：SDK 小型整合

檢查：

- 是否能建立 session
- 是否能送出 prompt
- 是否能處理 streaming event
- 是否在結束時 `dispose()`
- provider 不可用時是否有清楚錯誤說明
