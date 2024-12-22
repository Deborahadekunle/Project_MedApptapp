from fastapi import APIRouter
from models import Patient
from database import patients

router = APIRouter()

@router.get("/")
def list_patients():
    return {"patients": patients}

@router.post("/")
def create_patient(patient: Patient):
    patients.append(patient.dict())
    return {"message": "Patient added successfully", "patient": patient}

@router.get("/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return {"error": "Patient not found"}, 404

@router.put("/{patient_id}")
def update_patient(patient_id: int, patient: Patient):
    for index, existing_patient in enumerate(patients):
        if existing_patient["id"] == patient_id:
            patients[index] = patient.dict()
            return {"message": "Patient updated successfully", "patient": patient}
    return {"error": "Patient not found"}, 404

@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            return {"message": "Patient deleted successfully"}
    return {"error": "Patient not found"}, 404
