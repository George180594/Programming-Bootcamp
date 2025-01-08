import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

#Price on site
# URL= "https://appbrewery.github.io/instant_pot/"
URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ie=UTF8&useRedirectOnSuccess=1&ref_=dex_glow_signin&path=%2Fdp%2FB075CYMYK6%3Fpsc%3D1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
BUY_PRICE=200
headers={
  
    "upgrade-insecure-requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site":"cross-site",
    "sec-fetch-mode":"navigate",
    "sec-fetch-user":"?1",
    "sec-fetch-dest":"document",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "priority":"u=0, i",
    "x-forwarded-proto":"https",
    "x-https":"on",
    "X-Forwarded-For":"189.6.9.255",
}

response= requests.get(url=URL,headers=headers)
web_html=response.text
soup=BeautifulSoup(web_html,"html.parser")
price_tag=soup.find(class_="aok-offscreen")
price=price_tag.text.split("$")[1]
price_float=float(price)



#sending a email:

title=soup.find(id="productTitle").text.strip()
print(title)

if price_float < BUY_PRICE:
    message=f'{title} is on sale {price_float}'
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result= connection.login(os.environ["MY_EMAIL"],os.environ["KEY_EMAIL"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subjective: Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )



