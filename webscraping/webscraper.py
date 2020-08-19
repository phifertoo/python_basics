import bs4
import requests


# In order to access https (secure) websites, I had to copy
# libcrypto-1_1-x64.*
# libssl-1_1-x64.*
# from C:\Users\phife\anaconda3\Library\bin to C:\Users\phife\anaconda3\DLLs
res = requests.get('https://www.cnn.com/2020/08/16/health/us-coronavirus-sunday/index.html')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# right click => inspect
# In the inspect panel, right click on the desired element => copy => copy selector
# buybox > div > table > tbody > tr.kindle-price > td.a-color-price.a-size-medium.a-align-bottom > span

elements = soup.select('body > div.pg-right-rail-tall.pg-wrapper > article > div.l-container > h1')
print(elements)



headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
# amzn_res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994', headers = headers )
# amzn_soup = bs4.BeautifulSoup(res.text,'lxml')
# amzn_elements = amzn_soup.find_all('#iframeContent')
# print(amzn_elements)


# headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
# yahoo_res = requests.get('https://www.yahoo.com/')
# yahoo_soup = bs4.BeautifulSoup(res.text,'html.parser')
# yahoo_elements = yahoo_soup.select('.class')
# #applet_p_50000295 > div > div > div.tabs-section.Ovx\(h\)
# print(yahoo_elements)

yahoof_res = requests.get('https://finance.yahoo.com/quote/ES=F?p=ES=F')
yahoof_soup = bs4.BeautifulSoup(yahoof_res.text,'html.parser')
yahoof_elements = yahoof_soup.select('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)')
#applet_p_50000295 > div > div > div.tabs-section.Ovx\(h\)
print(yahoof_elements)
