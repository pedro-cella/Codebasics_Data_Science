from pydantic import BaseModel
from datetime import date
from typing import Literal, Optional

class Worker(BaseModel):
    registration_code: int
    name: str
    lastname: str
    birth_date: int 
    salary: float
    start_date: date
    end_date: Optional[date] = None
    satisfaction_rate: int
    department: str
    type: str

class Employee(Worker):
    type: Literal["Employee"] = "Employee"

class Outsourced(Worker):
    type: Literal["Outsourced"] = "Outsourced"

class Intern(Worker):
    type: Literal["Intern"] = "Intern"