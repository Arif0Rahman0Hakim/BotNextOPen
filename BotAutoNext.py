import time
from selenium import webdriver
Username = 'RuizTML11@yahoo.com'
Passwd = 'Kalingga69'
komen = 'Hadir'
driver = webdriver.Chrome('/home/arif/Desktop/chromedriver_linux64/chromedriver')
driver.get('https://umkt.ucm.ac.id/courses/networking-infrastruture-management/homepage/')
cih = driver.find_element_by_class_name('top-bar-menu-login-link')
cih.click()
userinput = driver.find_element_by_name('email')
userinput.send_keys(Username)
passinput = driver.find_element_by_xpath('//*[@id="5"]')
passinput.send_keys(Passwd)
tombol = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[3]/div/form/button')
tombol.click()
time.sleep(5)
driver.get('https://umkt.ucm.ac.id/courses/networking-infrastruture-management/i_1/')
while True :
    time.sleep(10)
    nexto = driver.find_element_by_xpath('//*[@id="page-traversal"]/a[2]').click()
//update
