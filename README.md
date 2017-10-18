# MineSweepR
(tentatively named)

A Python 3 tool and library that scans websites for signs of abnormal CPU usage which might be indicative of embedded Javascript miners.

## Prerequisites
* Python 3   
* Selenium  
* psutil  
* NumPy  
* PhantomJS  

## Sweeper Usage
The sweeper visits every website on a given list using a headless browser and checks the CPU usage on each of those websites. The readings are then analyzed using IQR and the outliers (websites with abnormally high CPU consumption) are outputted.  

```
usage: sweep.py [-h] [-t TIMEOUT] [-p PAUSE] urls

positional arguments:
  urls                  the file that contains the urls

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        how much the browser should wait for the page before
                        timing out
  -p PAUSE, --pause PAUSE
                        how much the browser should stay on a page before
                        measuring the cpu performance
```
## Library Usage

```python
from site_stat import SiteStater

statter = SiteStatter()
urls = ['https://gmail.com', 'https://alibaba.com', 'https://yahoo.com']
scores = [statter.stat_website(url) for url in urls]
print(scores)
```
