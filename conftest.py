import pytest
from core.api.api_client import SimpleApiClient
import os

from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """환경 변수에서 BASE_URL을 가져오는 Fixture"""
    url = os.getenv("BASE_URL")
    if not url:
        # 에러 방지를 위해 기본값을 주거나 예외를 발생시킵니다.
        raise ValueError("BASE_URL이 .env 파일에 설정되지 않았습니다.")
    return url

@pytest.fixture(scope="session")
def api(base_url):
    """
    모든 테스트에서 공통으로 사용할 API 클라이언트 객체
    scope="session"은 테스트가 다 끝날 때까지 이 객체를 딱 하나만 만들어 재사용한다
    """
    client = SimpleApiClient(base_url)
    return client