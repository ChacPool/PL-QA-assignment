from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "TestingUser"
PASSWORD = "Te$+1ng!"
WAIT_PERIOD = 2
SHORT_WAIT = WAIT_PERIOD * 0.25
LONG_WAIT = WAIT_PERIOD * 2

# Waiting is used to give a human user the ability to make a visual check that the script is running correctly 


def openLogin():
    # This function creates and opens an instance of the Chrome driver to work on.
    browserInstance = Chrome('/mnt/c/WebDriver/bin/chromedriver.exe')
    browserInstance.get('https://marchant.printercloud.com/admin/#')
    return browserInstance

def simpleLoginWithReturn():
    # This function will check username and password using return buttons to switch fields and submit
    try:
        browserInstance = openLogin()
        time.sleep(SHORT_WAIT) 
        username = browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME + "\n")
        password = browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD + "\n")
        print("Simple login with return test has been run.")
        time.sleep(WAIT_PERIOD) 
        return True
    except:
        browserInstance.quit()
        return False

def simpleLogin():
    # This function logs in to the PrinterLogic SaaS in a simple manner
    try:
        browserInstance = openLogin()
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        print("Simple login test has been run.")
        return True
    except:
        browserInstance.quit()
        return False

def noUsername(browserInstance):
    # This function will try logging in without entering a username
    try:
        browserInstance = openLogin()
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        print("No Username test has been run.")
        return True
    except:
        browserInstance.quit()
        return False

def noPassword(browserInstance):
    # This function will try logging in without entering a password
    return

def obnoxiousClicking(browserInstance):
    # This function will click the login button obnoxiously
    browserInstance = openLogin()
    loginbtn = browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn')
    for i in range(10):
        loginbtn.click()



def main():
    simpleLogin()
    simpleLoginWithReturn()
    
    time.sleep(WAIT_PERIOD)

main()
    



### FROM A TUTORIAL

# driver = Chrome('/mnt/c/WebDriver/bin/chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()