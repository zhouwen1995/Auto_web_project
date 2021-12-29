# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

try:
    driver = webdriver.Firefox()
    # sleep(3)
    # driver.maximize_window()
    first_url = "http://www.baidu.com"
    driver.get(first_url)

    # driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("Selenium2")
    # driver.find_element(By.ID, "su").click()

    # driver.find_element(By.LINK_TEXT, "新闻").click()

    # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/a[1]").click()

    # driver.find_element(By.XPATH, "//input[@id = 'kw']").send_keys("Selenium2")
    # driver.find_element(By.XPATH, "//input[@id = 'su']").click()

    # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/div/div[3]/ul/li[3]/a/span[2]").click()

    driver.find_element(By.XPATH, "//*[@id = 'kw' and @class = 's_ipt']").send_keys("Selenium2")
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id = 'kw' and @class = 's_ipt']").clear()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id = 'kw']").send_keys("Selenium3")
    driver.find_element(By.XPATH, "//*[@id = 'kw']").submit()
    sleep(1)
    driver.back()
    sleep(1)
    driver.forward()
    driver.refresh()



    sleep(3)
    driver.quit()
except Exception as unusual:
    print(unusual)
