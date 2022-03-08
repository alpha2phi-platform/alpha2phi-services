import * as sst from "@serverless-stack/resources";

export default class JobStack extends sst.Stack {
  cron;
  constructor(scope, id, props) {
    super(scope, id, props);

    const { table } = props;

    // Create Cron Job
    this.cron = new sst.Cron(this, "Cron", {
      schedule: "rate(1 minute)",
      job: {
        handler: "lambda.handler",
        environment: {
          STOCKS_TABLE: process.env.STOCKS_TABLE,
        },
      },
    });
    this.cron.jobFunction.attachPermissions([table]);
    this.cron.jobFunction.attachPermissions(["dynamodb"]);
  }
}
