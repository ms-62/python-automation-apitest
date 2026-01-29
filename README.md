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
- HTTP Method newman test용 추가 작업
- ci/cd 환경에서 api Test 돌릴 수 있게 yml 작업