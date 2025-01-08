from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chorome open
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ie=UTF8&useRedirectOnSuccess=1&ref_=dex_glow_signin&path=%2Fdp%2FB075CYMYK6%3Fpsc%3D1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")



# price_dollar=driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents=driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")


# search_bar=driver.find_element(By.NAME,value="q")
# # print(search_bar.tag_name)
# # print(search_bar.get_attribute("placeholder"))
# button=driver.find_element(By.ID,value="submit")
# # print(button.size)
# documentation_link=driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)


#so much easy find a element using XPATH
# submit_botton=driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_botton.text)

######################## CHALLENG ##############~


date_element=driver.find_elements(By.CSS_SELECTOR, value="div.medium-widget.event-widget time")
title_element=driver.find_elements(By.CSS_SELECTOR, value="div.medium-widget.event-widget li a")

title_list=[title.text for title in title_element]
date_list=[element.text for element in date_element]

events={}

for n in range(len(title_list)):
    events[n] = {
        "time":date_list[n] ,
        "name":title_list[n],
    }

# events = {n: {"time": date_list[n], "name": title_list[n]} for n in range(len(title_list))}

print(events)

import time
time.sleep(3)
lenguage_botton=driver.find_element(By.ID,value="langSelect-PT-BR")
lenguage_botton.click()











driver.quit()
# driver.close() close  a spefic tab
# driver.quit() all program
