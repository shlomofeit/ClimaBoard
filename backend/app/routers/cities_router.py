from fastapi import APIRouter, HTTPException, Query
from services.weather_service import get_coordinates

router = APIRouter(tags=["Cities"])


@router.get("/search")
def get_cities(
    city_search: str = Query(
        ..., max_length=2, description="returns cities array by your string"
    )
):
    cities_list = get_coordinates(city_search)

    if not cities_list:
        raise HTTPException(404, "City not found")

    return cities_list
