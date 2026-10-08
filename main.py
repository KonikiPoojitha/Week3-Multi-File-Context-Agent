from pathlib import Path

from context_builder import build_context
from llm import ask_llm
from editor import apply_changes
from executor import run_tests


PROJECT_FOLDER = Path(__file__).parent


def analyze_task(task):
    context = build_context(PROJECT_FOLDER)

    prompt = f"""
You are an AI coding agent.

PROJECT CONTEXT:
{context}

USER TASK:
{task}

Determine which files must be changed.

Return:
FILES_TO_CHANGE:
- filename.py

CHANGES:
- filename.py: exact change needed

Do not modify files.
"""

    return ask_llm(prompt)


def run_agent(task):
    print("\n===== USER TASK =====")
    print(task)

    print("\n===== PROJECT CONTEXT =====")
    context = build_context(PROJECT_FOLDER)
    print(context)

    print("\n===== LLM ANALYSIS =====")
    analysis = analyze_task(task)
    print(analysis)

    print("\n===== APPLYING CHANGES =====")
    backups = apply_changes(PROJECT_FOLDER)

    print("Backups created:")
    for name, path in backups.items():
        print(f"{name}: {path}")

    print("\n===== RUNNING TESTS =====")
    result = run_tests(PROJECT_FOLDER)

    print(result["stdout"])

    if result["stderr"]:
        print(result["stderr"])

    print("\n===== FINAL STATUS =====")

    if result["success"]:
        print("SUCCESS: All tests passed.")
    else:
        print("FAILED: Some tests failed.")

    return result["success"]


if __name__ == "__main__":
    task = (
        "Add input validation to the divide function so that "
        "division by zero raises ValueError, and update the "
        "test file to test this behavior."
    )

    run_agent(task)
