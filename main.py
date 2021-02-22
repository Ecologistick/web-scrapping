import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'технология']


def is_part_in_list(line):
    for word in KEYWORDS:
        if word.lower() in line.lower():
            return True
    return False


page = requests.get("https://habr.com/ru/all/")
soup = BeautifulSoup(page.text, 'html.parser')


for posts in soup.find_all('article'):
  for item in posts.find_all("div", class_ = "post__text"):
    text = item.contents[1].text
    if(is_part_in_list(text)):
      item = posts.find("h2", class_ = 'post__title')
      link = item.contents[1].attrs["href"]
      header = item.contents[1].text
      item = posts.find("span", class_ = 'post__time')
      data = item.text
      print(data + ' - ' + header + ' - ' + link)
