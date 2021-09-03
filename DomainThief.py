from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
# --| Parse or automation
browser.get('https://etherscan.io/enslookup-search?search=tomblack.eth')
only_divs = SoupStrainer("div", {"class": "col-md-3 font-weight-bold font-weight-sm-normal mb-1 mb-md-0"})
soup = BeautifulSoup(browser.page_source, 'lxml', parse_only=only_divs)
browser.implicitly_wait(2)

count = len(soup.find_all("div", {"class": "col-md-3 font-weight-bold font-weight-sm-normal mb-1 mb-md-0"}))

if count > 0:
    print("Taken")
else:
    print("Available")