import subprocess
import sys


def run_tests(project_folder):
    command = [
        sys.executable,
        "-m",
        "pytest",
        "-q"
    ]

    result = subprocess.run(
        command,
        cwd=project_folder,
        capture_output=True,
        text=True,
        timeout=30,
        shell=False
    )

    return {
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "success": result.returncode == 0,
    }


if __name__ == "__main__":
    result = run_tests(".")

    print("===== TEST RESULT =====")
    print(result["stdout"])

    if result["stderr"]:
        print("===== ERRORS =====")
        print(result["stderr"])

    print(
        "STATUS:",
        "PASSED" if result["success"] else "FAILED"
    )
