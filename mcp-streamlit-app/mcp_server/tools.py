from llm.local_llm import generate

# -------- TOOLS -------- #

def calculator(a: int, b: int):
    return a + b

def summarize(text: str):
    prompt = f"""
    Summarize the following text in 3-4 lines:

    {text}
    """
    return generate(prompt)

# -------- TOOL REGISTRY -------- #

def get_tools():
    return {
        "calculator": calculator,
        "summarize": summarize
    }