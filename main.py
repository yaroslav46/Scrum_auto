from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import db
from time import sleep



driver = webdriver.Edge()

driver.get(config.URL)
driver.find_element(By.NAME, 'os_username').send_keys(config.USERNAME)
driver.find_element(By.NAME, 'os_password').send_keys(config.PASSWORD)

driver.find_element(By.NAME, 'os_password').send_keys(Keys.ENTER)
sleep(2)
driver.find_element(By.ID, 'create_link').click()
sleep(1)
driver.refresh()
sleep(3)

info = db.get_info()
for i in info:
    driver.find_element(By.ID, 'create_link').click()
    sleep(5)
    driver.find_element(By.ID, 'summary').send_keys(i['Work'])
    #driver.find_element(By.ID, 'mce_7_ifr').send_keys(i['info_field'])
    driver.find_element(By.ID, 'assignee-field').send_keys(Keys.CONTROL,"A")
    driver.find_element(By.ID, 'assignee-field').send_keys(i['name'])
    sleep(2)
    driver.find_element(By.ID, 'assignee-field').send_keys(Keys.ENTER)
    sleep(1)
    driver.find_element(By.ID, 'duedate').send_keys(i['date'])
    sleep(1)
    driver.find_element(By.ID, 'duedate').send_keys(Keys.ALT,"S")
    
    
    
sleep(1000)