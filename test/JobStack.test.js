import { Template } from "aws-cdk-lib/assertions";
import * as sst from "@serverless-stack/resources";
import JobStack from "../stacks/JobStack";

test("Test Job Stack", () => {
  const app = new sst.App();
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "src",
  });
  // WHEN
  const stack = new JobStack(app, "job");
  // THEN
  const template = Template.fromStack(stack);
  template.resourceCountIs("AWS::Lambda::Function", 1);
});
