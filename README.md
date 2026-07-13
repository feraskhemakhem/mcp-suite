# mcp-suite
An MCP suite with servers and custom tools.

This suite's weather app follows the guide shared with on the official MCP website. This link is here: https://modelcontextprotocol.io/docs/develop/build-server.
The Pokemon app uses PokeAPI. The link the PokeAPI is here: https://pokeapi.co/.

## Setup

### Prerequisite Software

This project uses `uv` for setup. If you don't have `uv` installed, you can follow the first steps of [this link](https://docs.astral.sh/uv/). This project also uses [Python 3.14](https://www.python.org/downloads/release/python-3146/), so download that if you don't have it.

You'll also need some kind of MCP Client to interface with the server. I will provide instructions for using the [Claude for Desktop](https://claude.com/download) application as the client.

### Running the Servers

There are multiple servers that exist in this project. Each project follows the same steps to get running:

1. Open a terminal in the respective folder of the server you wish to run (navigate the terminal `mcp-suite/pokemon/` or `mcp-suite/weather`).
2. Activate the environment by running `.venv/Scripts/activate`.
3. Install the server to your MCP client. In the case of Claude Desktop, running `mcp install poke.py`/`mcp install weather.py` will update the config file, or you can update the config file manually to run the server.
4. Launch or relaunch your MCP client.

At this point, it should be ready to use!

## Utilizing the MCP Server

## Weather Server

To access the weather server, prompt your MCP client for weather alerts or forcasts for a given location.

## Pokemon Server

For the pokemon server, prompt your MCP client for information about specific pokemon, or for competitive viable teams. PokeAPI does not have the capability to build competitively viable teams, so the MCP server will default to the Red's competitive pokemon team from HeartGold/SoulSilver.