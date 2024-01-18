import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import xlsxwriter

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options = option)

url = "https://www.ss.lv/"
driver.get(url)
time.sleep(0.5)

find1 = driver.find_element(By.ID, "mtd_59")
find1.click()

time.sleep(0.5)

find2 = driver.find_element(By.LINK_TEXT, "Rīga")
find2.click()

time.sleep(0.5)

find3 = driver.find_element(By.LINK_TEXT, "Vecrīga")
find3.click()

time.sleep(2)

find4 = driver.find_element(By.CLASS_NAME, "filter_txt")
find4.send_keys("250")

find5 = driver.find_element(By.ID, "f_o_8_max")
find5.send_keys("600")

find6 = driver.find_element(By.ID, "f_o_4_min")
find6.send_keys("2")

meklet = driver.find_element(By.CLASS_NAME, "b")
meklet.click()

time.sleep(2)

ids = []
for row in driver.find_elements(By.XPATH,'//table[@id="page_main"]//tr'):
    ids.append(row.get_attribute('id'))

while("" in ids):
    ids.remove("")

ids.pop(0)
ele = ids.pop()

dzivokli = []
for id in ids:
    find = driver.find_element(By.ID, id)
    find.click()
    time.sleep(1)
    cena = driver.find_element(By.ID, "tdo_8").text
    atrasanas = driver.find_element(By.ID, "tdo_11").text
    x = atrasanas.split()
    iela = x[0] + " " + x[1]
    platiba = driver.find_element(By.ID, "tdo_3").text
    istabas = driver.find_element(By.ID, "tdo_1").text
    stavs = driver.find_element(By.ID, "tdo_4").text
    # epasts = driver.find_element(By.NAME, "send-mail")
    # epasts.click()
    # time.sleep(3)
    # ievaditepasts = driver.find_element(By.NAME, "mmail")
    # ievaditepasts.send_keys("vards.uzvards@gmail.com")
    # ievaditvards = driver.find_element(By.NAME, "mname")
    # ievaditvards.send_keys("Kate Vasiļjeva")
    # ievaditnumurs = driver.find_element(By.NAME, "mphone")
    # ievaditnumurs.send_keys("29123456")
    # ievaditteksts = driver.find_element(By.NAME, "mtxt")
    # ievaditteksts.send_keys("Labdien!\nVai būtu iespējams apskatīt dzīvokli?\nAr cieņu,\nKate Vasiļjeva")
    time.sleep(2)

    info = []
    info.append(cena)
    info.append(iela)
    info.append(platiba)
    info.append(istabas)
    info.append(stavs)
    dzivokli.append(info)

    find2 = driver.find_element(By.LINK_TEXT, "Atgriezties uz sludinājumu sarakstu")
    find2.click()
    time.sleep(1)

dz1 = [0, 1, 2, 3, 4]
dz2 = [5, 6, 7, 8, 9]
dzivokli_tuple = dz1, dz2
for dzivoklis in dzivokli:
    dzivokli_tuple += (dzivoklis,)

print(dzivokli_tuple)


workbook = xlsxwriter.Workbook('dzivokliprojekts.xlsx')
worksheet = workbook.add_worksheet("dzivokli Vecriga")

worksheet.write('A1', 'Cena')
worksheet.write('B1', 'Iela')
worksheet.write('C1', 'Platiba')
worksheet.write('D1', 'Istabas')
worksheet.write('E1', 'Stavs')


row = 1
col = 0
for cena, iela, platiba, istabas, stavs in (dzivokli_tuple):
    worksheet.write(row, col, cena)
    worksheet.write(row, col + 1, iela)
    worksheet.write(row, col + 2, platiba)
    worksheet.write(row, col + 3, istabas)
    worksheet.write(row, col + 4, stavs)

    row += 1

for row in range(1, 3):
   worksheet.set_row(row, None, None, {'hidden':1})

workbook.close()

input()