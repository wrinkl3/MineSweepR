import psutil, time
from selenium import webdriver


class SiteStater:
    def go_to_baseline(self):
        self.driver.get(self.baseline_website)

    def stat_current(self):
        return self.process.cpu_percent(interval=None)

    def stat_website(self, site_url):
        self.init_driver()
        self.go_to_baseline()
        self.stat_current()
        self.driver.get(site_url)
        time.sleep(2)
        after = self.stat_current()
        self.close()

        return after

    def init_driver(self):
	self.driver = webdriver.PhantomJS()
        for child in psutil.Process().children():
            if 'phantom' in child.name():  # 'geckodriver' for firefox
                self.process = child
                break
        if not self.process:
            raise Exception('Failed to launch PhantomJS')

    def __init__(self):
	self.driver = None
	self.process = None
        self.baseline_website = 'http://whatismyip.akamai.com'

    def close(self):
        self.driver.quit()
