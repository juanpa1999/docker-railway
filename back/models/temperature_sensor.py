import sqlalchemy
from db import metadata

"""
temperature_sensor: Table contains structure for sensor(temperature)
"""
temperature_sensor = sqlalchemy.Table(
    "temperature_sensors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("temperature", sqlalchemy.String(60), nullable=False, unique=False),
    sqlalchemy.Column("creation_date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("session_user", sqlalchemy.ForeignKey("users.id"), nullable=False)
)