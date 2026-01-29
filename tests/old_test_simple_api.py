import os
import requests
from dotenv import load_dotenv

# .env 파일에서 설정값 로드 (URL, API 키 등)
load_dotenv()
BASE_URL = "https://jsonplaceholder.typicode.com" # 테스트용 가짜 API 사이트

def test_get_posts_list():
    """사용자 목록 조회 API 테스트"""
    # 1. 요청 보내기
    response = requests.get(f"{BASE_URL}/posts")
    
    # 2. 결과 검증 (Assertion)
    assert response.status_code == 200  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    print(f"\n조회된 게시글 수: {len(response.json())}")

def test_post_posts():
    data = {
    "method": 'POST',
    "body": {
        "title": 'foo12',
        "body": 'bar32',
        "userId": 1,
    },
    "headers": {
        'Content-type': 'application/json; charset=UTF-8',
    }
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    
    assert response.status_code == 201  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    return_data = response.json()
    print(f"\n 등록 글 json: {response.json()}")
    print(f"\n {return_data['body']}")
    print(f"\n title : {return_data['body']['title']}")
    print(f"\n body : {return_data['body']['body']}")
    print(f"\n userId : {return_data['body']['userId']}")
    

def test_patch_post():
    data = {
    "method": 'PATCH',
    "body": {
        "title": '12foo12',
        "body": '34bar32',
    },
    "headers": {
        'Content-type': 'application/json; charset=UTF-8',
    }
    }
    response = requests.patch(f"{BASE_URL}/posts/1", json=data)
    assert response.status_code == 200  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    return_data = response.json()
    print(f"\n 일부 수정한 결과 json: {response.json()}")
    print(f"\n {return_data['body']}")
    print(f"\n title : {return_data['body']['title']}")
    print(f"\n body : {return_data['body']['body']}")

def test_put_post():
    data = {
    "method": 'PATCH',
    "body": {
        "id": '1',
        "title": 'put test',
        "body": 'put test test put',
        "userId": '1'
    },
    "headers": {
        'Content-type': 'application/json; charset=UTF-8',
    }
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=data)
    assert response.status_code == 200  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    return_data = response.json()
    print(f"\n 전체 수정한 결과 json: {response.json()}")
    print(f"\n {return_data['body']}")
    print(f"\n id : {return_data['body']['id']}")
    print(f"\n title : {return_data['body']['title']}")
    print(f"\n body : {return_data['body']['body']}")
    print(f"\n userId : {return_data['body']['userId']}")