export function add(a, b) {
  return a + b;
}

export function isEmail(value) {
  if (typeof value !== "string") return false;
  return value.includes("@") && value.includes(".");
}
