
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("C:/Users/Model/Desktop/auto_test/chromedriver")

# ----------------- 1-st ----------------------

# driver.get("https://www.google.com")

# driver.find_element(By.XPATH, "//*[@name=\"q\"]").send_keys('ace of base' + Keys.RETURN)

# sleep(3)

# driver.save_screenshot('sf.png')

# driver.quit()


# ----------------- 2-nd ----------------------

driver.get("http://130.193.37.179/app/pets")

# t = driver.find_elements(By.XPATH, "//*[@id=\"image\"]/img")
t = (driver.find_elements(By.XPATH, "//*[@id=\"image\"]/img"))[1].click()


print(t)

sleep(10)
driver.save_screenshot('pet.jpg')
driver.quit()


45:45