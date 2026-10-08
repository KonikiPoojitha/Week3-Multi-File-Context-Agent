from pathlib import Path
from datetime import datetime
import shutil


def backup_file(file_path):
    path = Path(file_path)

    if not path.exists():
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = path.with_name(
        f"{path.stem}_backup_{timestamp}{path.suffix}"
    )

    shutil.copy2(path, backup_path)

    return backup_path


def update_divide_function(file_path):
    path = Path(file_path)

    original = path.read_text()

    old_code = """def divide(a, b):
    return a / b
"""

    new_code = """def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
"""

    if old_code not in original:
        raise ValueError(
            "Expected divide function was not found in calculator.py"
        )

    backup_path = backup_file(path)

    updated = original.replace(old_code, new_code)

    path.write_text(updated)

    return backup_path


def update_test_file(file_path):
    path = Path(file_path)

    original = path.read_text()

    if "def test_divide_by_zero():" in original:
        return None

    backup_path = backup_file(path)

    new_test = """

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False
    except ValueError:
        assert True
"""

    path.write_text(original.rstrip() + new_test + "\n")

    return backup_path


def apply_changes(project_folder):
    project_path = Path(project_folder)

    calculator = project_path / "calculator.py"
    test_calculator = project_path / "test_calculator.py"

    calculator_backup = update_divide_function(calculator)
    test_backup = update_test_file(test_calculator)

    return {
        "calculator_backup": str(calculator_backup),
        "test_backup": str(test_backup),
    }


if __name__ == "__main__":
    result = apply_changes(".")
    print("Changes applied successfully.")
    print(result)
