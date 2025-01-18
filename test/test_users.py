from fastapi.testclient import TestClient
from ..main import app


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    
    

def test_create_user():
    response = client.post("/users", json={"email":"ada@gmail.com", "password":"ada1234"})
    
    assert response.status_code == 201
    
    
    