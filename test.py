from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from password import credentials

un,pwd = credentials()
#import the chrome driver for opening the browser
browser = webdriver.Chrome('/users/saral/Desktop/chromedriver')

#open a website
browser.get('http://www.goodreads.com/')
#sign in with google
browser.find_element_by_xpath('//*[@title="Sign in with your Google account"]').click()
#fill in the google credentials
username = browser.find_element_by_name("identifier")
# browser.find_element_by_class_name('whsOnd')
username.send_keys(un)
username.send_keys(Keys.ENTER)
# since the script runs fast it does not get enough time to find the item. Hence we add a wait 
browser.implicitly_wait(10)
element = browser.find_element_by_name('password')
element.send_keys(pwd)
element.send_keys(Keys.ENTER)
# update the current book
update = browser.find_element(By.XPATH, '//button[text()="Update progress"]')
update.click()
browser.implicitly_wait(10)

#access the update div 
progress = browser.find_element_by_class_name("updateReadingProgress__headerInput")
progress.clear()
progress.send_keys('181')

# click Update progress link
final_update = browser.find_element(By.XPATH, '//button[text()="Update progress"]')
final_update.click()

browser.quit()





