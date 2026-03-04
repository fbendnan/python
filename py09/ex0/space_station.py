from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default=datetime.now())
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    try:
        print("========================================")
        print("Valid station created:")
        space_station1 = SpaceStation(
                station_id='ISS001', name='International Space Station',
                crew_size=6, power_level=85.5, oxygen_level=92.3,
                is_operational=True)
        print(f"ID: {space_station1.station_id}")
        print(f"Name: {space_station1.name}")
        print(f"Crew: {space_station1.crew_size}")
        print(f"Power: {space_station1.power_level}")
        print(f"Oxygen: {space_station1.oxygen_level}")
        print(f"Status: {("Operational" if space_station1.is_operational
                          else "Not operational")}")
        print()

        print("========================================")
        print("Expected validation error:")
        space_station1 = SpaceStation(
                station_id='ISS001', name='International Space Station',
                crew_size=25, power_level=85.5, oxygen_level=92.3,
                is_operational=True
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


main()
