from pathlib import Path


def read_python_files(project_folder):
    project_path = Path(project_folder)

    files = {}

    for file_path in project_path.glob("*.py"):
        if file_path.name == "context_builder.py":
            continue

        try:
            files[file_path.name] = file_path.read_text()
        except OSError as error:
            files[file_path.name] = f"Could not read file: {error}"

    return files


def build_context(project_folder):
    files = read_python_files(project_folder)

    context_parts = []

    for filename, content in files.items():
        context_parts.append(
            f"===== {filename} =====\n{content}"
        )

    return "\n\n".join(context_parts)


if __name__ == "__main__":
    context = build_context(".")
    print(context)
