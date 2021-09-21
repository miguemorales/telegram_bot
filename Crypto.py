from selenium import webdriver  #to install: "pip install selenium"
import time
import datetime
import telegram_send  # pip install telegram-send


def BTC(driver):
        btcname = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[3]/div/a').text
        btcprice = driverfind_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[4]/div/a').text
        btc24h =  driverfind_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[5]/span').text
        btc7d = driverfind_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[6]/span').text
        print(btcname,' precio:', btcprice, ' 24h:',btc24h,' 7d:',btc7d)


if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get("https://coinmarketcap.com/")

    BTC(driver)

    
