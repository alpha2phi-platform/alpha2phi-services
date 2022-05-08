import { App } from "@serverless-stack/resources";
import { RemovalPolicy } from "aws-cdk-lib";
import { DbStack } from "./DbStack";
import { CronStack } from "./CronStack";

export default function (app: App) {
  app.setDefaultFunctionProps({
    runtime: "python3.9",
    srcPath: "backend",
    environment: {
      STAGE: app.stage,
    },
  });

  if (app.local) app.setDefaultRemovalPolicy(RemovalPolicy.DESTROY);

  app.stack(DbStack).stack(CronStack);
}
