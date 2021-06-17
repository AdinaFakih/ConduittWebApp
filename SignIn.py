from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://react-redux.realworld.io/#/login?_k=kuud5i")
time.sleep(2)

#email  [ Valid , Invalid, Empty, Invalid]
email = ["xor@x.com","xor@2.com", " ", "sd@sd"]
#password  [ Valid , Invalid, Empty, Valid]
password = ["123456789","1234", "", "1234567890"]

for x,y in zip(email,password):
    driver.refresh()
    # goto sign in
    driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[2]/a').click()
    time.sleep(1)
    # Email
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys(x)
    time.sleep(1)
    # Password
    driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys(y)
    time.sleep(1)
    # Click Signin button
    driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/button').click()
    time.sleep(4)
    try:
        if(driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/ul').is_displayed()==True):
            print("Sign In was Unsuccessful")
        else:
            pass
    except:
        time.sleep(2)
        # Settings
        driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[3]/a').click()
        time.sleep(3)
        print("Sign in was successful")
        # scroll to the end of the page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        # Logout
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/button').click()

time.sleep(6)
driver.close()