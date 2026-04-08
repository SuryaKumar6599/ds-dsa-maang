from llm.local_llm import generate

# -------- TOOL 1: Calculator (deterministic) -------- #
def calculator(a: int, b: int):
    return a + b

# -------- TOOL 2: Summarization (LLM) -------- #
def summarize(text: str):
    prompt = f"""
You are a precise assistant.

Summarize the following text in 3 bullet points:

{text}

Summary:
"""
    return generate(prompt)

# -------- TOOL REGISTRY -------- #
def get_tools():
    return {
        "calculator": calculator,
        "summarize": summarize
    }