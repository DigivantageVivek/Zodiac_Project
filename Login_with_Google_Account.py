import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.zodiaconline.com/")

driver.find_element(By.XPATH, "//i[@class='icon-down-open dropdownTriger']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Sign In / Register']").click()
