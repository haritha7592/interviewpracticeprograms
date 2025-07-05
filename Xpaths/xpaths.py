import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(3)
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys("mobiles")
# #driver.find_element(By.XPATH, "//a[text()='Mobiles']").click()
# #wait = driver.implicitly_wait(5)
# driver.implicitly_wait(3)
# driver.find_element(By.ID, "nav-search-submit-button").click()
# value= driver.find_element(By.XPATH, "//*[@class='a-color-state a-text-bold']")
# status = value.text.strip('"')
# print(status)
# # print(f"Captured text: '{status}'")
# #assert status.text is not None
# assert status == "mobiles"

driver.find_element(By.XPATH, "(//*[@class='nav-flyout-button nav-icon nav-arrow'])[2]")
# driver.find_element(By.XPATH, "(//*[@class='a-icon a-icon-previous-rounded'])[1]")
# driver.find_element(By.XPATH, "//*[@class='hm-icon-label']")
# driver.find_element(By.XPATH, "//*[@class='hm-icon nav-sprite']")
# driver.find_element(By.XPATH, "//*[@id='nav-hamburger-menu']")
# driver.find_element(By.XPATH, "//*[text()='Your Prime Video']")
# driver.find_element(By.XPATH, "//*[@class='nav-action-inner']")
# #
# #
# #
# #
# # #wait.until()
# #
# #
# # # driver.close()
# # driver.quit()
