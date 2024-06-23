import time
from zapv2 import ZAPv2

def run_zap_scan():
    target = 'http://example.com'
    zap = ZAPv2()

    # Start a new session
    print('Accessing target {}'.format(target))
    zap.urlopen(target)
    time.sleep(2)  # Give the scanner time to start

    print('Spidering target {}'.format(target))
    scan_id = zap.spider.scan(target)
    while int(zap.spider.status(scan_id)) < 100:
        print('Spider progress %: {}'.format(zap.spider.status(scan_id)))
        time.sleep(2)
    print('Spider completed')

    print('Scanning target {}'.format(target))
    scan_id = zap.ascan.scan(target)
    while int(zap.ascan.status(scan_id)) < 100:
        print('Scan progress %: {}'.format(zap.ascan.status(scan_id)))
        time.sleep(5)
    print('Scan completed')

    # Generate report
    with open('zap_report.html', 'w') as f:
        f.write(zap.core.htmlreport())

if __name__ == "__main__":
    run_zap_scan()
