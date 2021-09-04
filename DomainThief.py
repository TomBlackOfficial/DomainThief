from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.chrome.options import Options
import requests

counter = 0

options = Options()
options.add_argument("--incognito")

url = "https://alter.com/blog/top-domain-name-sales"
requests_session = requests.Session()
source_code = requests_session.get(url)
plain_text = source_code.text
soup1 = BeautifulSoup(plain_text, 'lxml')

gdp_table = soup1.find("table", attrs={"class": "table"})
gdp_table_data = gdp_table.tbody.find_all("tr")

for dataItem in gdp_table_data:
    domain_raw = dataItem.find_all("td")[1].text
    if ".com" in domain_raw:
        domain = domain_raw[:len(domain_raw) - 4]
        if len(domain) > 2:
            counter += 1
            print(counter)

            if counter > 383:
                browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
                browser.get('https://etherscan.io/enslookup-search?search=' + domain + '.eth')

                only_divs = SoupStrainer("div", {"class": "col-md-3 font-weight-bold font-weight-sm-normal mb-1 mb-md-0"})
                soup2 = BeautifulSoup(browser.page_source, 'lxml', parse_only=only_divs)
                browser.implicitly_wait(2)

                count = len(soup2.find_all("div", {"class": "col-md-3 font-weight-bold font-weight-sm-normal mb-1 mb-md-0"}))

                if count == 0:
                    print(domain + ".eth" + " is Available")

                browser.close()
