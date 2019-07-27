from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

url = 'https://login.microsoftonline.com/'

driver = webdriver.Chrome('/home/evan/PycharmProjects/chromedriver')
driver.get(url)

emailField = driver.find_element_by_id('i0116')
emailField.send_keys('monteithew21@mail.vmi.edu')

nextButton = driver.find_element_by_id('idSIButton9')
nextButton.click()

passwordField = driver.find_element_by_id('i0118')
passwordField.send_keys('1qazXDR%')

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()


#driver.execute_script("window.open('');")

#driver.switch_to.window(driver.window_handles[1])
#driver.get("https://mail.google.com")

#gmailField = driver.find_element_by_id('identifierId')
#gmailField.send_keys('evan.monteith@gmail.com')

#gmailNext = driver.find_element_by_id('identifierNext')
#gmailNext.click()

