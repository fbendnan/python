from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(default=datetime.now())
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")

        if not any(
            crew_member.rank in [Rank.captain, Rank.commander]
            for crew_member in self.crew
        ):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = [crew_member for crew_member in self.crew
                           if crew_member.years_experience > 5]
            if len(experienced) < len(self.crew)/2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                    )

        if any(not crew_member.is_active for crew_member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        crew_valid = [
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=45,
                specialization="Mission Command",
                years_experience=20,
                is_active=True,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=34,
                specialization="Navigation",
                years_experience=10,
                is_active=True,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=29,
                specialization="Engineering",
                years_experience=6,
                is_active=True,
            ),
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            crew=crew_valid,
            budget_millions=2500.0,
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")

        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )

        print("=" * 41)
        print("Expected validation error:")
        crew_invalid = [
            CrewMember(
                member_id="CM010",
                name="Mark Lee",
                rank=Rank.lieutenant,
                age=30,
                specialization="Navigation",
                years_experience=8,
                is_active=True,
            ),
            CrewMember(
                member_id="CM011",
                name="Emma Davis",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=7,
                is_active=True,
            ),
        ]

        SpaceMission(
            mission_id="M2025_FAIL",
            mission_name="Test Failure Mission",
            destination="Mars",
            duration_days=100,
            crew=crew_invalid,
            budget_millions=500.0,
        )

    except ValidationError as e:
        print(e.errors()[0]['msg'].removeprefix("Value error, "))


main()
