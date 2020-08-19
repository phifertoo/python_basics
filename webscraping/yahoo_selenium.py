from selenium import webdriver
browser = webdriver.Firefox()

# install the latest geckodriver from 
# https://github.com/mozilla/geckodriver/releases/tag/v0.27.0
# add the path to the driver in environmental variables

browser.get('https://www.yahoo.com/')
searchElement = browser.find_element_by_css_selector('#header-search-input')
searchElement.send_keys('zophie')
searchElement.submit()

# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()