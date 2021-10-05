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


def Precios(driver,i):
        criptoname = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr['+str(i)+']/td[3]/div/a/div/div/p').text
        criptoprice = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr['+str(i)+']/td[4]/div/a').text
        cripto24h =  driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr['+str(i)+']/td[5]/span').text
        cripto7d = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr['+str(i)+']/td[6]/span').text
        
        return  criptoprice, cripto24h, cripto7d

def Buscador(driver, cryp):
        for z in range(30):
                i= z+1
                palabra = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr['+str(i)+']/td[3]/div/a/div/div/p').text
                if (cryp == palabra):
                        return i

if __name__ == '__main__':

    criptos = ['Bitcoin','Ethereum','Cardano','Polkadot']
    driver = webdriver.Chrome('chromedriver',options=chrome_options)
    driver.get("https://coinmarketcap.com/")
    db = {}
    for cripto in criptos:
        aux = []
        aux.append(Buscador(driver,cripto))
        db[cripto] = aux
        db[cripto].append(list(Precios(driver,aux[0])))
        #print(db)
    print(db)
    
    '''prevprice, prev24h, prev7d = precios(driver)
    newbtcprice = prevbtcprice
    inicio = time.time()
    while(newbtcprice == prevbtcprice):
        time.sleep(2)
        driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        driver.get("https://coinmarketcap.com/")
        newbtcprice, newbtc24h, newbtc7d = precios(driver)
        
    if (newbtcprice < prevbtcprice):
        if (newbtc24h > prevbtc24h):
                newbtc24h = '-' + newbtc24h
        if(newbtc7d > prevbtc7d):
                newbtc7d = '-' + newbtc7d
                
    print('BTC-> precio:', btcprice, ' 24h:',btc24h,' 7d:',btc7d)
    print('Tiempo de ejecucion: ', time.time()-inicio)'''
        
        

    
