import psutil
import time
from selenium import webdriver


class SiteStater:
    baseline_website = 'http://whatismyip.akamai.com'  # ეს უფრო სწრაფად იტვირთება ვიდრე Google

    @staticmethod
    def stat_current():
        return psutil.cpu_percent(interval=None)

    def stat_website(self, site_url):
        self.stat_current()
        self.driver.get(site_url)
        time.sleep(5)  # CPU ბოლომდე რომ აიწიოს
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
        urls = f.readlines()
    stater = SiteStater()

    for url in urls:
        url = url.strip().decode()
        if not url.startswith("http"):
            break
        score = stater.stat_website(url)
        print('{} consumption at {}'.format(url, score))
    stater.close()


if __name__ == "__main__":
    main()
