from .filesystem_agent import initialize_file_system_agent
from .haiku_agent import initialize_haiku_agent
from .history_tutor_agent import initialize_history_tutor_agent
from .weather_agent import initialize_weather_agent


# TODO: Expand this with information about specifically which initialization failed
# TODO: Add logging
async def initialize_agents():
    await initialize_file_system_agent()
    await initialize_haiku_agent()
    await initialize_history_tutor_agent()
    await initialize_weather_agent()
