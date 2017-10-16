from selenium import webdriver
import psutil, time

class SiteStater:
	baseline_website = 'https://google.com/'

	def stat_current(self):
		return psutil.cpu_percent(interval=None)

	def stat_website(self, site_url):
		self.stat_current()
		self.driver.get(site_url)
		time.sleep(2)
		after = self.stat_current()
		self.driver.get(self.baseline_website)
		return after

	def __init__(self):
		self.driver = webdriver.PhantomJS()
		self.driver.get(self.baseline_website)
		self.stat_current() #initial call

	def close(self):
		self.driver.close()

def main():
	urls = ['https://alibaba.com','http://npa.ge/Video/details/760/------', 'https://facebook.com']
	stater = SiteStater()
	for url in urls:
		score = stater.stat_website(url)
		print '{} consumption at {}'.format(url, score)
	stater.close()

if __name__ == "__main__": main()
