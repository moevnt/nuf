from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://bumble.com/login/enter-phone'
number = '6092878113'

driver = webdriver.Chrome('/home/evan/PycharmProjects/chromedriver')
driver.get(url)

time.sleep(30)


while True:
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT).perform()
    time.sleep(1)