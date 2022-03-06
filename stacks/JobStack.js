import * as sst from "@serverless-stack/resources";

export default class JobStack extends sst.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    // Create Cron Job
    new sst.Cron(this, "Cron", {
      schedule: "rate(1 minute)",
      job: {
        function: "lambda.handler",
      },
      environment: {
        STOCKS_TABLE: process.env.STOCKS_TABLE,
      },
    });
  }
}