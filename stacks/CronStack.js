import * as sst from "@serverless-stack/resources";

export default class CronStack extends sst.Stack {
  cron;
  constructor(scope, id, props) {
    super(scope, id, props);

    const { stocksTable, countriesTable } = props;

    // Create Cron Job
    this.cron = new sst.Cron(this, "cron", {
      schedule: "rate(5 minutes)",
      job: {
        handler: "cron_stocks.handler",
        timeout: 900,
        environment: {
          STOCKS_TABLE: stocksTable.dynamodbTable.tableName,
          COUNTRIES_TABLE: countriesTable.dynamodbTable.tableName,
        },
      },
    });
    // this.cron.attachPermissions(["dynamodb:PutItem"]);
    this.cron.attachPermissions([stocksTable]);
    this.cron.attachPermissions([countriesTable]);
  }
}
