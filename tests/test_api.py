import pytest
from httpx import ASGITransport, AsyncClient
from src.api.main import app

@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c

@pytest.mark.asyncio
async def test_sentiment_analysis(client):
    r = await client.post("/api/v1/analyze/sentiment", json={
        "text": "I absolutely love this product! Best purchase ever!", "source": "amazon"
    })
    assert r.status_code == 200
    d = r.json()
    assert d["sentiment"] in ("positive", "negative", "neutral")
    assert "emotions" in d

@pytest.mark.asyncio
async def test_batch(client):
    r = await client.post("/api/v1/analyze/batch", json={"texts": [
        {"text": "Great experience", "source": "twitter"},
        {"text": "Terrible quality", "source": "amazon"},
        {"text": "Just okay nothing special", "source": "general"}
    ]})
    assert r.status_code == 200
    d = r.json()
    assert d["total"] == 3

@pytest.mark.asyncio
async def test_aspect(client):
    r = await client.post("/api/v1/analyze/aspects", json={
        "text": "The screen is beautiful but the battery life is disappointing", "source": "general"
    })
    assert r.status_code == 200
    assert len(r.json()["aspects"]) > 0
