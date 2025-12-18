from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_movie():
    response = client.get('/movie')
    assert response.status_code == 200

    data = response.json()

    assert data
    for key in ['title', 'overview', 'release_date']:
        assert key in data

    assert isinstance(data['title'], str)
    assert isinstance(data['overview'], str)
    assert isinstance(data['release_date'], str)

def test_get_genre():
    response = client.get('/genre')
    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert 'id' in data[0] and 'name' in data[0]
    assert isinstance(data[0]['id'], int)
    assert isinstance(data[0]['name'], str)

def test_movie_data_not_empty():
    response = client.get('/movie')
    data = response.json()

    assert data['title'] != ''
    assert data['overview'] != ''
    assert data['release_date'] != ''
    