import { existsSync } from "node:fs";

if (!existsSync("src/index.js")) {
  console.error("build failed: src/index.js not found");
  process.exit(1);
}

console.log("build passed");
