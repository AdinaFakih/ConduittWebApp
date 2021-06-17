from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://react-redux.realworld.io/#/login?_k=kuud5i")
time.sleep(2)

#Verifying the functionality of Sign In Page
time.sleep(2)
#Email
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("xor@x.com")
time.sleep(2)
#Password
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("12345678")
time.sleep(2)
#Click Signin button
driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/button').click()
time.sleep(4)
# Click New_Post
driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[2]/a').click()
time.sleep(2)
for i in range(1,11):
    time.sleep(2)
    # Article Title
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys("Automation")
    time.sleep(2)
    # What's this article about?
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys("It is about testing")
    time.sleep(2)
    # Write your article(in markdown)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[3]/textarea').send_keys("lalallaalallal")
    time.sleep(1)
    # Enter tags
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[4]/input').send_keys("test")
    time.sleep(1)
    # Verify "Publish Article" button
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/button').click()
    time.sleep(3)
    #Goto New Post to Publish again
    driver.find_element_by_xpath("/html/body/div/div/nav/div/ul/li[2]/a").click()


time.sleep(8)
driver.close()