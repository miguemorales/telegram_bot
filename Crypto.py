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
    data0 = {}
    for cripto in criptos:
        aux = []
        aux.append(Buscador(driver,cripto))
        aux.append(Precios(driver,aux[0])[0])
        aux.append(Precios(driver,aux[0])[1])
        aux.append(Precios(driver,aux[0])[2])
        data0[cripto] = aux

    print(data0)

    #Hata aqui ya crea el dic de moneda, posicion y valores inciales

    inicio = time.time()
    done = 0
    Cdone = []
    data1 = data0.copy()
    while (done < len(criptos)):
        time.sleep(2)
        driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        driver.get("https://coinmarketcap.com/")
        for cripto in criptos:
                if (data0[cripto][1] != Precios(driver,data0[cripto][0]) and cripto not in Cdone):
                        print('Entro, precio anterior: ',data0[cripto][1],'precio nuevo: ',Precios(driver,data0[cripto][0]), 'criptos hechas: ',Cdone)
                        done = done +1
                        Cdone.append(cripto)
    #once I know all i have old and new data, i compare
    data1 = data0.copy()                 
    for cripto in criptos:
        
        data1[cripto][1:] = Precios(driver,data1[cripto][0])

    print(data1)
    for cripto in criptos:     
        if (float(data0[cripto][1][1:].replace(',','')) < float(data1[cripto][1][1:].replace(',',''))):
                if (float(data0[cripto][2].replace('%','')) < float(data1[cripto][2].replace('%',''))):
                        data1[cripto][2] = '-' + data1[cripto][2]
                if (float(data0[cripto][3].replace('%','')) < float(data1[cripto][3].replace('%',''))):
                        data1[cripto][3] = '-' + data1[cripto][3]
    for cripto in criptos:
        print(cripto,': ',data1[cripto])
        
    print('Tiempo de ejecucion: ', time.time()-inicio)
        
        

    
