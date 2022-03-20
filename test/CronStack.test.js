import { Template } from "aws-cdk-lib/assertions";
import * as sst from "@serverless-stack/resources";
import CronStack from "../stacks/CronStack";

test("Test Cron Stack", () => {
  const app = new sst.App();
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "src",
  });
  // WHEN
  const cronStack = new CronStack(app, "cron");
  // THEN
  const template = Template.fromStack(cronStack);
  template.resourceCountIs("AWS::Lambda::Function", 1);
});
