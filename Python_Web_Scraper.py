# Importing Required Modules
import requests
from bs4 import BeautifulSoup

# Taking article URL
url = 'https://www.dawn.com/news/1766926/discovering-iran-the-land-of-islamic-history'

# Requesting the given url for page
res = requests.get(url)

# Making a BeautifulSoup object
soup = BeautifulSoup(res.text, 'html.parser')

# Scraping data
article_tag = soup.find('article', class_='story')

# article title
title_tag = article_tag.find('h2', class_='story__title')

# Article content
content_tag = article_tag.find('div', class_='story__content')

# Extracting text from all paragraph tags in content_tag
paragraph_strings = [p.text for p in content_tag.find_all('p', recursive=False)] # list of paragraphs text

# Final output
article = {
    'title': title,
    'content': paragraph_strings
}

print('\n'+'-'*15)
print(f"Article Title: {article['title']} \n")
print("Content: ------------------\n")
print(*article['content'], sep='\n')
