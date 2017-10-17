import psutil, time
from selenium import webdriver

class SiteStater:
    baseline_website = 'http://whatismyip.akamai.com'

    def stat_current(self):
        return self.process.cpu_percent(interval=None)

    def stat_website(self, site_url):
        self.stat_current()
        self.driver.get(site_url)
        time.sleep(2)
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