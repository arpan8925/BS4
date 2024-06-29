import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
content = response.text
soup = BeautifulSoup(content, "html.parser")
articles = soup.find_all(name="span", class_="titleline")





article_title = [title.find("a").getText() for title in articles]

article_link = [link.find("a").get("href") for link in articles]

article_score = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

largest_score = max(article_score)
largest_score_index = article_score.index(largest_score)


print(article_title[largest_score_index])
print(article_link[largest_score_index])
print(article_score[largest_score_index])



