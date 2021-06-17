from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

#Browser compatibility
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://react-redux.realworld.io/#/login?_k=kuud5i")
#print(driver.title)
time.sleep(2)

# #Browser compatibility
# driver = webdriver.Firefox(executable_path="C:\webdriver\geckodriver.exe")
# driver.maximize_window()
# driver.get("https://react-redux.realworld.io/#/login?_k=kuud5i")
# #print title of the page
# print(driver.title)
# time.sleep(2)
#Redirect to SignUp page
driver.find_element_by_link_text("Need an account?").click()
time.sleep(2)
#SignUp Page
#Positive test case
#Username
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("Xordd123423232356")
time.sleep(1)
#Email
driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("xor@xd3434422d.com")
time.sleep(1)
#Password
driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/fieldset[3]/input').send_keys("12345678")
time.sleep(1)
#click Signin button
driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/button').click()
time.sleep(2)
# #goto settings and logout
# # Settings
# driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[3]/a').click()
# time.sleep(3)
# # scroll to the end of the page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# # Logout
# driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/button').click()

# #Negative test case for Sign Up
# #Username
# driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("Xor")
# time.sleep(1)
# #Email
# driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("xor@x.com")
# time.sleep(1)
# #Password
# driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/fieldset[3]/input').send_keys("12345678")
# time.sleep(1)
# #click Signin button
# driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/button').click()
# time.sleep(2)

# #Verifying "Have an account functionality"
# driver.find_element_by_link_text('Have an account?').click()
# #Verifying the functionality of Sign In Page
# time.sleep(1)
# #Email
# driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[1]/input").send_keys("xor@x.com")
# time.sleep(1)
# #Password
# driver.find_element_by_xpath("//*[@id='main']/div/div/div/div/div/form/fieldset/fieldset[2]/input").send_keys("12345678")
# time.sleep(1)
# #Click Signin button
# driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/form/fieldset/button').click()
#
#Hover On to verify Link Colour change functionality
time.sleep(2)
Settings = driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[3]/a')
time.sleep(2)
New_Post = driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[2]/a')
time.sleep(2)
Profile_Name = driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[4]/a')

actions = ActionChains(driver)
actions.move_to_element(Settings).move_to_element(New_Post).move_to_element(Profile_Name).click().perform()
time.sleep(2)
#MouseHover on Home page
act = ActionChains(driver)
Home = driver.find_element_by_xpath('//*[@id="main"]/div/nav/div/ul/li[1]/a')
act.move_to_element(Home).click().perform()
time.sleep(6)

#Verify the functionality of Global Feed
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/div[1]/ul/li[2]/a').click()
time.sleep(2)
#Veritying the functionality of Popular Tags Box (test)
driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div[2]/div/div/a[18]').click()
time.sleep(2)
#Verify favorite button functionality when clicked first time
if (driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button/i').is_selected()):
    print("Article already selected as Favorite")
else:
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/button/i').click()

# scroll to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#Verity index button functionality
for i in range(1,6):
    time.sleep(5)
    driver.find_element_by_xpath(f"/html/body/div/div/div/div/div/div[1]/div[2]/nav/ul/li[{i}]/a").click()
time.sleep(2)
#Goto Profile page
#scroll till element is visible
flag = driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[4]/a')
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(3)
#Click Profile page
driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[4]/a').click()

# time.sleep(3)
# #Open Article
# driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div[1]/a/h1').click()
# time.sleep(3)
# #Verify that after clicking on "Edit Article" it redirects to edit article page
# driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/span/a').click()

time.sleep(9)
#Close browser
driver.close()