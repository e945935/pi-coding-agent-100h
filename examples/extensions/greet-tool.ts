import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";

export default function (pi: ExtensionAPI) {
  pi.registerTool({
    name: "greet",
    label: "Greet",
    description: "用指定名字產生問候訊息",
    parameters: Type.Object({
      name: Type.String({ description: "要問候的名字" }),
    }),
    async execute(_toolCallId, params) {
      return {
        content: [{ type: "text", text: `你好，${params.name}！` }],
        details: {},
      };
    },
  });
}
