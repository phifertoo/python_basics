import bs4
import requests


# headers = {'user-agent': 'Mozilla/5.0'}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}  # to make the server think its a web browser and not a bot

amzn_res2 = requests.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers', headers = headers )
amzn_soup2 = bs4.BeautifulSoup(amzn_res2.text,'lxml')
amzn_elements2 = amzn_soup2.findAll('#zg_left_col1 > div:nth-child(1)')
print(amzn_elements2)
# import requests
# from bs4 import BeautifulSoup 

# def make_soup(url: str) -> BeautifulSoup:
#     res = requests.get(url, headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
#     })
#     res.raise_for_status()
#     return BeautifulSoup(res.text, 'lxml')

# def parse_product_page(soup: BeautifulSoup) -> dict:
#     title = soup.select_one('#productTitle').text.strip()
#     return {
#         'title': title
#     }

# if __name__ == "__main__":
#     url = 'https://www.amazon.com/Nike-Rival-Track-Field-Shoes/dp/B07HYNB7VV/'
#     soup = make_soup(url)
#     info = parse_product_page(soup)
#     print(res.text) 
