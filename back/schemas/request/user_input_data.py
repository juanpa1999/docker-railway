from pydantic import BaseModel, Field
from enum import Enum


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"


class UserRole(str, Enum):
    master = "master"
    admin = "admin"
    operator = "operator"


"""
User Request Schemas
"""


# User Registration Schema
class UserRegistrationData(BaseModel):
    username: str
    password: str
    status: UserStatus = Field(default=UserStatus.pending)
    user_role: UserRole = Field(default=UserRole.operator)


# User Login Schema
class UserLoginData(BaseModel):
    username: str
    password: str
