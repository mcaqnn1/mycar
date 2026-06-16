from httpx import AsyncClient,ASGITransport
from modules.cars.router import router
from fastapi import FastAPI
import pytest

app = FastAPI()
app.include_router(router=router)

@pytest.mark.asyncio(loop_scope="session")
async def test_car_create():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test1"
    ) as client:

        response = await client.post("/cars/",json={
            "user_id": "08d76ef1-6d4a-4d2f-a4c3-0aa22e1570dc",
            "city_id": "ad10a43a-a1ab-4807-8610-f660e5da634c", #Almaty
            "brand": "Toyota",
            "model": "Camry 70",
            "mileage": 45617,
            "description": "good"
        })
        
        assert response.status_code == 200

@pytest.mark.asyncio(loop_scope="session")
async def test_cars():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test2"
    ) as client:

        response = await client.get("/cars/all/")

        assert response.status_code == 200

@pytest.mark.asyncio(loop_scope="session")
async def test_get_car_by_id():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test3"
    ) as client:
        
        response = await client.get("/cars/{car_id}/")

        assert response.status_code == 200