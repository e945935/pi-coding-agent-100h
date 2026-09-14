# Shell 指令對照表

本教材主要在 Windows 環境撰寫，但指令會盡量同時提供 Git Bash / macOS / Linux / PowerShell 寫法。

## 切換資料夾

| 情境 | 指令 |
|---|---|
| Git Bash | `cd /c/Users/user/pi-coding-agent-100h/sample-project` |
| PowerShell | `cd C:\Users\user\pi-coding-agent-100h\sample-project` |
| macOS / Linux | `cd ~/pi-coding-agent-100h/sample-project` |

## 設定 API Key，臨時有效

| Shell | 指令 |
|---|---|
| Git Bash / bash / zsh | `export ANTHROPIC_API_KEY="sk-ant-..."` |
| PowerShell | `$env:ANTHROPIC_API_KEY="sk-ant-..."` |
| cmd.exe | `set ANTHROPIC_API_KEY=sk-ant-...` |

> 注意：不要把 API key 寫進 repo，也不要提交到 Git。

## Alias / 快捷指令

### Git Bash / bash / zsh

```bash
alias pic='pi -c'
alias pir='pi -r'
```

若要永久生效，加入 `~/.bashrc` 或 `~/.zshrc`。

### PowerShell

PowerShell 的 `Set-Alias` 不適合帶參數，建議使用 function：

```powershell
function pic { pi -c }
function pir { pi -r }
```

若要永久生效，可加入 PowerShell profile：

```powershell
notepad $PROFILE
```

## Git 回復變更

| 目的 | 指令 |
|---|---|
| 查看變更 | `git diff` |
| 查看狀態 | `git status` |
| 回復單一檔案，新版建議 | `git restore <file>` |
| 回復單一檔案，舊版寫法 | `git checkout -- <file>` |
| 回復所有未提交變更，危險 | `git restore .` |

## Sample project 常用指令

```bash
npm test
npm run lint
npm run build
```
