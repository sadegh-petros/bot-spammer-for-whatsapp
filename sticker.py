from selenium import webdriver
from time import sleep
import os
os.system('cls' or 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'


dev = webdriver.Chrome()
dev.get("https://web.whatsapp.com/")
sleep(5)
def spamer():
    print(color.GREEN + "[0]" + color.WHITE + " create by " + color.RED + "SADEGH.PETROS \n")

    input("ENTER .....")

    name = input("name terget >>>  ")
    sticker = int(input("adade sticker >>>  "))
    tedad = int(input("tedad... >>>  "))
    sleep(2)
    dev.find_element_by_xpath("//span[@title ='{}']".format(name)).click()
    sleep(3)
    dev.find_element_by_xpath("//span[@data-icon='smiley']").click()
    sleep(3)
    dev.find_element_by_xpath("//span[@data-icon='sticker']").click()
    sleep(3)
    input(color.GREEN + "ENTER TO START..... ")
    for i in range(tedad):
        dev.find_elements_by_class_name("_2YpcJ")[sticker].click()
        print(i)

    print(color.RED + "'FINISHED'\n") 
a = 10
while a < 1000 :
    spamer()