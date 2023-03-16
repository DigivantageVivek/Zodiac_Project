import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.zodiaconline.com/")

driver.find_element(By.XPATH, "//i[@class='icon-down-open dropdownTriger']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Sign In / Register']").click()
driver.find_element(By.XPATH, "//input[@id='logtypeboxemail']").click()

# Enter Email & click on submit
driver.find_element(By.XPATH, "//form[@id='fchknum_form']//input[@id='mobilenumber']").send_keys("demo1mail@gmail.com")
driver.find_element(By.XPATH, "//button[@id='fchknum']").click()
time.sleep(20)

# Enter Password & click on submit
driver.find_element(By.XPATH, "//input[@id='login_password']").send_keys("Pass@123")
driver.find_element(By.XPATH, "//button[@id='fwithotp']").click()


if driver.find_element(By.LINK_TEXT, "NEW ARRIVALS").is_displayed():
     print("Test Case Passed")











