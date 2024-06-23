import subprocess

def run_safety():
    result = subprocess.run(['safety', 'check', '-r', 'test_web/requirements.txt'], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception("Dependency issues found")

if __name__ == "__main__":
    run_safety()
