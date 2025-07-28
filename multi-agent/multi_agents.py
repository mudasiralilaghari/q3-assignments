# multi_agents.py
from agents import Agent
from tools import get_career_roadmap


career_agent= Agent(
    name="CareerAgent",
    instructions="You are a career advisor. Provide career roadmaps based on the given career name.",
    tools=[get_career_roadmap]
)



job_agent= Agent(
    name="JobAgent",
    instructions="You are a job advisor. Provide job search strategies and tips.",
)


skills_agent= Agent(
    name="SkillsAgent",
    instructions="You are a skills advisor. Provide skill development strategies based on the given career name."
)


main_agent = Agent(
    name="MainAgent",
    instructions="You are the main agent coordinating career advice. Use CareerAgent, JobAgent, and SkillsAgent to provide comprehensive career guidance.",
    handoffs=[career_agent,job_agent,skills_agent]
)