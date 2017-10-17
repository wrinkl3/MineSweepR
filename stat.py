import psutil, time
from selenium import webdriver
from utils import upper_outlier_indices
from operator import itemgetter


class SiteStater:
    baseline_website = 'http://whatismyip.akamai.com'

    def stat_current(self):
        return self.process.cpu_percent(interval=None)

    def stat_website(self, site_url):
        self.stat_current()
        self.driver.get(site_url)
        time.sleep(5)
        after = self.stat_current()
        #self.init_driver()
        self.go_to_baseline()

        return after

    def init_driver(self):
        if hasattr(self, 'driver'):
            self.close()
            self.process = None
        self.driver = webdriver.PhantomJS()
        for child in psutil.Process().children():
            if 'phantomjs' in child.name():
                self.process = child
                break
        if not hasattr(self, 'process') or self.process is None:
            raise Error('Failed to launch PhantomJS')

    def go_to_baseline(self):
        self.driver.get(self.baseline_website)
    
    def __init__(self):
        self.init_driver()
        self.go_to_baseline() # initial

    def close(self):
        self.driver.close()


def main():
    with open("./urls.list", "rb") as f:
        urls = [url.strip().decode() for url in f.readlines() if url.startswith(b'http')]
    stater = SiteStater()

    scores = [stater.stat_website(url) for url in urls]
    print(scores)
    indices = upper_outlier_indices(scores, 0.5)
    if len(indices)>0:
        print('These websites might have a miner:')
        print(itemgetter(*indices)(urls))
    else:
        print('No outliers detected')

if __name__ == "__main__":
    main()
