import os
from datetime import datetime
import glob
from test_models import test_models, build_documentation_prompt
from evaluation import get_evaluation_criteria


def main():
    input_dir = "input_code"
    # Ensure the "results" directory exists.
    os.makedirs("results", exist_ok=True)

    # List of locally installed models to test.
    models = ["codegemma", "qwen2.5-coder", "codeqwen"]

    # Build the documentation prompt.
    prompt = build_documentation_prompt()

    # Find all Python files in the input directory.
    python_files = glob.glob(os.path.join(input_dir, "*.py"))

    if not python_files:
        print("No Python files found in the input_code directory.")
        return

    output_lines = []
    output_lines.append("# Documentation Results")
    output_lines.append(f"**Models Tested:** {', '.join(models)}")
    output_lines.append("\n---\n")

    # Process each Python file found.
    for file_path in python_files:
        file_name = os.path.basename(file_path)

        # Read the content (for processing; input code will not be output)
        with open(file_path, "r", encoding="utf-8") as f:
            code_snippet = f.read()

        output_lines.append(f"## Input File: {file_name}")
        output_lines.append("\n---\n")

        # Generate documentation outputs for the code snippet.
        results = test_models(models, code_snippet, prompt)
        for model, doc in results.items():
            output_lines.append(f"### Documentation Output from {model}")
            output_lines.append("")
            output_lines.append(doc)
            output_lines.append("\n---\n")

    # Append evaluation criteria to the output.
    output_lines.append("## Evaluation Criteria for Comparing Outputs")
    output_lines.append("")
    output_lines.append(get_evaluation_criteria())

    # Create a timestamped filename with a Markdown (.md) extension.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = os.path.join("results", f"results_{timestamp}.md")

    # Write the output to the Markdown file.
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    # Minimal terminal output.
    print(f"Documentation generated and saved in: {output_filename}")


if __name__ == "__main__":
    main()
