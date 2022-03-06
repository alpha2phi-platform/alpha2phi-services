import JobStack from "./JobStack";
import StorageStack from "./StorageStack";

export default function main(app) {
  // Set default runtime for all functions
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "src",
  });

  new JobStack(app, "job");
  new StorageStack(app, "storage");
}
