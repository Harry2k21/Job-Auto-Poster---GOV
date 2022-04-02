from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\Users\Kim\Desktop\Python Projects\chromedriver_win32\chromedriver.exe')
driver.get("https://findajob.dwp.gov.uk/employer/companies/59287/advert/2494496/clone")

elem = driver.find_element_by_xpath('//*[@id="email"]')
elem.send_keys("harry.parker@justintimeresourcing.co.uk")

elem = driver.find_element_by_xpath('//*[@id="password"]')
elem.send_keys("rohan123")

elem = driver.find_element_by_xpath('//*[@id="main"]/main/div[2]/div[1]/form/fieldset/div[3]/input')
elem.send_keys(Keys.RETURN)

groups = ["1","Sheffield, South Yorkshire","Harrogate, North Yorkshire",""]
for i in range(len(groups)):
   driver.get("http://www.google.com/")
   driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
# You can use (Keys.CONTROL + 't') on other OSs
# Load a page 
   driver.get(r'https://findajob.dwp.gov.uk/employer/companies/59287/advert/2494496/clone')
   time.sleep(1)
   elem = driver.find_element_by_xpath('//*[@id="location"]')
   elem.send_keys(groups[i])

   elem = driver.find_element_by_xpath('//*[@id="main"]/div/div/form/button[1]')
   elem.send_keys(Keys.RETURN)
   time.sleep(1)

