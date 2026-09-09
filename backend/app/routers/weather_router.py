from fastapi import APIRouter, HTTPException, Query
from services.weather_service import get_current_weather, get_forecast_weather

router = APIRouter(tags=["Weather"])


@router.get("/current")
def get_current(lat, lon):
    current = get_current_weather(lat, lon)

    if not current:
        raise HTTPException(404, "wether no found")

    return current


@router.get("/forecast")
def get_current(lat, lon):
    forecast = get_forecast_weather(lat, lon)

    if not forecast:
        raise HTTPException(404, "wether no found")

    return forecast


@router.get("/compare")
def compare_cities(
    lat1: float = Query(..., ge=-90.0, le=90.0),
    lon1: float = Query(..., ge=-180.0, le=180.0),
    lat2: float = Query(..., ge=-90.0, le=90.0),
    lon2: float = Query(..., ge=-180.0, le=180.0),
):
    current1 = get_current_weather(lat1, lat1)
    current2 = get_current_weather(lat2, lat2)

    return {"current_1": current1, "current_2": current2}
