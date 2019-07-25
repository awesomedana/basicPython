# seleniumdemo.py
# selenium : Browser Automation Tool
# - java에서도 이용 가능
# 자동으로 DataFrame까지 만들어 줌
# pip install selenium
from selenium import webdriver

# Explicit Wait(명시적 대기) : 특정 element가 로딩할 때까지 대기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# selenium이랑 상관없고 모듈 쓰기
import time

url = "http://tour.interpark.com/"
keyword = '런던'
driver = webdriver.Chrome(executable_path = 'chromedriver.exe')

#WebSite에 연결하기
driver.get(url)

#find_element_by_id().send_keys()
driver.find_element_by_id('SearchGNBText').send_keys(keyword) #검색창에 keyword를 입력
driver.find_element_by_css_selector('button.search-btn').click() #검색버튼을 누르는 것까지 자동화시킨 것

try:
    element = WebDriverWait(driver, 10).until( #10초 내에 발견되면 언제라도 로딩
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
except Exception as err:
    print("오류 발생 : ", err)

# Implicit Wait(암시적 대기) : 시간을 지정해서 시간만큼 대기
driver.implicitly_wait(10) #10초동안 무조건 대기 후 다음 작업 실행(버퍼링에 유리함)

# 해외여행 더보기 클릭 이벤트 처리하기
driver.find_element_by_css_selector('.oTravelBox > .boxList > .moreBtnWrap > .moreBtn').click()

# JavaScript 함수 실행하기 : page 이동시키기
tour_list = []
for page in range(1, 11):
    try:
        driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
        time.sleep(3) #python에서 일정시간 holding할 때(implicit waiting)
        print("%s페이지로 이동" % page)
        # oTravelBox > boxList > boxItem
        boxItems = driver.find_elements_by_css_selector('.panelZone > .oTravelBox > .boxList > li.boxItem')

        for li in boxItems:
            strInfo = '' # 판다스 연결해서 DF만들기용
            for info in li.find_elements_by_css_selector('.proInfo'): #복수일 때는 elements 주의!
                strInfo += info.text + ', '
            mydic = {
                '상품이미지' : li.find_element_by_css_selector('img').get_attribute('src'),
                '상품명' : li.find_element_by_css_selector('h5.proTit').text,
                '부상품명' : li.find_element_by_css_selector('.proSub').text,
                '가격' : li.find_element_by_css_selector('.proPrice').text,
                '나머지정보' : strInfo
            }
            tour_list.append(mydic)
            # TERMINAL 출력용
            # print("상품 이미지", li.find_element_by_css_selector('img').get_attribute('src')) #img태그의 src속성
            # print("상품명 -> ", li.find_element_by_css_selector('h5.proTit').text)
            # print("(부상품명 ->", li.find_element_by_css_selector('.proSub').text, ")")
            # print("가격 :", li.find_element_by_css_selector('.proPrice').text)
            # for info in li.find_elements_by_css_selector('.proInfo'): #복수일 때는 elements 주의!
            #     print(info.text)
            # print("== " * 50)
    except Exception as err1:
        print("오류 발생 : ", err1)

import pandas as pd

df = pd.DataFrame(data = tour_list, columns = ['상품이미지', '상품명', '부상품명', '가격', '나머지정보'])
print(df.head()) #상위 5개만 출력