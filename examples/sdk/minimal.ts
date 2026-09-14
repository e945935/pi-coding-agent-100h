import { createAgentSession, ModelRuntime, SessionManager } from "@earendil-works/pi-coding-agent";

async function main() {
  const prompt = process.argv.slice(2).join(" ") || "請摘要目前資料夾中的專案。";

  const modelRuntime = await ModelRuntime.create();
  const { session } = await createAgentSession({
    sessionManager: SessionManager.inMemory(),
    modelRuntime,
  });

  session.subscribe((event) => {
    if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
      process.stdout.write(event.assistantMessageEvent.delta);
    }
  });

  try {
    await session.prompt(prompt);
    process.stdout.write("\n");
  } finally {
    session.dispose();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
