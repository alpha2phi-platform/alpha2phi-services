import MyStack from "./MyStack";

export default function main(app) {
  // Set default runtime for all functions
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "src",
  });

  new MyStack(app, "my-stack");

  // Add more stacks
}