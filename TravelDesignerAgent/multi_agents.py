from agents import Agent
from tools import set_destination, get_flights, suggest_hotels, recommend_exploration

booking_agent = Agent(
    name="BookingAgent",
    instructions="Use ONLY the provided mock data tools: get_flights and suggest_hotels to respond with flight and hotel options. Do not say you can't help.",
    tools=[get_flights, suggest_hotels],
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="Use ONLY the provided mock data tool recommend_exploration to suggest places to explore and food options.",
    tools=[recommend_exploration],
)

main_agent = Agent(
    name="TravelMainAgent",
    instructions="First, set the destination using set_destination. Then hand off to BookingAgent for flights/hotels and then ExploreAgent for local tips. Always use the tools.",
    tools=[set_destination],
    handoffs=[booking_agent, explore_agent]
)



