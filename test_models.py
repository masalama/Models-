from local_inference import generate_documentation

def test_models(model_list, code_snippet, prompt):
    """
    Generate documentation for a given code snippet using multiple local models.

    Args:
        model_list (list of str): The list of model identifiers (e.g., ["llama2:7b", "llama3.2:latest"]).
        code_snippet (str): The code snippet for which documentation is generated.
        prompt (str): The prompt with instructions for generating the documentation.

    Returns:
        dict: A dictionary mapping each model to its generated documentation output.
    """
    results = {}
    for model in model_list:
        output = generate_documentation(model, prompt, code_snippet)
        results[model] = output
    return results

def build_documentation_prompt():
    """
    Returns an improved prompt that guides the model to generate comprehensive, well-structured Markdown
    documentation for the provided Python code. The prompt ensures that every function in the code is
    documented with details on purpose, parameters, return values, edge cases, and any additional considerations.

    Returns:
        str: The detailed documentation prompt.
    """
    return (
        "Your task is to generate detailed documentation for a Python code snippet. Please adhere to the following guidelines:\n\n"
        "1. **Overview:** Provide a high-level explanation of what the entire code does and its overall purpose. Specify the intended audience (e.g., developers, technical managers).\n\n"
        "2. **Function Identification:** Identify every function present in the code snippet. For each function, document the following:\n"
        "   - A brief summary of its purpose and functionality.\n"
        "   - A detailed breakdown of its input parameters, including types, expected values, and constraints.\n"
        "   - A clear explanation of its return value(s), including type and meaning.\n"
        "   - Any potential edge cases, error conditions, or exceptions that could occur.\n\n"
        "3. **Additional Considerations:** If applicable, include information on performance or security implications related to the functions.\n\n"
        "4. **Formatting and Style:** Use Markdown formatting with clear headers such as:\n"
        "   - `## Overview`\n"
        "   - `## Function Details`\n"
        "   - `### Parameters`\n"
        "   - `### Return Values`\n"
        "   - `### Edge Cases`\n\n"
        "5. **Usage Examples (Optional):** Include usage examples or common use cases that help clarify how each function should be used.\n\n"
        "6. **Exclusivity:** Do NOT include the original source code in your documentation output.\n\n"
        "Ensure that every function in the provided code snippet is documented. The final documentation should be clear, concise, and technically accurate."
    )
