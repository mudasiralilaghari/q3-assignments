
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from multi_agents import career_agent, job_agent, skills_agent, main_agent

# Load environment variables
load_dotenv()

# ✅ FIXED: Correct spelling of the environment variable
gemini_api_key = os.getenv("GOOGLE_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# ✅ Async client for Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ✅ Gemini 2.0 Flash model setup
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# ✅ RunConfig setup
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# ✅ Run your main agent
result = Runner.run_sync(main_agent, input="I want to become a web developer.", run_config=config)

# ✅ Correct key is `final_output`
print(result.final_output)
