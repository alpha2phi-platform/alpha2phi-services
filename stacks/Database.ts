import { StackContext, Table } from "@serverless-stack/resources";

export function Database({ stack }: StackContext) {
  // Create the Countries table
  const countriesTable = new Table(stack, process.env.COUNTRIES_TABLE!, {
    fields: {
      country: "string",
    },
    primaryIndex: { partitionKey: "country" },
  });

  // Create the Stocks table
  const stocksTable = new Table(stack, process.env.STOCKS_TABLE!, {
    fields: {
      country: "string",
      symbol: "string",
    },
    primaryIndex: { partitionKey: "country", sortKey: "symbol" },
  });

  return { countriesTable, stocksTable };
}
