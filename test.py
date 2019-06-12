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

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
        
    )
finally:
    pass
element.send_keys('liv3rpool fc1892')
element.send_keys(Keys.ENTER)




# browser.quit()

# browser.find_element_by_xpath('//*[@name="password"]')
# pwd = browser.find_element_by_name('password')

# pwd  = browser.find_element_by_xpath('//*[@aria-label="तपाईको पासवर्ड प्रविष्टि गर्नुहोस्"]')
# # pwd = browser.find_element_by_name("password")
# print(pwd.text)
# pwd.send_keys('liv3rpool fc1892')
# pwd.send_keys(Keys.ENTER)
# #hit enter


