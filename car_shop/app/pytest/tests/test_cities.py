from httpx import AsyncClient,ASGITransport
from modules.cities.router import router
from fastapi import FastAPI
import pytest

app = FastAPI()
app.include_router(router=router)

@pytest.mark.asyncio(loop_scope="session")
async def test_city_create():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test1"
    ) as client:

        response = await client.post("/cities/",json={
            "name":"Almaty obl"
        })

        assert response.status_code == 200

@pytest.mark.asyncio(loop_scope="session")
async def test_get_cities():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test2"
    ) as client:

        response = await client.get("/cities/all/")

        response.status_code == 200

@pytest.mark.asyncio(loop_scope="session")
async def test_get_city_by_id():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test3"
    ) as client:

        response = await client.get("/cities/{city_id}/")
        
        assert response.status_code == 200