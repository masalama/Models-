import subprocess

def generate_documentation(model_name, prompt, code_snippet):
    """
    Generate documentation by running a locally installed model using the Ollama CLI.

    Args:
        model_name (str): The model identifier as shown in `ollama list` (e.g., "llama2:7b" or "llama3.2:latest").
        prompt (str): The prompt containing instructions for documentation generation.
        code_snippet (str): The code snippet that needs documentation.

    Returns:
        str: The generated documentation output, or an error message.
    """
    full_prompt = f"{prompt}\n\nCode:\n{code_snippet}"
    try:
        # Invoke the Ollama CLI with the model name. Pass the prompt via stdin.
        result = subprocess.run(
            ["ollama", "run", model_name],
            input=full_prompt,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # If there is an error, return the stderr (or the exception message).
        error_msg = e.stderr.strip() if e.stderr else str(e)
        return f"Error with model {model_name}: {error_msg}"
