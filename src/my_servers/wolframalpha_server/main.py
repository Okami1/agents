import asyncio
import logging
import os

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("wolfram-alpha-mcp")

# API Key from environment variables
APP_ID = os.getenv("WOLFRAM_ALPHA_APP_ID")
if not APP_ID:
    logger.warning(
        "Wolfram Alpha App ID not found in environment variables. Please set WOLFRAM_ALPHA_APP_ID in your .env file."
    )

BASE_URL = "http://api.wolframalpha.com/v1/result"


@mcp.tool("get_answer")
async def get_answer(query: str) -> str:
    """Get an answer from Wolfram Alpha.

    Args:
        query (str): The query to ask Wolfram Alpha.

    Returns:
        String with the answer or an error message.
    """
    try:
        if not APP_ID:
            return {
                "Wolfram Alpha App ID not configured. Please set WOLFRAM_ALPHA_APP_ID in your .env file."
            }

        # Get the answer from Wolfram Alpha Short Answer API
        params = {"appid": APP_ID, "i": query}
        logger.info(params)
        response = requests.get(BASE_URL, params=params)

        # Check for API errors
        if response.status_code == 501:
            return {
                "error": "API cannot answer the request because it is unintelligible or otherwise unable to be answered."
            }
        if response.status_code >= 400 and response.status_code < 500:
            return {"error": f"API error: {response.status_code} - {response.text}"}

        return response.text
    except Exception as e:
        logger.error(f"Error answering query '{query}': {str(e)}")
        return f"Failed to answer query '{query}': {str(e)}"


if __name__ == "__main__":
    # Print API key status (without revealing the key)
    if APP_ID:
        logger.info("Wolfram Alpha App ID loaded successfully")
    else:
        logger.warning(
            "Wolfram Alpha App ID not found. Please set WOLFRAM_ALPHA_APP_ID in your .env file."
        )

    # Run the MCP server
    mcp.run()
