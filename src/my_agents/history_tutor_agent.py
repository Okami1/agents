from agents import Agent

HISTORY_TUTOR_AGENT = None


async def initialize_history_tutor_agent():
    print("  History Tutor Agent")

    global HISTORY_TUTOR_AGENT

    HISTORY_TUTOR_AGENT = Agent(
        name="History Tutor Agent",
        handoff_description="Answers historical questions.",
        instructions="Provide detailed historical insights for the question provided.",
    )
