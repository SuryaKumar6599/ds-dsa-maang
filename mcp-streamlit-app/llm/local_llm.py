import requests

def generate(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",   # 👈 use mistral
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_predict": 150
                }
            },
            timeout=60
        )

        data = response.json()
        return data.get("response", "No response from model")

    except Exception as e:
        return f"LLM Error: {str(e)}"