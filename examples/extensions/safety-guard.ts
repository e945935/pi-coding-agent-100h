import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const dangerousPatterns = [
  "rm -rf",
  "Remove-Item -Recurse -Force",
  "sudo",
  "npm publish",
  "pnpm publish",
  "yarn publish",
];

const protectedPaths = [
  ".env",
  ".env.local",
  "node_modules",
  "package-lock.json",
];

export default function (pi: ExtensionAPI) {
  pi.on("tool_call", async (event, ctx) => {
    if (event.toolName === "bash") {
      const command = String(event.input.command || "");
      const matched = dangerousPatterns.find((pattern) => command.includes(pattern));

      if (matched) {
        const ok = await ctx.ui.confirm(
          "危險指令確認",
          `偵測到危險指令片段：${matched}\n\n是否允許執行？`
        );
        if (!ok) return { block: true, reason: `已封鎖危險指令：${matched}` };
      }
    }

    if (event.toolName === "write" || event.toolName === "edit") {
      const text = JSON.stringify(event.input);
      const matched = protectedPaths.find((path) => text.includes(path));

      if (matched) {
        const ok = await ctx.ui.confirm(
          "受保護檔案確認",
          `即將修改或寫入受保護路徑：${matched}\n\n是否允許？`
        );
        if (!ok) return { block: true, reason: `已封鎖受保護路徑：${matched}` };
      }
    }
  });
}
