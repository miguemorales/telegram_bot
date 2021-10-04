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
        btcname = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[3]/div/a/div/div/p').text
        btcprice = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[4]/div/a').text
        btc24h =  driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[5]/span').text
        btc7d = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[6]/span').text
         print(btcname,'-> precio:', btcprice, ' %24h:',btc24h,' %7d:',btc7d)
        
        return btcprice, btc24h, btc7d


if __name__ == '__main__':

    Criptos = ['Bitcoin','Ethereum','Cardano','Polkadot']
    driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    driver.get("https://coinmarketcap.com/")

    prevbtcprice, prevbtc24h, prevbtc7d = BTC(driver)
    newbtcprice = prevbtcprice
    inicio = time.time()
    while(newbtcprice == prevbtcprice):
        time.sleep(5)
        newbtcprice, newbtc24h, newbtc7d = BTC(driver)
        
    if (newbtcprice < prevbtcprice):
        if (newbtc24h > prevbtc24h):
                newbtc24h = -newbtc24h
        if(newbtc7d > prevbtc7d):
                newbtc7d = -newbtc7d
                
    print('BTC-> precio:', btcprice, ' 24h:',btc24h,' 7d:',btc7d)
    print('Tiempo de ejecucion: ', time.time()-inicio)
        
        

    
