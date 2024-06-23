import subprocess
import os

def run_safety():
    requirements_file = 'test_web/requirements.txt'
    if os.path.exists(requirements_file):
        result = subprocess.run(['safety', 'check', '-r', requirements_file], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            raise Exception("Dependency issues found")
    else:
        print(f"{requirements_file} not found, skipping dependency scanning.")

if __name__ == "__main__":
    run_safety()

