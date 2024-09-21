from selenium import webdriver
from selenium.webdriver.common.by import By

def startbot(username, password, url):
    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_element(By.NAME, "login").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    
    driver.find_element(By.NAME, "commit").click()

username = input("Enter your username: ")
password = input("Enter your password: ")
url = input("Enter the url of login page: ")

startbot(username, password, url)
