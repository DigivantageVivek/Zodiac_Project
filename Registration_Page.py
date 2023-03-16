from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.zodiaconline.com/")

driver.find_element(By.XPATH, "//i[@class='icon-down-open dropdownTriger']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Sign In / Register']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='New User/Register']").click()
driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("Vivek")
driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys("Devkar")
driver.find_element(By.XPATH, "//input[@id='email_address']").send_keys("demo1mail@gmail.com")
driver.find_element(By.XPATH, "//input[@id='mobilenumber']").send_keys("9887655632")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Pass@123")
driver.find_element(By.XPATH, "//input[@id='password-confirmation']").send_keys("Pass@123")
driver.find_element(By.XPATH, "//span[normalize-space()='Create an Account']").click()

if driver.find_element(By.XPATH, "//h1[normalize-space()='Profile Details']").is_displayed():
    print("Test Case Passed")

driver.find_element(By.)