from .filesystem_agent import initialize_file_system_agent
from .haiku_agent import initialize_haiku_agent
from .history_tutor_agent import initialize_history_tutor_agent
from .orchestration_agent import initialize_orchestration_agent


# TODO: Expand this with information about specifically which initialization failed
# TODO: Add logging
async def initialize_agents():
    # Initialize the File System Agent first, as it depends on the server.
    await initialize_file_system_agent()
    # Initialize the remaining agents.
    await initialize_haiku_agent()
    await initialize_history_tutor_agent()

    # Finally, initialize the Orchestration Agent that depends on all others.
