from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#opening yahoo site using Chromedriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://in.yahoo.com')
browser.find_element_by_xpath("//*[@id='header-signin-link']/span").click()
wait = WebDriverWait(browser, 10)
#entering the email address
emailelem = wait.until(EC.presence_of_element_located((By.ID,'login-username')))
emailelem.send_keys('xxxx@yahoo.com')
time.sleep(3)
#clicking next button
wait.until(EC.presence_of_element_located((By.ID,'login-signin')))
emailelem.submit()
time.sleep(3)

#entering the password and clicking next
wait.until(EC.element_to_be_clickable((By.ID,'login-signin')))
passwordelem = wait.until(EC.presence_of_element_located((By.ID,'login-passwd')))
passwordelem.send_keys('xxxxx')
passwordelem.send_keys(Keys.RETURN)
time.sleep(3)

#clicking mail button
mailelem=wait.until(EC.element_to_be_clickable((By.ID,'header-mail-button')))
mailelem.click()
time.sleep(3)

#clicking compose button
compelem=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[2]/div/div[1]/n
av/div/div[1]/a')))
compelem.click()
time.sleep(3)

#entering email address of recipient
sendelem = wait.until(EC.presence_of_element_located((By.ID,'message-to-field')))
sendelem.send_keys('nigelcrasto12@gmail.com')
time.sleep(3)
#entering subject of the mail

subjectelem=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mail-app-
component"]/div/div/div[1]/div[3]/div/div/input')))

subjectelem.send_keys("TESTING SELENIUM")
time.sleep(3)
#message in mail

msgelem=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="editor-
container"]/div[1]/div')))

msgelem.send_keys("This is a sample email sent for testing.\n")
time.sleep(3)
#sending mail

sElem=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mail-app-
component"]/div/div/div[2]/div[2]/div/button/span')))

sElem.click()
