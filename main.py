# Project imports ------------------------------------------------------
from typing import Optional
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from models.models import PrintJob, Partner, Citation, PrintJobCitationLink
from sqlmodel import SQLModel, Session, create_engine
from bl import db_access as data 
# --------------------------------------------------------------------- 


app = FastAPI()


# ROUTES ---------------------------------------------------------------
# Create a Print job
@app.post("/printjobs", response_model=PrintJob)
def create_print_job(print_job: PrintJob):
    print_job = data.create_print_job(print_job)
    return print_job


# Get all print jobs 
@app.get("/printjobs", response_model=list[PrintJob])
def get_all_print_jobs():
    print_jobs = data.get_all_print_jobs()
    return print_jobs


# Get a print job by id 
@app.get("/printjobs/{print_job_id}", response_model=PrintJob)
def get_print_job(print_job_id: int):
    print_job = data.get_print_job(print_job_id)
    if not print_job:
        raise HTTPException(status_code=404, detail=f"Print job id: {print_job_id} not found")
    return print_job


# TODO: Add the following routes for print job management starter project 

# Get all print jobs by partner id (need partner id)

# Update print job (need print job id)

# Add citation to print job (need citation id and print job id)

# Get print job citations by print job id (need print job id)

# Remove citation from print job (need citation id and print job id)
# --------------------------------------------------------------------- 


# Run the app using Uvicorn -------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
# --------------------------------------------------------------------- 