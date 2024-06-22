import subprocess

def run_zap():
    # Start ZAP
    start_result = subprocess.run(['zap-cli', 'start'], capture_output=True, text=True)
    if start_result.returncode != 0:
        raise Exception("Failed to start OWASP ZAP")

    # Open target URL (replace with your actual application URL)
    target_url = 'http://your_application_url'
    open_url_result = subprocess.run(['zap-cli', 'open-url', target_url], capture_output=True, text=True)
    if open_url_result.returncode != 0:
        raise Exception(f"Failed to open URL {target_url}")

    # Run active scan
    scan_result = subprocess.run(['zap-cli', 'active-scan', target_url], capture_output=True, text=True)
    if scan_result.returncode != 0:
        raise Exception(f"Failed to perform active scan on {target_url}")

    # Generate report
    report_result = subprocess.run(['zap-cli', 'report', '-o', 'zap_report.html', '-f', 'html'], capture_output=True, text=True)
    if report_result.returncode != 0:
        raise Exception("Failed to generate ZAP report")

    print(report_result.stdout)
    if "High" in report_result.stdout or "Medium" in report_result.stdout:
        raise Exception("High or Medium risk vulnerabilities found")

if __name__ == "__main__":
    run_zap()
