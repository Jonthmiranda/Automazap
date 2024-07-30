#Libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import webbrowser, os
import pyautogui

#Ask to do not touch the computer and keep only the program active,
#after everything is closed, press enter, and type the message that the customer will receive on their Whatsapp
check = input("\n\nWhile this program is running, do not touch the computer!!\nPress enter to contine!\n\n")
msg_client = input("Enter the message the customer will receive: \n\n")

#Open the directory that contains the menus, wait for loading for 2 seconds, change the screen to
#the menu using alt + tab (that's why everything is closed), wait 1 second to be sure,
#select all and copy using PYAUTOGUI
webbrowser.open(os.path.realpath(r".\cardapio")) #cardapio == menu
time.sleep(2)
pyautogui.hotkey('alt', 'tab') #If running in IDE, it is necessary to enable line 21 and 22, otherwise it will be bug
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

#Loading database containing contacts using Panda
contacts_df = pd.read_excel(r"Contatos.xlsx") #contatos == contacts

#Using Selenium, open the navegator in Whastapp Web
browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/")

#Wait for the login with the QRCODE, when the page is fully loaded, it continues
while len(browser.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

#try with Try, if you get it perfect, if not, go to excess and skip the number
#Sending a message using the link, scrolls through the database, organizes the data to be able to use it in a link
#open the link and follow
for i, message in enumerate(contacts_df['Número']): #número == number
    try:
        number = contacts_df.loc[i, "Número"]
        link = f"https://web.whatsapp.com/send?phone={number}&text={msg_client}"
        browser.get(link)
    
        #Waits for the page to load, locating the "side" element in the HTML, once located it waits
        #complete loading of the page for 5 seconds
        while len(browser.find_elements(By.ID, "side")) < 1:
            time.sleep(1) 
        time.sleep(5)   

        #Variable "elem_xpath" contains the XPATH of the element that needs to be located,
        #locate the "text box" element in the HTML using XPATH, and press enter, wait 2 seconds
        #to continue
        elem_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'
        browser.find_element(By.XPATH, f'{elem_xpath}').send_keys(Keys.ENTER)
        time.sleep(2)

        #sending menus that are in the clipboard, waiting 10 seconds to load photos
        #press enter and wait 5 seconds until sending
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(5)
        pyautogui.hotkey('enter')
        time.sleep(5)

    #exception if the phone number is wrong or not located, then send a message saying which number it is
    except NoSuchElementException:
        print("\nThe number ", numero, " did not work!\n")
