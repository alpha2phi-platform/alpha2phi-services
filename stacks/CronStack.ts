import { StackContext, Cron, use } from "@serverless-stack/resources";
import { DbStack } from "./DbStack";

export function CronStack({ stack }: StackContext) {
  const db = use(DbStack);

  // Create Cron Job
  const cron = new Cron(stack, "cron", {
    schedule: "rate(5 minutes)",
    job: {
      function: {
        handler: "functions/cron.handler",
        timeout: 900,
        environment: {
          STOCKS_TABLE: db.stocksTable.tableName,
          COUNTRIES_TABLE: db.countriesTable.tableName,
        },
        permissions: [db.stocksTable, db.countriesTable],
      },
    },
  });

  return cron;
}
