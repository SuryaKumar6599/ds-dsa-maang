mcp-streamlit-app/
│
├── app.py                 # Streamlit UI
├── mcp_server/
│   ├── server.py         # MCP server (FastAPI or simple handler)
│   ├── tools.py          # Tools exposed via MCP
│   ├── resources.py      # Data/context providers
│
├── llm/
│   ├── client.py         # OpenAI / local LLM wrapper
│
├── utils/
│   ├── logger.py
│
├── requirements.txt
└── README.md