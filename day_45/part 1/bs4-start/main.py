from bs4 import BeautifulSoup
import requests

response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page=response.text
soup= BeautifulSoup(yc_web_page, "html.parser")
article_tag=soup.find(name="a",class_="storylink")
article_text=article_tag.getText()
article_link=article_tag.get("href")
article_upvote=soup.find(name="span",class_="score").getText()
# print(article_tag)
# print(article_text)
# print(article_link)
# print(article_upvote)
article_texts=[]
article_links=[]
tag_a=soup.find_all(name="a",class_="storylink")
for title in tag_a:
    article_txt=title.getText()
    article_texts.append(article_text)
    article_lnk=title.get("href")
    article_links.append(article_lnk)
score_text=soup.find_all(name="span",class_="score")
article_upvotes=[int(score.getText().split()[0]) for score in score_text]
largest_number=max(article_upvotes)
largest_index=article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])


# print(largest_number)

# print(article_links)
# print(article_texts)
# print(article_upvotes)
























# import lxml

# with open("day_45/part 1/bs4-start/website.html") as file:
#     contents=file.read()


# soup= BeautifulSoup(contents, "html.parser")
# soup= BeautifulSoup(contents, "lxml")

# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)

# all_anchor_tags=soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag)
#     print(tag.get("href"))

# heading=soup.find(name="h1", id="name")
# print(heading)


# section_heading= soup.find(name="h3",class_="heading")
# print(section_heading.get("class"))
# print(section_heading.getText())
# print(section_heading.name)

# company_url= soup.select_one(selector="p a")
# print(company_url)

# company_url= soup.select_one(selector="#name")
# print(company_url)

# company_url= soup.select(selector=".heading")
# print(company_url)
