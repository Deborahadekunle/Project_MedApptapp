from fastapi import APIRouter
from models import Doctor
from database import doctors

router = APIRouter()

@router.get("/")
def list_doctors():
    return {"doctors": doctors}

@router.post("/")
def create_doctor(doctor: Doctor):
    doctors.append(doctor.dict())
    return {"message": "Doctor added successfully", "doctor": doctor}

@router.put("/{doctor_id}/availability")
def set_availability(doctor_id: int, is_available: bool):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            doctor["is_available"] = is_available
            return {"message": "Doctor availability updated"}
    return {"error": "Doctor not found"}, 404
