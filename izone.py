#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime,localtime
import random
import pyautogui
import telegram

telegram_token = "XXXXX"
telegram_chat_id = "XXXXX"

bot = telegram.Bot(token = telegram_token)

def getTime():
    hourNow = strftime("%H", localtime())
    return int(hourNow)

def randomTemp():
    if (getTime() < 12):
        temp = random.uniform(35.3, 36.1)
    elif (getTime() >= 12):
        temp = random.uniform(36.0, 36.9)

    temp = "{:.1f}".format(temp)
    return temp


fileRead = open("/home/pi/Scripts/credentials.txt", "r")

credentials = fileRead.readlines()

credentialsList = []

for i in credentials:
    credentialsList.append(i)

fileRead.close()

tempResults = ""

for i in range(len(credentialsList)):
    credList = []
    credList = credentialsList[i].replace("\n", "").split(',')
    your_username = credList[0]
    your_password = credList[1]
    your_name = credList[2]

    temp = randomTemp()
    if (i == 0):
        tempResults += "-"*5 + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "-"*5 + "\n"

    tempResults += your_name + " - " + str(temp) + "\n"

    if (i == (len(credentialsList) - 1)):
        tempResults += "-"*30 + "\n"

    #Path of chromedriver
    chromedriver_path = '/usr/lib/chromium-browser/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.implicitly_wait(120)

    #Enter WEBSITE to visit
    driver.get('https://i-zone.mobi/companion')

    username = driver.find_element_by_name('WebPatterns_wt17$block$wtUsername$wtUserNameInput')
    username.send_keys(your_username)
    password = driver.find_element_by_name('WebPatterns_wt17$block$wtPassword$wtPasswordInput')
    password.send_keys(your_password)

    button_login = driver.find_element_by_name('WebPatterns_wt17$block$wtAction$wtLoginButton')
    button_login.click()

    uap = driver.find_element_by_id('wt11_wtMainContent_WebPatterns_wt7_block_wtContent_wt13')
    uap.click()

    #Temperature is generated by a function() and typed into box
    temperature = driver.find_element_by_name('Comp_Common_UI_wt39$block$wtMainContent$WebPatterns_wt32$block$wtActions$wtTempTaking_Temp')
    temperature.send_keys(temp)

    submitTemp = driver.find_element_by_name('Comp_Common_UI_wt39$block$wtMainContent$WebPatterns_wt32$block$wtActions$wtTempSubmit')
    submitTemp.click()

    sleep(9)

    #Uses PyAutoGUI to click on confirmation
    pyautogui.click(500, 500)

    sleep(9)

    driver.quit()

bot.send_message(chat_id = telegram_chat_id, text = tempResults)
