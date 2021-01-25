from selenium import webdriver
import datetime
import time

login = {
    "id" : "93_11_23",
    "pw" : "wjaqls_23"
}

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)


driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.find_element_by_name('id').send_keys("93_11_23")
driver.find_element_by_name('pw').send_keys("wjaqls_23")
time.sleep(10);
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


while True:
    time.sleep(1);