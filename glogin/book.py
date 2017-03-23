'''
Created on 17/03/2017

@author: Rachappa
'''
from selenium import webdriver
from glogin.signin import driver
if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get("//http:www.gmail.com")
    driver.close()
