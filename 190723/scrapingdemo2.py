#scrapingdemo2.py
import xml.etree.ElementTree as ET
import requests

url='http://rss.etnews.com/Section901.xml' #전자신문 - 오늘의 뉴스
xml_doc = requests.get(url)

#print(xml_doc.text) -> Crawling

#동적으로 웹페이지를 가져오는 것 -> 셀레니움(java에서도 쓴다.)
#셀레니움 : 웹페이지의 자동화툴