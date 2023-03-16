import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.zodiaconline.com/")

driver.find_element(By.XPATH, "//i[@class='icon-down-open dropdownTriger']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Sign In / Register']").click()

# Enter Mobile number & Click on 'Submit'
driver.find_element(By.XPATH, "//form[@id='fchknum_form']//input[@id='mobilenumber']").send_keys(7843000238)
driver.find_element(By.XPATH, "//button[@id='fchknum']").click()
time.sleep(30)

# Enter OTP & Click on 'Submit'
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(8262)
driver.find_element(By.XPATH, "//button[@id='fwithotp']").click()

# driver.quit()