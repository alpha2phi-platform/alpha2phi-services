import { StackContext, Cron, Table, use } from "@serverless-stack/resources";
import { Database } from "./Database";

export function CronJob({ stack }: StackContext) {
  const database: {
    stocksTable: Table;
    countriesTable: Table;
    stocksInfoTable: Table;
    stocksDividendsTable: Table;
  } = use(Database);

  // Cron Job to get the countries and list of stocks
  const cron_get_stocks = new Cron(stack, "cron_get_stocks", {
    // schedule: "rate(1 minute)",
    schedule: "cron(0 8 1 * ? *)", // Run at 8:00 am (UTC+0) every 1st day of the month
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

  // Cron Job to get the stock info and dividends
  const cron_get_stocks_info = new Cron(stack, "cron_get_stocks_info", {
    // schedule: "cron(0 8 1 * ? *)", // Run at 8:00 am (UTC+0) every 1st day of the month
    schedule: "rate(1 minute)",
    job: {
      function: {
        handler: "functions/cron_get_stocks_info.handler",
        timeout: 900,
        environment: {
          COUNTRIES_TABLE: database.countriesTable.tableName,
          STOCKS_TABLE: database.stocksTable.tableName,
          STOCKS_INFO_TABLE: database.stocksInfoTable.tableName,
          STOCKS_DIVIDENDS_TABLE: database.stocksDividendsTable.tableName,
        },
        permissions: [
          database.stocksTable,
          database.countriesTable,
          database.stocksInfoTable,
          database.stocksDividendsTable,
        ],
      },
    },
  });

  return { cron_get_stocks, cron_get_stocks_info };
}
