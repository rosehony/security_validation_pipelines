import subprocess

def run_zap_scan():
    # Running the ZAP scan
    subprocess.run(['zap-cli', '--zap-url', 'http://localhost:8080', 'quick-scan', 'http://example.com'], check=True)
    # Generating the report
    subprocess.run(['zap-cli', '--zap-url', 'http://localhost:8080', 'report', '-o', 'zap_report.html', '-f', 'html'], check=True)

if __name__ == "__main__":
    run_zap_scan()
