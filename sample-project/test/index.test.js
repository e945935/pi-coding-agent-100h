import test from "node:test";
import assert from "node:assert/strict";
import { add, isEmail } from "../src/index.js";

test("add returns sum", () => {
  assert.equal(add(1, 2), 3);
});

test("isEmail accepts simple email", () => {
  assert.equal(isEmail("user@example.com"), true);
});

test("isEmail rejects non email text", () => {
  assert.equal(isEmail("hello"), false);
});
