from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

dev = webdriver.Chrome()
dev.get("https://web.whatsapp.com/")
sleep(5)
input("inter.....")

name = input("name terget >>>  ")
piyam = input("matn >>>   ")
tedad = int(input("tedad... >>>  "))

dev.find_element_by_xpath("//span[@title ='{}']".format(name)).click()
dev.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]").click()

for i in range(tedad):
    

    dev.find_element_by_css_selector(".DuUXI  ._1awRl").send_keys(piyam , i)
    
    dev.find_element_by_css_selector(".DuUXI  ._1awRl").send_keys(Keys.ENTER)



