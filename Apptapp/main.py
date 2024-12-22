from fastapi import FastAPI
from routers import patients, doctors, appointments

app = FastAPI()

# Register routers
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Apptapp!"}
