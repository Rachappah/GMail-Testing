'''
Created on 15/03/2017

@author: Rachappa
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.google.com/gmail")
    driver.find_element_by_xpath("//input[@id='Email']").send_keys("rachappahalinge")
    driver.find_element_by_xpath("//*[@id='link-signup']/a").click()
    time.sleep(3)
    driver.find_element_by_id("FirstName").send_keys("rachappa")
    driver.find_element_by_xpath("//*[@id='LastName']").send_keys("rachappaa")
    driver.find_element_by_xpath("//*[@id='GmailAddress']").send_keys("rachu22goalsr@gmail.com")
    driver.find_element_by_xpath("//*[@id='Passwd']").send_keys("ragoal222")
    driver.find_element_by_xpath("//*[@id='PasswdAgain']").send_keys("ragoal222")
    driver.find_element_by_id("BirthMonth").click()
    driver.find_element_by_xpath(".//*[@id=':9']/div").click()
    driver.find_element_by_id("BirthDay").send_keys("12")
    driver.find_element_by_id("BirthYear").send_keys("1990")
    driver.find_elements_by_id("Gender")
    element =driver.find_element_by_xpath("//label/div/div[@class='goog-inline-block goog-flat-menu-button jfk-select']")
    e1=element.click()
    element.send_keys("male")
    element.click()
    driver.find_element_by_id("RecoveryPhoneNumber").send_keys("7353249488")
    driver.find_element_by_id("RecoveryEmailAddress").send_keys("rachappahalinge@gmail.com")
    driver.find_element_by_id("submitbutton").click()
    time.sleep(1)
    driver.find_element_by_class_name("tos-scroll-button-icon").click()
    time.sleep(1)
    driver.find_element_by_class_name("tos-scroll-button-content").click()
    time.sleep(1)
    driver.find_element_by_id("iagreebutton").click()
    time.sleep(1)
    driver.find_element_by_id("signupidvinput")
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='i18n_phone_number_input-inner_input']").click()
    
   
    
    