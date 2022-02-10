from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Firefox()
driver.get('https://finance.yahoo.com/quote/BTC-EUR/history/')

csvDictList = []
fieldNames = ['Date', 'Close']
csvFile = open('eur_btc_rates.csv', 'w', newline='')
writer = csv.DictWriter(csvFile, fieldNames)
writer.writeheader()

i = 1
while (i <= 10):
	date = driver.find_element(By.XPATH, '//table/tbody/tr[%s]/td[1]/span' % i).text
	btcClose = driver.find_element(By.XPATH, '//table/tbody/tr[%s]/td[5]/span' % i).text

	csvDictList.append({
		'Date': date,
		'Close': btcClose
	})

	i += 1

writer.writerows(csvDictList)
driver.close()
csvFile.close()
