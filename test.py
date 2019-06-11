from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#import the chrome driver for opening the browser
browser = webdriver.Chrome('/users/saral/Desktop/chromedriver')

#open a website
browser.get('http://www.goodreads.com/')
#sign in with google
browser.find_element_by_xpath('//*[@title="Sign in with your Google account"]').click()
#fill in the google credentials

username = browser.find_element_by_class_name('whsOnd')
username.send_keys('saral.karki@gmail.com')
username.send_keys(Keys.ENTER)


# browser.find_element_by_xpath('//*[@name="password"]')
# pwd = browser.find_element_by_name('password')
element = browser.find_element_by_xpath('//*[@type="password"]')
print(element.text)
element.send_keys('liv3rpool fc1892')
element.send_keys(Keys.ENTER)
#hit enter


