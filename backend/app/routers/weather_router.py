from fastapi import APIRouter, HTTPException, Query
from services.weather_service import get_current_weather, get_forecast_weather

router = APIRouter(tags=["Weather"])


@router.get("/current")
def get_current(lat: float, lon: float):
    current = get_current_weather(lat, lon)

    if not current:
        raise HTTPException(404, "wether no found")

    return current


@router.get("/forecast")
def get_current(lat: float, lon: float):
    forecast = get_forecast_weather(lat, lon)

    if not forecast:
        raise HTTPException(404, "wether no found")

    return forecast
