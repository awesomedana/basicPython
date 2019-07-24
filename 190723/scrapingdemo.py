#scrappingdemo.py 

import pandas as pd
import requests
from bs4 import BeautifulSoup
import pprint

url='http://movie.naver.com/movie/point/af/list.nhn?&page='
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')
movie_list = []
point_list = []
review_list = []
#print(soup.find_all('a', class_ = 'movie'))

# for movie in soup.find_all('a', class_='movie'):
#     print(movie.text)

for page in range(1, 101):
    url = url + str(page)
    print(url)
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    for movie in soup.find_all('a', class_='movie'):
        movie_list.append(movie.text)

    for point in soup.find_all('td', class_='point'):
        point_list.append(point.text)

    for review in soup.find_all('td', class_='title'):
        review = review.text.strip()
        review = review.replace('\t', '')
        review = review.replace('\n', '')
        review = review.replace('신고', '')
        review_list.append(review)
    
    url = url.split('=')[0] + '='

df = pd.DataFrame(date = movie_list, columns = ['Movie'])
df['Point'] = point_list
df['Review'] = review_list
print(df.info())
