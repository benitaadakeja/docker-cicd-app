from app.app import app
def test_home_route():
	client = app.test_client()
	response = client.get("/")
	assert response.status_code == 200
	assert response.data.decode() == "Hello from CI/CD and Docker applications!"

def test_health_check():
	client = app.test_client()
	response = client.get("/health")
	assert response.status_code == 200
	assert response.json == {"status": "healthy"}

