'''
Created on 16/03/2017

@author: Rachappa
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.youtube.com/")
    driver.find_element_by_id("masthead-search-term").send_keys("news")
    driver.find_element_by_id("search-btn").click()
    time.sleep(1)
    driver.find_element_by_class_name("yt-lockup-thumbnail").click()
    
    
    # Added new steps
    driver.find_element_by_id("FirstName").send_keys("rachappa")
    driver.find_element_by_xpath("//*[@id='LastName']").send_keys("rachappaa")
    driver.find_element_by_xpath("//*[@id='GmailAddress']").send_keys("rachu22goalsr@gmail.com")
    driver.find_element_by_xpath("//*[@id='Passwd']").send_keys("ragoal222")
    driver.find_element_by_xpath("//*[@id='PasswdAgain']").send_keys("ragoal222")
    driver.find_element_by_id("BirthMonth").click()
    driver.find_element_by_xpath(".//*[@id=':9']/div").click()
