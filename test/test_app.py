import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. 수정된 프로필 테스트 (Interest와 Bio를 각각 테스트)
def test_update_profile_bio(client):
    """독립된 버튼 로직에 맞춘 프로필 업데이트 테스트"""
    
    # Interest 업데이트 테스트 (action 추가)
    response = client.post('/profile', 
                           data={'interest': 'Quantum Algorithms', 'action': 'update_interest'}, 
                           follow_redirects=True)
    assert b"Quantum Algorithms" in response.data
    
    # Bio 업데이트 테스트 (action 추가)
    response = client.post('/profile', 
                           data={'bio': 'KNU Student & Researcher', 'action': 'update_bio'}, 
                           follow_redirects=True)
    assert b"KNU Student & Researcher" in response.data
    
    # 결과 화면에 'Name' 항목이 없는지 확인
    assert b"Name:" not in response.data

# 2. 학습 페이지 테스트
def test_add_study_subject(client):
    """학습 페이지 과목 추가 테스트"""
    response = client.post('/study', 
                           data={'subject': 'Open Source Programming'}, 
                           follow_redirects=True)
    assert response.status_code == 200
    assert b"Open Source Programming" in response.data
    
def test_append_profile_data(client):
    """기존 데이터가 사라지지 않고 추가(Append)되는지 테스트"""
    # 1. 초기값 확인 (QML, Initial Bio)
    
    # 2. Interest 추가
    client.post('/profile', data={'interest': 'Quantum Software', 'action': 'update_interest'})
    response = client.get('/profile')
    assert b"QML" in response.data # 기존 것 유지
    assert b"Quantum Software" in response.data # 새 것 추가
    
    # 3. Bio 추가
    client.post('/profile', data={'bio': 'KNU Student', 'action': 'update_bio'})
    response = client.get('/profile')
    assert b"KNU undergraduate student" in response.data # 기존 것 유지
    assert b"KNU Student" in response.data # 새 것 추가