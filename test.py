from selenium.webdriver import Chrome
from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

USERNAME = "TestingUser"
PASSWORD = "Te$+1ng!"
WAIT_PERIOD = 2
SHORT_WAIT = WAIT_PERIOD * 0.25
LONG_WAIT = WAIT_PERIOD * 2
# export PATH="$PATH:/mnt/c/WebDriver/bin/geckodriver.exe"

# Waiting is used to give a human user the ability to make a visual check that the script is running correctly 

def openLogin(browser):
    # This function creates and opens an instance of the Chrome driver to work on.
    if browser == "chrome":
        browserInstance = Chrome('/mnt/c/WebDriver/bin/chromedriver.exe')
        browserInstance.get('https://marchant.printercloud.com/admin/#')
        return browserInstance
    elif browser == "firefox":
        # '/mnt/c/WebDriver/bin/geckodriver.exe'
        browserInstance = Firefox(executable_path='C:/WebDriver/bin/geckodriver.exe')
        # browserInstance = Firefox('/mnt/c/WebDriver/bin/geckodriver.exe')
        print(browserInstance.title)
        browserInstance.get('https://marchant.printercloud.com/admin/#')
        return browserInstance
    else:
        return -1

def simpleLoginWithReturn(browser):
    # This function will check username and password using return buttons to switch fields and submit
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        username = browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME + "\n")
        password = browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD + "\n")
        print("Simple login with return test has been run.")
        time.sleep(WAIT_PERIOD)
        browserInstance.quit()
        return True
    except:
        browserInstance.quit()
        return False

def simpleLogin(browser):
    # This function logs in to the PrinterLogic SaaS in a simple manner
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        print("Simple login test has been run.")
        browserInstance.quit()
        return True
    except:
        # browserInstance.quit()
        return False

def noUsername(browser):
    # This function will try logging in without entering a username
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        print("Incorrect login test has been run.")
        browserInstance.quit()
        return True
    except:
        browserInstance.quit()
        return False

def noPassword(browser):
    # This function will try logging in without entering a password
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        print("No Password test has been run.")
        browserInstance.quit()
        return True
    except:
        browserInstance.quit()
        return False

def wrongLogin(browser):
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys("NotMyPassword")
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        print("Simple login test has been run.")
        browserInstance.quit()
        return True
    except:
        browserInstance.quit()
        return False

def obnoxiousLoginClicking(browser):
    # This function will click the login button obnoxiously
    try:
        browserInstance = openLogin(browser)
        loginbtn = browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn')
        for i in range(100):
            loginbtn.click()
        print("Login button has been clicked obnoxiously.")
        browserInstance.quit()
        return True
    except:
        browserInstance.quit()
        return False

def forgotPasswordButton(browser):
    # This function will check that the forgot password button works
    try:
        browserInstance = openLogin(browser)
        forgotPass = browserInstance.find_element(By.CSS_SELECTOR, '#forgot-password')
        forgotPass.click()
        print("Forgot Password button has been checked.")
        browserInstance.quit()
        return True
    except:
        browserInstance.quit()
        return False

def forgotPasswordObnoxiousSwitch(browser):
    # This function will switch between the login and forgot password screen repeatedly.
    try:
        browserInstance = openLogin(browser)
        for i in range(5):
            forgotPass = browserInstance.find_element(By.CSS_SELECTOR, '#forgot-password')
            forgotPass.click()
            cancelBtn = browserInstance.find_element(By.XPATH, '//*[@class="ui-dialog-buttonset"]/button[2]')
            cancelBtn.click()
        print("Forgot Password and login screen have been flipped between obnoxiously.")
        browserInstance.quit()
        return True
    except:
        browserInstance.quit()
        return False

def chromeTests():
    browser = "chrome"
    testOutcomes = []
    testOutcomes.append(simpleLogin(browser))
    testOutcomes.append(simpleLoginWithReturn(browser))
    testOutcomes.append(noUsername(browser))
    testOutcomes.append(noPassword(browser))
    testOutcomes.append(wrongLogin(browser))
    testOutcomes.append(obnoxiousLoginClicking(browser))
    testOutcomes.append(forgotPasswordButton(browser))
    testOutcomes.append(forgotPasswordObnoxiousSwitch(browser))
    checkSuccesses(testOutcomes, browser)

def firefoxTests():
    browser = "firefox"
    testOutcomes = []
    testOutcomes.append(simpleLogin(browser))
    # testOutcomes.append(simpleLoginWithReturn(browser))
    # testOutcomes.append(noUsername(browser))
    # testOutcomes.append(noPassword(browser))
    # testOutcomes.append(wrongLogin(browser))
    # testOutcomes.append(obnoxiousLoginClicking(browser))
    # testOutcomes.append(forgotPasswordButton(browser))
    # testOutcomes.append(forgotPasswordObnoxiousSwitch(browser))
    checkSuccesses(testOutcomes, browser)

def checkSuccesses(testOutcomes, browser):
    # This function checks how many of the tests run were successful
    testsRun = len(testOutcomes)
    successes = 0
    for test in testOutcomes:
        if test == True:
            successes += 1
    print(str(successes) + " tests were successful out of the " + str(testsRun) + " tests that were run on the " + browser + " browser.")

def main():
    chromeTests()
    # firefoxTests()
    time.sleep(WAIT_PERIOD)

main()