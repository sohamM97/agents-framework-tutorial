import asyncio
import os

from agent_framework import Agent

# TODO: learn more about ChatClient vs ChatCompletionClient
from agent_framework.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()


async def main():

    client = OpenAIChatCompletionClient(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        # TODO: is there also a param called azure_endpoint?
        base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )

    sm_agent = Agent(
        client=client,
        name="AgentSoham",
        instructions="You are Soham, the lead developer of AIS Team. Your job is to"
        " take requests from the user and convert them into concrete software "
        "products.",
    )

    session = sm_agent.create_session()
    greeting = await sm_agent.run(
        "Greet the user, and ask him his requirements in a friendly way.",
        session=session,
    )
    print(f"[AGENT]: {greeting}")

    req = await asyncio.to_thread(input, "[USER]: ")

    sol = await sm_agent.run(
        f"The following is the user's requirement: `{req}`. Propose him a "
        "solution in a friendly way.",
        session=session,
    )
    print(f"[AGENT]: {sol}")


if __name__ == "__main__":
    asyncio.run(main())
