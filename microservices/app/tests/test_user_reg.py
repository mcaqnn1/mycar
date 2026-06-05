from httpx import AsyncClient,ASGITransport
import pytest
from fastapi import FastAPI
from api.v1.routes.users import router

app = FastAPI()
app.include_router(router)

@pytest.mark.asyncio(loop_scope="session")
async def test_register():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http1://test"
    ) as client:
        response = await client.post("/user/register/",json={
            "full_name":"Test User",
            "email":"test@gmail.com",
            "password":"12345"
        })
    assert response.status_code == 200

