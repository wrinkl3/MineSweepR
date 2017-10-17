# MineSweepR
(tentatively named)

A Python 3 tool and library that scans websites for signs of abnormal CPU usage that might be indicative of embedded Javascript miners.

## Prerequisites
Python 3   
Selenium  
psutil  
PhantomJS  

## Sweeper Usage
The sweeper visits every website on a given list using a headless browser and checks the CPU usage on each of those websites. The readings are than analyzed using IQR and the outliers (websites with abnormally high CPU consumption) are outputted.  

```
usage: sweep.py [-h] urls

positional arguments:
  urls        the file that contains the urls

optional arguments:
  -h, --help  show this help message and exit
```
## Library Usage

```python
from site_stat import SiteStater

statter = SiteStatter()
urls = ['https://gmail.com', 'https://alibaba.com', 'https://yahoo.com']
scores = [statter.stat_website(url) for url in urls]
print(scores)
```
