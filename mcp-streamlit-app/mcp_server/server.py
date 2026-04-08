from fastapi import FastAPI
from mcp_server.tools import get_tools

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MCP Server Running"}

@app.post("/execute")
def execute_tool(payload: dict):
    try:
        tool_name = payload.get("tool")
        args = payload.get("args", {})

        tools = get_tools()

        if tool_name in tools:
            result = tools[tool_name](**args)
            return {"result": result}

        return {"error": "Tool not found"}

    except Exception as e:
        return {"error": str(e)}