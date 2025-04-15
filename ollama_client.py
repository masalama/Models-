

## `ollama_client.py`


import requests

# Change this if Ollama is running on a different port or host
OLLAMA_API_URL = "http://localhost:11434/api/v1/generate"


def generate_documentation(model_name, prompt, code_snippet, temperature=0.5):
    """
    Generate documentation for a code snippet using a specified model via Ollama.

    Args:
        model_name (str): Name or identifier of the model (e.g., "llama2:7b").
        prompt (str): The user instructions for documentation generation.
        code_snippet (str): The code snippet to be documented.
        temperature (float): LLM "creativity" parameter (0.0 - 1.0). Defaults to 0.5.

    Returns:
        str: The text response from the model, or an error message.
    """
    full_prompt = f"{prompt}\n\nCode:\n{code_snippet}"
    payload = {
        "model": model_name,
        "prompt": full_prompt,
        "temperature": temperature
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.RequestException as error:
        return f"Error from model {model_name}: {error}"
