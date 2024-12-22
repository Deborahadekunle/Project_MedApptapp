from fastapi import APIRouter
from database import appointments, doctors, patients

router = APIRouter()

@router.post("/")
def create_appointment(patient_id: int, date: str):
    # Check if patient exists
    if not any(patient["id"] == patient_id for patient in patients):
        return {"error": "Patient not found"}, 404

    # Find the first available doctor
    available_doctor = next((doc for doc in doctors if doc["is_available"]), None)
    if not available_doctor:
        return {"error": "No doctors available"}, 400

    # Create the appointment
    appointment_id = len(appointments) + 1
    new_appointment = {
        "id": appointment_id,
        "patient": patient_id,
        "doctor": available_doctor["id"],
        "date": date
    }
    appointments.append(new_appointment)
    available_doctor["is_available"] = False
    return {"message": "Appointment booked successfully", "appointment": new_appointment}

@router.put("/{appointment_id}/complete")
def complete_appointment(appointment_id: int):
    for appt in appointments:
        if appt["id"] == appointment_id:
            for doc in doctors:
                if doc["id"] == appt["doctor"]:
                    doc["is_available"] = True
            appointments.remove(appt)
            return {"message": "Appointment completed"}
    return {"error": "Appointment not found"}, 404

@router.delete("/{appointment_id}")
def cancel_appointment(appointment_id: int):
    for appt in appointments:
        if appt["id"] == appointment_id:
            for doc in doctors:
                if doc["id"] == appt["doctor"]:
                    doc["is_available"] = True
            appointments.remove(appt)
            return {"message": "Appointment canceled"}
    return {"error": "Appointment not found"}, 404
