import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
import time
import datetime
import telegram_send  # pip install telegram-send


def BTC(driver):
        btcname = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[3]/div/a').text
        btcprice = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[4]/div/a').text
        btc24h =  driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[5]/span').text
        btc24hS = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[5]/span/span').class
        btc7d = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[6]/span').text
        print(btcname,' precio:', btcprice, ' 24h:',btc24h,'signo:',btc24hS,' 7d:',btc7d)


if __name__ == '__main__':

    driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    driver.get("https://coinmarketcap.com/")

    BTC(driver)

    
