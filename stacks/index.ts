import { MyStack } from "./MyStack";
import { App } from "@serverless-stack/resources";

export default function (app: App) {
  app.setDefaultFunctionProps({
    runtime: "python3.9",
    srcPath: "backend",
    environment: {
      STAGE: app.stage,
    },
  });
  app.stack(MyStack);
}
