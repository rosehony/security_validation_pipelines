import subprocess

def run_safety():
    result = subprocess.run(['safety', 'check'], capture_output=True, text=True)
    print(result.stdout)
    if "vulnerabilities found" in result.stdout:
        raise Exception("Vulnerable dependencies found")

if __name__ == "__main__":
    run_safety()
