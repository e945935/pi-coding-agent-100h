import { readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

function walk(dir) {
  const result = [];
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    const stat = statSync(path);
    if (stat.isDirectory()) result.push(...walk(path));
    else if (path.endsWith(".js")) result.push(path);
  }
  return result;
}

const files = [...walk("src"), ...walk("test")];
let failed = false;

for (const file of files) {
  const content = readFileSync(file, "utf8");
  if (content.includes("console.log")) {
    console.error(`lint error: console.log is not allowed in ${file}`);
    failed = true;
  }
}

if (failed) process.exit(1);
console.log("lint passed");
