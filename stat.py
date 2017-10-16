import psutil, time
from selenium import webdriver
from utils import upper_outlier_indices
from operator import itemgetter


class SiteStater:
    baseline_website = 'http://whatismyip.akamai.com'

    @staticmethod
    def stat_current():
        return psutil.cpu_percent(interval=None)

    def stat_website(self, site_url):
        time.sleep(5)
        self.stat_current()
        self.driver.get(site_url)
        time.sleep(2)  # CPU ბოლომდე რომ აიწიოს
        after = self.stat_current()
        self.driver.get(self.baseline_website)  # reset

        return after

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.baseline_website)  # initial

    def close(self):
        self.driver.close()


def main():
    with open("./urls.list", "rb") as f:
        urls = [url.strip().decode() for url in f.readlines() if url.startswith(b'http')]
    stater = SiteStater()

    '''
    for url in urls:
        url = url.strip().decode()
        if not url.startswith("http"):
            continue
        score = stater.stat_website(url)
        print('{} consumption at {}'.format(url, score))
    stater.close()
    '''
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
