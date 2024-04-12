from pydantic import BaseModel

"""
User Request Schemas
"""


# User Temperature Schema
class TemperatureRegistrationData(BaseModel):
    temperature: str