import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const dangerousPatterns = ["rm -rf", "sudo", "npm publish", "pnpm publish", "yarn publish"];

export default function (pi: ExtensionAPI) {
  pi.on("tool_call", async (event, ctx) => {
    if (event.toolName !== "bash") return;

    const input = event.input as { command?: unknown };
    const command = String(input.command || "");
    const matched = dangerousPatterns.find((pattern) => command.includes(pattern));

    if (!matched) return;

    const ok = await ctx.ui.confirm(
      "危險指令確認",
      `偵測到危險指令片段：${matched}\n\n是否允許執行？`
    );

    if (!ok) {
      return { block: true, reason: `已封鎖危險指令：${matched}` };
    }
  });
}
