import { StackContext, Cron } from "@serverless-stack/resources";

export function CronStack({ stack }: StackContext) {
  new Api(stack, "api", {
    routes: {
      "GET /": "functions/lambda.handler",
    },
  });
}
