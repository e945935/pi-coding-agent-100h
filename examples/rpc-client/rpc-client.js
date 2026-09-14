import { spawn } from "node:child_process";
import { createInterface } from "node:readline";

const prompt = process.argv.slice(2).join(" ") || "請用一句話摘要目前專案。";
const agent = spawn("pi", ["--mode", "rpc"], {
  stdio: ["pipe", "pipe", "inherit"],
});

const rl = createInterface({ input: agent.stdout });
let finished = false;

rl.on("line", (line) => {
  if (!line.trim()) return;

  try {
    const event = JSON.parse(line);
    console.log(JSON.stringify(event));

    if (event.type === "agent_end") {
      finished = true;
      agent.stdin.end();
      agent.kill();
    }
  } catch {
    console.log(line);
  }
});

agent.on("exit", (code) => {
  if (!finished && code !== 0) {
    console.error(`pi rpc exited with code ${code}`);
    process.exit(code ?? 1);
  }
});

agent.stdin.write(JSON.stringify({
  id: "req-1",
  type: "prompt",
  message: prompt,
}) + "\n");
