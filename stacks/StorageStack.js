import * as sst from "@serverless-stack/resources";

export default class StorageStack extends sst.Stack {
  // Public reference to the table
  table;

  constructor(scope, id, props) {
    super(scope, id, props);

    // Create the Stocks table
    this.table = new sst.Table(this, "Stocks", {
      fields: {
        country: sst.TableFieldType.STRING,
        symbol: sst.TableFieldType.STRING,
      },
      primaryIndex: { partitionKey: "country", sortKey: "symbol" },
    });

    // TODO - Create Countries table
  }
}
