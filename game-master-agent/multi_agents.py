from agents import Agent
from tools import roll_dice, generate_event

# Narrator Agent
narrator_agent = Agent(
    name="NarratorAgent",
    instructions="Narrate the story and switch to MonsterAgent for combat.",
    tools=[generate_event],
    handoffs=[]
)

# Monster Agent
monster_agent = Agent(
    name="MonsterAgent",
    instructions="Fight phase. Use roll_dice. After combat, switch to ItemAgent.",
    tools=[roll_dice],
    handoffs=[]
)

# Item Agent
item_agent = Agent(
    name="ItemAgent",
    instructions="Give loot and rewards. Then switch back to NarratorAgent.",
    tools=[generate_event],
    handoffs=[]
)

# Connect handoffs properly
narrator_agent.handoffs = [monster_agent]
monster_agent.handoffs = [item_agent]
item_agent.handoffs = [narrator_agent]

# Main Game Master Agent
main_agent = Agent(
    name="GameMasterAgent",
    instructions="Start the adventure game with NarratorAgent.",
    tools=[],
    handoffs=[narrator_agent]
)
