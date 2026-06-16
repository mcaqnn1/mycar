from httpx import AsyncClient,ASGITransport
from fastapi import FastAPI
from modules.users.router import router
import pytest

app = FastAPI()
app.include_router(router=router)

@pytest.mark.asyncio(loop_scope="session")
async def test_registration():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test1"
    ) as client:

        response = await client.post("/users/registration/",json={
            "phone_number": "testnumbexcr",
            "email": "test2@test.com",
            "is_active": True,
            "password": "test2",
            "full_name": "Test2"
        })
        
        assert response.status_code == 200

@pytest.mark.asyncio(loop_scope="session")
async def test_login():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test2"
    ) as client:

        response = await client.post("/users/login/",json={
            "email":"test@test.com",
            "password":"test11"
        })

        assert response.status_code == 200

@pytest.mark.asyncio(loop_scope="session")
async def test_users():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="htpp://test3"
    ) as client:

        response = await client.get("/users/all/")

        assert response.status_code == 200


