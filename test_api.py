import pytest
import requests

BASE_URL = 'http://localhost:5000'

#@pytest.fixture()
def test_create_project():
    data = {
        'title': 'project 1',
        'sprints': [
            {
                'title': 'sprint 1',
                'effort_estimated': 10,
                'cost_estimated': 200.12
            }
        ]
    }
    response = requests.post(f'{BASE_URL}/projects', json=data)
    assert response.status_code == 201
    assert 'id' in response.json()

if __name__ == '__main__':
    pytest.main()
