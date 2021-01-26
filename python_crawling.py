from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import datetime
import time




def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)
        
login = {
    "id" : "93_11_23",
    "pw" : "wjaqls_23"
}

driver = webdriver.Chrome(r'C:\Users\손정빈\Desktop\python\JB_Work_21_01_13\chromedriver')
driver.implicitly_wait(1)




driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
# driver.find_element_by_name('id').send_keys("93_11_23")
# driver.find_element_by_name('pw').send_keys("wjaqls_23")
# time.sleep(10);
# driver.find_element_by_xpath('//*[@id="log.login"]').click()

clipboard_input('//*[@id="id"]', login.get("id"))
clipboard_input('//*[@id="pw"]', login.get("pw"))
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(1);
# driver.find_element_by_xpath('/html/body/div/div/div[2]/div[7]/div/a').click()
driver.get('https://blog.naver.com/93_11_23')
driver.find_element_by_xpath('//*[@id="post-admin"]/a[1]').click()





while True:
    time.sleep(1);