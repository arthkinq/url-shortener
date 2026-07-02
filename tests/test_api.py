def test_create_short_url(client):
    response = client.post("/api/v1/urls", json={"original_url": "https://www.example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "short_id" in data
    assert "short_url" in data
    assert len(data["short_id"]) == 6

def test_create_invalid_url(client):
    response = client.post("/api/v1/urls", json={"original_url": "not-a-valid-url"})
    assert response.status_code == 422

def test_redirect_to_original(client):
    res = client.post("/api/v1/urls", json={"original_url": "https://www.google.com"})
    short_id = res.json()["short_id"]
    redirect_res = client.get(f"/{short_id}", follow_redirects=False)
    assert redirect_res.status_code == 307
    assert redirect_res.headers["location"] == "https://www.google.com/"

def test_redirect_not_found(client):
    res = client.get("/nonexistent_id", follow_redirects=False)
    assert res.status_code == 404

def test_get_url_stats(client):
    res = client.post("/api/v1/urls", json={"original_url": "https://www.python.org"})
    short_id = res.json()["short_id"]
    
    client.get(f"/{short_id}")
    client.get(f"/{short_id}")
    
    stats_res = client.get(f"/api/v1/urls/{short_id}/stats")
    assert stats_res.status_code == 200
    stats = stats_res.json()
    
    assert stats["short_id"] == short_id
    assert stats["original_url"] == "https://www.python.org/"
    assert stats["clicks"] == 2
    assert "created_at" in stats

def test_get_stats_not_found(client):
    res = client.get("/api/v1/urls/missing12/stats")
    assert res.status_code == 404

