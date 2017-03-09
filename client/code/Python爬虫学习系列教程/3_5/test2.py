﻿from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.python.org')
assert 'Python' in driver.title
elem = driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
print driver.page_source.__repr__()