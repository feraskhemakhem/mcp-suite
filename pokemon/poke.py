import httpx
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("poke")

POKEABI_BASE = "https://pokeapi.co/api/v2"

# --- Helper functions to fetch data from the PokeAPI --- #

# fetch pokemon data from the PokeAPI
async def fetch_pokemon_data(pokemon_name: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{POKEABI_BASE}/pokemon/{pokemon_name.lower()}")
            response.raise_for_status()
            if (response.status_code == 200):
                return response.json()
        except httpx.HTTPStatusError:
            pass
    return {}

# create competitive team of Pokemon
async def competitive_team_helper() -> list:
    team_info = []
    # suggest Red's team from HeartGold/SoulSilver as a competitive team
    top_pokemon = ["pikachu", "venusaur", "charizard", "blastoise", "lapras","snorlax"]
    for name in top_pokemon:
        data = await fetch_pokemon_data(name)
        if data:
            team_info.append(data.get("name").capitalize())
    return team_info

# --- MCP Tools --- #

# get information about a specific Pokemon by name
@mcp.tool()
async def get_pokemon_info(pokemon_name: str) -> str:
    """
    Get detailed information about a specific Pokemon by name.

    Args:
        pokemon_name (str): The name of the Pokemon.

    Returns:
        types.MCPResponse: A response containing the Pokemon information or an error message.
    """
    data = await fetch_pokemon_data(pokemon_name)
    if not data:
        return f"Pokemon '{pokemon_name}' not found."

    # Extract relevant information from the data
    pokemon_info = {
        "name": data.get("name").capitalize(),
        "id": data.get("id"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "types": [t["type"]["name"] for t in data.get("types", [])],
        "abilities": [a["ability"]["name"] for a in data.get("abilities", [])],
        "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data.get("stats", [])},
    }

    return json.dumps(pokemon_info, indent=4)



# create a competitive team of Pokemon based on a list of names
@mcp.tool()
async def create_competitive_team(pokemon_names: list) -> str:
    """
    Create a competitive team of Pokemon based on a list of names.

    Returns:
        types.MCPResponse: A response containing the team information or an error message.
    """
    team_info = await competitive_team_helper()
    if not team_info:
        return f"Failed to create a competitive team."

    return "Competitive Squad:\n" + "\n".join(team_info)


# --- Entry point for the MCP server --- #
if __name__ == "__main__":
    mcp.run(transport="stdio")