from fastapi import (
    APIRouter,
    HTTPException,
    status
)

from crud.models import (
    HotelsDAO,
    RoomsDAO
)

from schemas.hotels import SchemaHotels

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)

@router.get("/all_hotels/",description="Hotels")
async def all_hotels():
    hotels = await HotelsDAO.find_all()

    if not hotels:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotels not found!"
        )

    return hotels

@router.get("/{hotel_id}/",response_model=SchemaHotels)
async def hotel_by_id(
    hotel_id: int
):
    hotel = await HotelsDAO.find_one_or_none(id=hotel_id)

    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found"
        )

    return hotel

@router.get("/{hotel_id}/rooms",description="Rooms")
async def get_hotel_rooms(hotel_id:int):
    hotel = await HotelsDAO.find_one_or_none(id=hotel_id)

    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found"
        )

    rooms = await RoomsDAO.find_all_filter(hotel_id=hotel_id)

    return rooms

