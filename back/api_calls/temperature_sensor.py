from fastapi import APIRouter, Depends, HTTPException
from managers.auth import AuthManager
from managers.temperature_sensor import TemperatureSensor
from schemas.request.sensor_input_data import TemperatureRegistrationData
from schemas.request.user_input_data import UserRole

router = APIRouter(prefix="/temperature_sensor", tags=["temperature_sensor"],
                   responses={401: {"user": "Not authorized"}})

"""@router.get("/show_all_temperatures/", description="Allows users to get all cases")
async def get_all_cases(current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] in [UserRole.master, UserRole.admin, UserRole.operator]:
        temperatures = await TemperatureSensor.get_all_temperatures()
        return temperatures
    else:
        raise HTTPException(status_code=403, detail="Not authorized to view cases")"""


@router.get("/show_all_temperatures/", description="Allows users to get all cases")
async def get_all_temperatures():
    try:
        temperatures = await TemperatureSensor.get_all_temperatures()
        return temperatures
    except:
        raise HTTPException(status_code=403, detail="Not authorized to view cases")


@router.post("/create_temperature/", description="Allows users to create a new temperature")
async def create_temperatures(temperature_data: TemperatureRegistrationData):
    try:
        result = await TemperatureSensor.create_temperature(temperature_data)
        return result
    except:
        raise HTTPException(status_code=403, detail="Unexpected error while uploading temperature sensor data")
