import JobStack from "./JobStack";
import StorageStack from "./StorageStack";

export default function main(app) {
  // Set default runtime for all functions
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "src",
    // environment: {
    //   STOCKS_TABLE: process.env.STOCKS_TABLE,
    // },
  });

  const storageStack = new StorageStack(app, "storage");
  new JobStack(app, "job", {
    stocksTable: storageStack.stocksTable,
    countriesTable: storageStack.countriesTable,
  });
}
