from models.models import PrintJob, Partner, Citation, PrintJobCitationLink
from dal import mysql as dal


def create_print_job(print_job: PrintJob) -> PrintJob:
    print_job = dal.create_print_job(print_job)
    return print_job


def get_all_print_jobs() -> list[PrintJob]:
    print_jobs = dal.get_all_print_jobs()
    return print_jobs


def get_print_job(print_job_id: int) -> PrintJob:
    try:
        print_job = dal.get_print_job(print_job_id)
    except ValueError as e:
        # Handle the case where the print job is not found (log it, raise an exception, etc.)
        # For now I'm just printing the error message and re-throwing the exception.
        print(f"Caught an exception: {e}")
        raise
    return print_job




# --------------------------------------------------------------------- 
# TODO: Add the following routes for print job management starter project 

# Get all print jobs by partner id (need partner id)

# Update print job (need print job id)

# Add citation to print job (need citation id and print job id)

# Get print job citations by print job id (need print job id)

# Remove citation from print job (need citation id and print job id)
# --------------------------------------------------------------------- 


