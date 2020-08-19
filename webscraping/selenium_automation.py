from selenium import webdriver
browser = webdriver.Firefox()

# install the latest geckodriver from 
# https://github.com/mozilla/geckodriver/releases/tag/v0.27.0
# add the path to the driver in environmental variables

browser.get('https://automatetheboringstuff.com/')
element = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
element.click()

elements = browser.find_elements_by_css_selector('p')

# to find all text on a webpage select the 'html' element and call the 'text' property
html = browser.find_element_by_css_selector('html')
print(html.text)