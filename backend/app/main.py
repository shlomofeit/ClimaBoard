from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.cities_router import router as cities
from routers.weather_router import router as weather
from middleware.time_process import add_process_time_header

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.middleware("http")(add_process_time_header)

app.include_router(cities)

app.include_router(weather)
