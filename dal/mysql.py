# This file is part of the DAL (Data Access Layer) for the Print Jobs Starter Project.
# It provides functions to interact with the MySQL database for managing print jobs, partners, and citations.


# Project imports ------------------------------------------------------
import os
from dotenv import load_dotenv
from models.models import PrintJob, Partner, Citation, PrintJobCitationLink
from sqlmodel import SQLModel, Session, create_engine, select


# Environment variables -----------------------------------------------
load_dotenv()

# Now you can access the variables using os.environ
DATABASE_URL = os.environ.get("DATABASE_URL")
# --------------------------------------------------------------------- 


# Set up the database --------------------------------------------------
# Create the SQLite database engine (change the URL to MySQL later)
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
# --------------------------------------------------------------------- 


def create_print_job(print_job: PrintJob) -> PrintJob:
    session = next(get_session()) 
    session.add(print_job)
    session.commit()
    session.refresh(print_job)
    return print_job


def get_all_print_jobs() -> list[PrintJob]:
    session = next(get_session())
    print_jobs = session.exec(select(PrintJob)).all()
    if not print_jobs:
        return []
    return print_jobs


def get_print_job(print_job_id: int) -> PrintJob | None:
    session = next(get_session())
    print_job = session.get(PrintJob, print_job_id)
    if not print_job:
        raise ValueError(f"Print job with id {print_job_id} not found")
    session.refresh(print_job)
    return print_job



# --------------------------------------------------------------------- 
# TODO: Add the following routes for print job management starter project 

# Get all print jobs by partner id (need partner id)

# Update print job (need print job id)

# Add citation to print job (need citation id and print job id)

# Get print job citations by print job id (need print job id)

# Remove citation from print job (need citation id and print job id)
# --------------------------------------------------------------------- 

