import requests

def call_mcp(tool, args):
    response = requests.post(
        "http://localhost:8000/execute",
        json={"tool": tool, "args": args}
    )
    def call_mcp(tool, args):
        try:
            response = requests.post(
                "http://localhost:8000/execute",
                json={"tool": tool, "args": args},
                timeout=60
            )

            print("SERVER RAW:", response.text)

            return response.json()

        except Exception as e:
            return {"error": str(e)}