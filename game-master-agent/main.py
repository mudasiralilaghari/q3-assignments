import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from multi_agents import main_agent

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

result = Runner.run_sync(
    main_agent,
    input="I want to open the treasure chest now.",
    run_config=config
)

print(result.final_output)
