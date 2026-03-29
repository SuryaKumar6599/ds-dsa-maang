import requests

def generate(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        # Debug print
        print("RAW RESPONSE:", response.text)

        data = response.json()
        return data.get("response", "No response from model")

    except Exception as e:
        return f"LLM Error: {str(e)}"