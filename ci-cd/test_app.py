from app import app

def test_hello():
    response = app.test_client().get('/')
    assert response.data == b'Hello, Abhay from Flask!'
