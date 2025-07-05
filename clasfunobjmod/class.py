import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#encapulation class
class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def url(self, url):
        self.driver.get(url)
        #print(self.driver.title)
    def maximize(self):
        self.driver.maximize_window()
        print("window maximised")
        time.sleep(3)
    def perform(self):
        element = self.driver.find_element(By.XPATH, "//*[text()='Your Prime Video']")
        element.click()
    def close(self):
        self.driver.close()
        print("window closed")
#Inheritance
class Implementation(Browser):
    def __init__(self):
        super().__init__()# this is required becoz im using initalizing new variable title.
        self.title = "Shopping"
    def get_url(self):
        self.url("https://www.amazon.in")
        assert self.title in self.driver.title, f"Expected '{self.title}' is not  in '{self.driver.title}'"
        print(f"Assertion passed,  '{self.title}' in '{self.driver.title}'")
    def perform(self): # Polymorphism-- two different classes with same method name
        dom_ele = self.driver.find_element(By.XPATH, "//*[@class='nav-a  ' and text()='Mobiles']")
        dom_ele.click()
        print("movies searched")

actions = Browser()
actions.maximize()
run = Implementation()
run.get_url()
run.perform()
actions.close()

#actions.url("https://www.amazon.in")
#driver = webdriver.Chrome()
# class Poly():
#     # def __init__(self):
#     #     self.driver = webdriver.Chrome()
#     def url(url):
#         driver.get("https://www.amazon.in")