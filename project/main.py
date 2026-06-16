import asyncio
import os

from agent_framework import Agent, AgentSession

# TODO: learn more about ChatClient vs ChatCompletionClient
from agent_framework.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()


async def run_agent(agent: Agent, prompt: str, session: AgentSession):
    response = await agent.run(prompt, session=session, stream=True)
    print("\n[AGENT]: ", end="", flush=True)
    async for chunk in response:
        if chunk.text:
            print(chunk.text, end="", flush=True)
    print()


async def take_input_from_user() -> str:
    return await asyncio.to_thread(input, "\n[USER]: ")


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
        instructions="You are Soham, the lead developer of AIS Team. Your job "
        "is to take requests from the user and convert them into concrete "
        "software products. The requests can be features, bugfixes, "
        "deployments, implementations or anything technical, really.",
    )

    session = sm_agent.create_session()

    await run_agent(
        agent=sm_agent,
        prompt="Greet the user, and ask him his requirements in a friendly way.",
        session=session,
    )

    req = await take_input_from_user()

    await run_agent(
        agent=sm_agent,
        prompt=f"The following is the user's requirement: `{req}`. Propose him"
        " a solution in a friendly way.",
        session=session,
    )


if __name__ == "__main__":
    asyncio.run(main())
