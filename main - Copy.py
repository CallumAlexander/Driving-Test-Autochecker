'''
DRIVING TEST AUTOCHECKER by Callum
This script automatically logs in to the DVSA website under my booking and checks
whether there is a earlier test avaiable. It notifies my by sounding an alarm.
It utilizes random wait times in order to eliminate serverside antiscript software (I think). 
Enjoy x
'''
#--- Imports ---
from selenium import webdriver
from time import sleep
from random import randint as rnd
from random import uniform as uni
from playsound import playsound
import numpy as np


#This fuction checks the website for an earlier date and returns the month of
#the earliest booking.
def Check():
    try:
        #running the browser
        driver = webdriver.Chrome(r'path\to\chromewebdriver.exe')
        driver.get('urltobookingwebpage.com')

        #finding the login elements
        LNumber = driver.find_element_by_name('username')
        bookingNumber = driver.find_element_by_id('application-reference-number')
        sleep(Rand(False))
        
        #entering login data
        LNumber.send_keys('Username')
        bookingNumber.send_keys('booking no')
        sleep(Rand(False))

        #logging in
        login_button = driver.find_element_by_name('booking-login')
        login_button.click()
        sleep(Rand(False))

        #find and click 'change' button
        changeButton = driver.find_element_by_id('date-time-change')
        changeButton.click()
        sleep(Rand(False))

        #find and click 'show earliest available date' radio button
        earliestButton = driver.find_element_by_id('test-choice-earliest')
        earliestButton.click()
        sleep(Rand(False))

        #find and click 'continue' button
        conButton = driver.find_element_by_id('driving-licence-submit')
        conButton.click()
        sleep(Rand(False))

        #find the month tag and text
        monthTag = driver.find_element_by_class_name('BookingCalendar-currentMonth')
        month = monthTag.text

        sleep(Rand(False))
        driver.close()
        
        return month
    
    except:
        print('Error occured')


#This function generates suitable wait times before the fuction continues with
#the checking. - Combats serverside antiscript protection
def Rand(boolean):

    if boolean == True:
        #seconds = rnd(427, 604)
        seconds = round(np.random.normal(loc = 60*15+9, scale = 64))
    else:
        seconds = round(uni(0.4, 3.1), 2)
        
    return seconds


#--- Main Loop ---
counter = 0
while True:
    date = Check()
    counter += 1
    if date == 'January':
        print('date in January')
        while True:
            playsound('foghorn-daniel_simon.mp3')
        break
            
    elif date == 'February':
        print('date in February')
        while True:
            playsound('foghorn-daniel_simon.mp3')
        break
    
    else:
        seconds = Rand(True)
        conv = round(seconds / 60, 2)
        print('attempt ', str(counter), ' - no change, ', date, ' - next check : ', str(conv), ' minutes')
        
        
    date = ''
    sleep(seconds)

