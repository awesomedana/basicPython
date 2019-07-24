#scrapingdemo1.py
#pip install lxml -> 외장모듈. 홈페이지 https://lxml.de/   BeautifulSoup보다 더 빠르다고 함
#pip install cssselect -> 이미 설치되어 있네

from urllib.request import urlopen
from urllib.error import HTTPError

def download(url):
    print('Downloading : ', url)
    try:
        html = urlopen(url).read().decode('utf-8')
    except HTTPError as err:
        print('Error :', err.reason)
        html = None
    return html

html = download('http://www.hanbit.co.kr/media/')  #여기까지는 Crawling
import lxml.html  #Parser -> BeautifulSoup의 'html.parser'

etree = lxml.html.fromstring(html)  #url에서 Parsing(파싱하면 tree구조가 만들어진다.)

# print(etree.cssselect('a'))
for atag in etree.cssselect('a'):
    print(atag.get('href'), atag.text) #a 태그 속성이 href의 값 중 text값 가져오기 