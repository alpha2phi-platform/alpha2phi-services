import * as sst from "@serverless-stack/resources";

// TODO - change to functional component

export default class DbStack extends sst.Stack {
  // Public reference to the table
  countriesTable;
  stocksTable;

  constructor(scope, id, props) {
    super(scope, id, props);

    // Create the Countries table
    this.countriesTable = new sst.Table(this, process.env.COUNTRIES_TABLE, {
      fields: {
        country: sst.TableFieldType.STRING,
      },
      primaryIndex: { partitionKey: "country" },
    });

    // Create the Stocks table
    this.stocksTable = new sst.Table(this, process.env.STOCKS_TABLE, {
      fields: {
        country: sst.TableFieldType.STRING,
        symbol: sst.TableFieldType.STRING,
      },
      primaryIndex: { partitionKey: "country", sortKey: "symbol" },
    });
  }
}
