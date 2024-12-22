from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class Appointment(BaseModel):
    id: int
    patient: int  # Patient ID
    doctor: int   # Doctor ID
    date: str     # Appointment date (ISO format)
