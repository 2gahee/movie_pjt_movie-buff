from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome 드라이버 경로 설정 : Chrome update needed
service = Service('./chromedriver.exe')

# ChromeOptions 설정 (선택 사항)
chrome_options = Options()
chrome_options.add_argument('--headless')  # 헤드리스 모드 (브라우저 창 없이 실행)

# 웹 드라이버 실행
driver = webdriver.Chrome(service=service, options=chrome_options)

# 페이지 접속
driver.get('https://megabox.co.kr/on/oh/ohe/Event/selectGoodsStockPrco.do')

# 페이지가 로드될 때까지 기다림
time.sleep(3)

# 이후의 코드 계속...


# 각 지역의 버튼을 찾아 클릭
area_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.btn')

# 지역별로 버튼 클릭 후 지점 정보 가져오기
for button in area_buttons:
    area_name = button.text  # 지역 이름 (예: 서울, 경기 등)
    print(f'지역: {area_name}')
    
    # 버튼 클릭하여 해당 지역의 정보 로딩
    button.click()
    time.sleep(2)  # 데이터가 로드될 때까지 잠시 대기
    
    # 해당 지역의 지점 정보 추출
    branches = driver.find_elements(By.CSS_SELECTOR, 'li.brch')
    for branch in branches:
        branch_name = branch.find_element(By.TAG_NAME, 'a').text  # 지점 이름
        stock_status = branch.find_element(By.CLASS_NAME, 'act').text  # 보유 상태
        print(f"  지점: {branch_name}, 상태: {stock_status}")
    
    print('-' * 50)  # 구분선

# Selenium 종료
driver.quit()
