import { StackContext, Cron, Table, use } from "@serverless-stack/resources";
import { Database } from "./Database";

export function CronJob({ stack }: StackContext) {
  const database: { stocksTable: Table; countriesTable: Table } = use(Database);

  // Create Cron Job
  const cron_get_stocks = new Cron(stack, "cron_get_stocks", {
    schedule: "rate(1 minutes)",
    job: {
      function: {
        handler: "functions/cron_get_stocks.handler",
        timeout: 900,
        environment: {
          COUNTRIES_TABLE: database.countriesTable.tableName,
          STOCKS_TABLE: database.stocksTable.tableName,
        },
        permissions: [database.stocksTable, database.countriesTable],
      },
    },
  });

  return cron_get_stocks;
}
