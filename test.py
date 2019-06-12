from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#import the chrome driver for opening the browser
browser = webdriver.Chrome('/users/saral/Desktop/chromedriver')

#open a website
browser.get('http://www.goodreads.com/')
#sign in with google
browser.find_element_by_xpath('//*[@title="Sign in with your Google account"]').click()
#fill in the google credentials
username = browser.find_element_by_name("identifier")
# browser.find_element_by_class_name('whsOnd')
username.send_keys('saral.karki@gmail.com')
username.send_keys(Keys.ENTER)
# since the script runs fast it does not get enough time to find the item. Hence we add a wait method to 
#wait until it finds the locator
# try:
#     element = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.NAME, "password"))
        
#     )
# finally:
#     pass
browser.implicitly_wait(10)
element = browser.find_element_by_name('password')
element.send_keys('liv3rpool fc1892')
element.send_keys(Keys.ENTER)
# book read update
# currently_reading = browser.find_element_by_xpath('//*[@href="/book/show/31706504-barking-up-the-wrong-tree"]')
# print(currently_reading)

# browser.implicitly_wait(10)
# update the current book
# book_up  = browser.find_element_by_class_name("gr-book__additionalContent")
update = browser.find_element(By.XPATH, '//button[text()="Update progress"]')
update.click()
browser.implicitly_wait(10)

#the popup div
progress = browser.find_element_by_class_name("updateReadingProgress__headerInput")
progress.clear()
progress.send_keys('181')

# click Update progress link
final_update = browser.find_element(By.XPATH, '//button[text()="Update progress"]')
final_update.click()
browser.implicitly_wait(5)

browser.quit()





