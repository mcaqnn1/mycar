from httpx import AsyncClient,ASGITransport
import pytest
from api.v1.routes.users import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

@pytest.mark.asyncio(loop_scope="session")
async def test_login():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http2://test"
    ) as client:
        response = await client.post("/user/login/", json={
            "full_name":"john",
            "email":"john@gmail.com",
            "password":"john"
        })
    assert response.status_code == 200


