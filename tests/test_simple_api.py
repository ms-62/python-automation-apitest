import allure
import pytest


def test_get_posts_list(api):
    response = api.get_post()
    
    assert response.status_code == 200  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    print(f"\n조회된 게시글 수: {len(response.json())}")

def test_get_post_list(api):
    response = api.get_post(2)
    assert response.status_code == 200  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    print(f"\n 특정 사용자의 조회된 게시글 수: {len(response.json())}")
    
@allure.feature("게시글 관리")
@allure.story("게시글 생성 테스트")
def test_create_post_success(api): 
    payload = {
        "body": {
            "title": 'foo12',
            "body": 'bar32',
            "userId": 1
        }
    }
    with allure.step("1. 게시글 데이터를 준비하고 전송합니다."):
        response = api.create_post(payload)
    
    with allure.step("2. 응답 상태 코드가 201인지 확인합니다."):    
        assert response.status_code == 201  # 성공했는지 확인
        assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
        return_data = response.json()
        print(f"\n 등록 글 json: {response.json()}")
        print(f"\n {return_data['body']}")
        print(f"\n title : {return_data['body']['title']}")
        print(f"\n body : {return_data['body']['body']}")
        print(f"\n userId : {return_data['body']['userId']}")
    allure.dynamic.description("이 테스트는 게시글이 정상적으로 생성되는지 확인하는 시나리오입니다.")

def test_patch_post_success(api):
    data = {
        "body": {
            "title": '12foo12'
        }
    }
    response = api.patch_post(1,data)
    assert response.status_code == 200  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    return_data = response.json()
    print(f"\n 일부 수정한 결과 json: {response.json()}")
    print(f"\n {return_data['body']}")
    print(f"\n title : {return_data['body']['title']}")

def test_put_post_success(api):
    data = {
    "body": {
        "id": '1',
        "title": 'put test',
        "body": 'put test test put',
        "userId": '1'
    }
    }
    response = api.put_post(1,data)
    assert response.status_code == 200  # 성공했는지 확인
    assert len(response.json()) > 0    # 데이터가 비어있지 않은지 확인
    return_data = response.json()
    print(f"\n 전체 수정한 결과 json: {response.json()}")
    print(f"\n {return_data['body']}")
    print(f"\n id : {return_data['body']['id']}")
    print(f"\n title : {return_data['body']['title']}")
    print(f"\n body : {return_data['body']['body']}")
    print(f"\n userId : {return_data['body']['userId']}")