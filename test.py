from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver import Opera
# from selenium import webdriver

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
        browserInstance = Firefox(executable_path='/mnt/c/WebDriver/bin/geckodriver.exe')
        browserInstance.get('https://marchant.printercloud.com/admin/#')
        return browserInstance
    elif browser == "msedge":
        browserInstance = Edge(executable_path='/mnt/c/WebDriver/bin/msedgedriver.exe')
        browserInstance.get('https://marchant.printercloud.com/admin/#')
        return browserInstance
    elif browser == "opera":
        browserInstance = Opera(executable_path='/mnt/c/WebDriver/bin/operadriver.exe')
        browserInstance.get('https://marchant.printercloud.com/admin/#')
        return browserInstance
    else:
        return -1

def simpleLogin(browser):
    # This function logs in to the PrinterLogic SaaS in a simple manner
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        browserInstance.quit()
        print("Simple login test has been run. TEST #1")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def simpleLoginWithReturn(browser):
    # This function will check username and password using return buttons to switch fields and submit
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        username = browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME + "\n")
        password = browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD + "\n")
        time.sleep(WAIT_PERIOD)
        browserInstance.quit()
        print("Simple login with return test has been run. TEST #2")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False


def noUsername(browser):
    # This function will try logging in without entering a username
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        browserInstance.quit()
        print("No username test has been run. TEST #3")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def noPassword(browser):
    # This function will try logging in without entering a password
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        browserInstance.quit()
        print("No Password test has been run. TEST #4")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def wrongLogin(browser):
    # This function will test bad login information
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys("NotMyPassword")
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        browserInstance.quit()
        print("Wrong login test has been run. TEST #5")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def obnoxiousLoginClicking(browser):
    # This function will click the login button obnoxiously
    try:
        browserInstance = openLogin(browser)
        loginbtn = browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn')
        for i in range(100):
            loginbtn.click()
        browserInstance.quit()
        print("Login button has been clicked obnoxiously. TEST #6")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def forgotPasswordButton(browser):
    # This function will check that the forgot password button works
    try:
        browserInstance = openLogin(browser)
        forgotPass = browserInstance.find_element(By.CSS_SELECTOR, '#forgot-password')
        forgotPass.click()
        browserInstance.quit()
        print("Forgot Password button has been checked. TEST #7")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
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
        browserInstance.quit()
        print("Forgot Password and login screen have been flipped between obnoxiously. TEST #8")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def privacyPolicy(browser):
    # This function will check the privacy policy link
    try:
        browserInstance = openLogin(browser)
        privacyPolicy = browserInstance.find_element(By.XPATH, '//*[@id="privacy-policy-container"]/a[1]')
        privacyPolicy.click()
        time.sleep(WAIT_PERIOD)
        print("Privacy Policy has been clicked. TEST #9")
        browserInstance.quit()
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def failThenLogin(browser):
    try:
        browserInstance = openLogin(browser)
        time.sleep(SHORT_WAIT) 
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys("NotMyPassword")
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        time.sleep(WAIT_PERIOD)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_user').send_keys(USERNAME)
        browserInstance.find_element(By.CSS_SELECTOR, '#relogin_password').send_keys(PASSWORD)
        browserInstance.find_element(By.CSS_SELECTOR, '#admin-login-btn').click()
        browserInstance.quit()
        print("Failed login and relogin test has been run. TEST #10")
        return True
    except:
        try:
            browserInstance.quit()
            return False
        except:
            return False

def checkSuccesses(testOutcomes, browser):
    # This function checks how many of the tests run were successful and will give a small summary
    testsRun = len(testOutcomes)
    successes = 0
    for i in range(len(testOutcomes)):
        if testOutcomes[i] == True:
            successes += 1
        else:
            print("Test number " + str(i + 1) + " failed.")
    print("===========================================================================")
    print(str(successes) + " tests were successful out of the " + str(testsRun) + " tests that were run on the " + browser + " browser.")
    print("===========================================================================")
    # This is used by the overall summary
    if successes == testsRun:
        return True
    else:
        return False

def tests(browser):
    testOutcomes = []
    testOutcomes.append(simpleLogin(browser))
    testOutcomes.append(simpleLoginWithReturn(browser))
    testOutcomes.append(noUsername(browser))
    testOutcomes.append(noPassword(browser))
    testOutcomes.append(wrongLogin(browser))
    testOutcomes.append(obnoxiousLoginClicking(browser))
    testOutcomes.append(forgotPasswordButton(browser))
    testOutcomes.append(forgotPasswordObnoxiousSwitch(browser))
    testOutcomes.append(privacyPolicy(browser))
    testOutcomes.append(failThenLogin(browser))
    return checkSuccesses(testOutcomes, browser)

def main():
    browsers = ["chrome", "firefox", "msedge", "opera"]
    browserSuccesses = []
    for browser in browsers:
        browserOutcome = tests(browser)
        browserSuccesses.append(browserOutcome)
    # This will give a summary of the browser successes
    for j in range(len(browserSuccesses)):
        if browserSuccesses[j] == True:
            print(browsers[j] + " was successfully tested.")
    time.sleep(WAIT_PERIOD)

main()