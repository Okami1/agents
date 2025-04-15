from agents import Agent


async def initialize_history_tutor_agent():
    print("  Initializing HISTORY_TUTOR_AGENT")

    return Agent(
        name="History Tutor Agent",
        handoff_description="Answers historical questions.",
        instructions="Provide detailed historical insights for the question provided.",
    )
