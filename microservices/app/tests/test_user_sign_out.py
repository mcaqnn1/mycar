from httpx import AsyncClient,ASGITransport
import pytest
from fastapi import FastAPI
from api.v1.routes.users import router

app = FastAPI()
app.include_router(router)

@pytest.mark.asyncio(loop_scope="session")
async def test_sign_out():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http3://test"
    ) as client:
        response = await client.post("/user/sign_out/")

    assert response.status_code == 200