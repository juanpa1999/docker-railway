from fastapi import APIRouter
from api_calls import auth, temperature_sensor

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(temperature_sensor.router)
