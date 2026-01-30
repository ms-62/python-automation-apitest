# Python 가상환경 생성 (권장)
python3 -m venv .venv # Mac <br>
source .venv/bin/activate  # Linux/Mac <br>
또는 venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt

# newman 설치
npm install -g newman

### mac & 외장하드 사용 시 utf-8 에러 발생 시 대응
dot_clean .


### Next Step
- HTTP Method newman test용 추가 작업 - (완료)
- ci/cd 환경에서 api Test 돌릴 수 있게 yml 작업 - (완료)

## Report
### pytest - allure 활용 (local)
### 테스트 실핼 및 데이터 생성 
### --alluredir을 통해 폴더 생성
- python -m pytest --alluredir=allure-results
### 결과 임시 서버로 띄워 브라우저 확인용 명령어
- allure serve allure-results
yml에도 적용 (gihub actions 생성확인) <br>

### test 파일에 데코레이터로 설명 추가
- @allure.feature()
- @allure.story()
- with allure.step():
- allure.dynamic.description()

### local reports 폴더는 .gitingore 추가


