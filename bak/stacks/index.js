import CronStack from "./CronStack";
import DbStack from "./DbStack";

export default function main(app) {
  // Set default runtime for all functions
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "src",
    environment: {
      STAGE: app.stage,
    },
  });

  const dbStack = new DbStack(app, "db");
  new CronStack(app, "cron", {
    stocksTable: dbStack.stocksTable,
    countriesTable: dbStack.countriesTable,
  });
}
