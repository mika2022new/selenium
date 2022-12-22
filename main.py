
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("C:/Users/Model/Desktop/auto_test/chromedriver")

driver.get("https://www.google.com")

driver.find_element(By.XPATH, "//*[@name=\"q\"]").send_keys('ace of base' + Keys.RETURN)

sleep(3)

driver.save_screenshot('sf.png')

driver.quit()

