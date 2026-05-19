# pip install agent-framework
# Use `az login` to authenticate with Azure CLI
import os
import asyncio
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


async def main():
    # Initialize a chat agent with Microsoft Foundry
    # the endpoint, deployment name, and api version can be set via environment variables
    # or they can be passed in directly to the FoundryChatClient constructor
    agent = Agent(
        client=FoundryChatClient(
            credential=AzureCliCredential(),
            project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
            model=os.environ["FOUNDRY_MODEL_DEPLOYMENT_NAME"],
        ),
        name="HaikuAgent",
        instructions="You are an upbeat assistant that writes beautifully.",
    )

    print(await agent.run("Write a haiku about Microsoft Agent Framework."))


if __name__ == "__main__":
    asyncio.run(main())
