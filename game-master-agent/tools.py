from agents import function_tool

@function_tool()
def roll_dice() -> str:
    return "You rolled a 6. The monster is defeated!"
roll_dice.name = "roll_dice"

@function_tool()
def generate_event() -> str:
    return "You discover a secret passage with hidden treasures."
generate_event.name = "generate_event"
