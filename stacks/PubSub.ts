import { StackContext, Topic } from "@serverless-stack/resources";

export function PubSub({ stack }: StackContext) {
  // Create Topic
  const topic = new Topic(stack, "pubsub-analytics", {
    subscribers: {
      analytics: "analysis.main",
    },
  });

  return topic;
}
