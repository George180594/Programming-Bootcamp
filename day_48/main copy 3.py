from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#Keep Chorome open
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# driver.set_window_size(1920, 1080)
first_name= driver.find_element(By.NAME, value="fName")
first_name.send_keys("George")

last_name= driver.find_element(By.NAME, value="lName")
last_name.send_keys("Rezende")

email= driver.find_element(By.NAME, value="email")
email.send_keys("george180594@gmail.com",Keys.ENTER)

#OR could be
# submit=driver.find_element(By.CSS_SELECTOR,value="form button")
# submit.click()



# driver.quit()

