import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";

const root = resolve("../..");
const targetDir = resolve(root, "sample-project/.pi/extensions");
mkdirSync(targetDir, { recursive: true });

for (const name of ["hello.ts", "safety-guard.ts"]) {
  copyFileSync(resolve("src", name), resolve(targetDir, name));
  console.log(`copied ${name} to ${targetDir}`);
}
