# Python 가상환경 생성 (권장)
python3 -m venv .venv # Mac
source .venv/bin/activate  # Linux/Mac
# 또는 venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt

# mac & 외장하드 사용 시 utf-8 에러 발생 시 대응
dot_clean .

# newman 설치
npm install -g newman