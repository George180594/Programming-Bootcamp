
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://appbrewery.github.io/Zillow-Clone/'
response = requests.get(url)
response.raise_for_status()
data = response.text
# print(data)  # website all data


# Getting all addresses
add = []
soup = BeautifulSoup(data, "html.parser")
addresses = soup.find_all("address")
for address in addresses:
    format_adress = address.text.replace(" ","").replace("\n","").replace("|"," ")
    add.append(format_adress)
print(add)


#all address link

add_links = soup.select(".StyledPropertyCardDataWrapper a")
link=[li.get('href') for li in add_links]
print(link)


#all rent
add_rents = soup.select(".PropertyCardWrapper span")
rent = [rent.text.replace("/","").replace("mo","").replace("+","") for rent in add_rents]
print(rent)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdOzBAwrDw70AC9zAQtAK9IcbT7Lko7WY4_95jdvaCWSYfs7g/viewform?usp=sf_link")

time.sleep(3)
for index in range(len(add)):
    f_input = driver.find_element(By.CSS_SELECTOR,".Xb9hP input")
    f_input.send_keys(add[index], Keys.TAB, rent[index], Keys.TAB, link[index], Keys.TAB, Keys.SPACE)
    time.sleep(2)
    another_response = driver.find_element(By.CSS_SELECTOR,".c2gzEf a[href]")
    another_response.click()
    time.sleep(4)
    if index == len(rent):
        driver.quit()