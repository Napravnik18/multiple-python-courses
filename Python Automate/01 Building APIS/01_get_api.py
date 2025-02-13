# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests

r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2024-10-21&sortBy=publishedAt&apiKey=08b86e90a495455a8de51902acd46e76')
content = r.json()
print(content['articles'][0]['title'])