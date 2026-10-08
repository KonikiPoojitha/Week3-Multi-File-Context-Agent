from context_builder import build_context
from llm import ask_llm


def analyze_task(project_folder, task):
    context = build_context(project_folder)

    prompt = f"""
You are an AI coding agent.

You are working with a small Python project.

PROJECT FILES:
{context}

USER TASK:
{task}

Analyze the project carefully.

Identify:
1. Which files need to be changed.
2. What change is required in each file.
3. Why each file needs to be changed.

Return your answer in this format:

FILES_TO_CHANGE:
- filename1.py
- filename2.py

CHANGES:
- filename1.py: description
- filename2.py: description

Do not modify files yet.
"""

    return ask_llm(prompt)


if __name__ == "__main__":
    project_folder = "."

    task = (
        "Add input validation to the divide function so it raises "
        "ValueError when dividing by zero, and update the test file "
        "to test this behavior."
    )

    result = analyze_task(project_folder, task)

    print("\n===== AGENT ANALYSIS =====\n")
    print(result)
