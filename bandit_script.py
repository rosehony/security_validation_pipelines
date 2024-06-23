import subprocess

def run_bandit():
    result = subprocess.run(['bandit', '-r', 'test_web'], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception("Security issues found")

if __name__ == "__main__":
    run_bandit()
