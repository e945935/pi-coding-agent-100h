# Provider 設定檢查表

## 開始前

- [ ] 已安裝 Pi：`pi --version`
- [ ] 已確認 Node.js / npm 可用
- [ ] 已選擇 subscription 或 API-key provider
- [ ] 知道帳號方案、額度與費用限制
- [ ] 確認 API key 不會寫入 repo

## Subscription login

- [ ] 執行 `pi`
- [ ] 執行 `/login`
- [ ] 選擇 provider
- [ ] 完成瀏覽器或裝置驗證
- [ ] 執行 `/model`
- [ ] 選到可用模型
- [ ] 實際送出簡單 prompt

## API key

- [ ] 使用環境變數或 Pi auth file 管理 key
- [ ] `.env` 已加入 `.gitignore`
- [ ] 沒有把 key 貼到公開 issue、commit 或 log
- [ ] 執行 `/model` 確認模型
- [ ] 送出簡單 prompt 驗證

Git Bash / macOS / Linux：

```bash
export ANTHROPIC_API_KEY="你的金鑰"
```

PowerShell：

```powershell
$env:ANTHROPIC_API_KEY="你的金鑰"
```

## 模型檢查

- [ ] `/model` 可以開啟模型選擇器
- [ ] 已選擇具備工具呼叫能力的模型
- [ ] 必要時執行 `pi update --models`
- [ ] 按 Ctrl+S 儲存預設模型
- [ ] 用 `/thinking` 選擇適合任務的思考層級

## 無法使用時的排除順序

1. `pi --version`
2. 確認網路與 provider 狀態
3. 重新執行 `/login`
4. 執行 `/model` 確認可用模型
5. 檢查 API key 是否過期或額度不足
6. 換一個已知可用模型測試
7. 記錄 Pi 版本、provider、錯誤訊息，再尋求協助

> 回報問題時不要貼出完整 API key。
