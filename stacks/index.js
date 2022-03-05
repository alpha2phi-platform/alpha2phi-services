import JobStack from "./JobStack";

export default function main(app) {
  // Set default runtime for all functions
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "src",
  });

  new JobStack(app, "job");

  // Add more stacks
}
