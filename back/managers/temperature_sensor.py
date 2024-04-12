import sqlalchemy
from db import database
from fastapi import HTTPException
from models import temperature_sensor, user
from datetime import datetime
from schemas.request.sensor_input_data import TemperatureRegistrationData


class TemperatureSensor:

    @staticmethod
    async def get_all_temperatures():
        try:
            query = sqlalchemy.select([temperature_sensor])
            result = await database.fetch_all(query)
            return result
        except Exception as e:
            error_message = f"Failed to get temperatures: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    @staticmethod
    async def get_user_temperatures(current_user):
        try:
            query = sqlalchemy.select([temperature_sensor]).where(
                temperature_sensor.c.session_user == current_user["id"])
            result = await database.fetch_all(query)
            return result
        except Exception as e:
            error_message = f"Failed to get temperature for user {current_user['id']}: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)

    """@staticmethod
    async def create_temperature(temperature_data: TemperatureRegistrationData, current_user):
        try:
            user_id = current_user["id"]
            temperature_dict = temperature_data.model_dump()
            temperature_dict["creation_date"] = datetime.now().date()
            temperature_dict["session_user"] = user_id
            query = temperature_sensor.insert().values(**temperature_dict)
            last_record_id = await database.execute(query)
            return {**temperature_dict, "id": last_record_id}

        except Exception as e:
            error_message = f"Failed to create temperature: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)"""

    @staticmethod
    async def create_temperature(temperature_data: TemperatureRegistrationData):
        try:
            user_id = 1 # This is a test integer for testing, will be sensor id
            temperature_dict = temperature_data.model_dump()
            temperature_dict["creation_date"] = datetime.now().date()
            temperature_dict["session_user"] = user_id
            query = temperature_sensor.insert().values(**temperature_dict)
            last_record_id = await database.execute(query)
            return {**temperature_dict, "id": last_record_id}

        except Exception as e:
            error_message = f"Failed to create temperature: {str(e)}"
            print(error_message)
            raise HTTPException(status_code=500, detail=error_message)
