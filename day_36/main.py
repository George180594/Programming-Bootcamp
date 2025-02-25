import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY= "PHQWC624UNGE67O6"
NEWS_API_KEY="501bd6f8a0554838816b349562d739fe"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)

response.raise_for_status()
data = response.json()["Time Series (Daily)"]
print(data)
data_list=[value for (key, value) in data.items()]
yesterday_data= data_list[0]
yesterday_closing_price= yesterday_data['4. close']
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down=None

if difference > 0:
    up_down= "⬆️"
else:
    up_down="⬇️"
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent= round(difference /float(yesterday_closing_price)) *100
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent>1:
    new_params={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
    new_response=requests.get(NEWS_ENDPOINT,params=new_params)
    articles=new_response.json()["articles"]

    

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles= articles[:3]



#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles=[f"{STOCK_NAME}:{up_down}{diff_percent}%\n Headline: {article['title']}. \n\nBrief: {article['description']}" for article in three_articles]

print("\n\n".join(formatted_articles))

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""





