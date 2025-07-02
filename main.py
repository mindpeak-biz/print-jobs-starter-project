from typing import Optional
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


# Define the models --------------------------------------------------
class PrintjobCitationLink(SQLModel, table=True):
    printjob_id: Optional[int] = Field(
        default=None, foreign_key="printjob.id", primary_key=True
    )
    citation_id: Optional[int] = Field(
        default=None, foreign_key="citation.id", primary_key=True
    )


class Partner(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    citations: list["Citation"] = Relationship(back_populates="partner")


class Citation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    issue_date: str
    amount: Optional[float] = None
    partner_id: Optional[int] = Field(default=None, foreign_key="partner.id")
    partner: Optional[Partner] = Relationship(back_populates="citations")
    printjobs: list["Printjob"] = Relationship(
        back_populates="citations", link_model=PrintjobCitationLink
    )


class Printjob(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str

    citations: list[Citation] = Relationship(
        back_populates="printjobs", link_model=PrintjobCitationLink
    )
# ---------------------------------------------------------------------


# Set up the database --------------------------------------------------
# Create the SQLite database engine (change the URL to MySQL later)
engine = create_engine("sqlite:///printjobs.db")
SQLModel.metadata.create_all(engine)


# Get the session (this will be injected as a dependency for our FastAPI routes)
def get_session():
    with Session(engine) as session:
        yield session
# --------------------------------------------------------------------- 


# Create and configure the app ----------------------------------------
app = FastAPI()
# --------------------------------------------------------------------- 


# ROUTES ---------------------------------------------------------------
# Create a Printjob
@app.post("/printjobs", response_model=Printjob)
def create_printjob(printjob: Printjob, session: Session = Depends(get_session)):
    session.add(printjob)
    session.commit()
    session.refresh(printjob)
    return printjob


# Get all print jobs 
@app.get("/printjobs", response_model=list[Printjob])
def get_all_printjobs(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    printjobs = session.exec(select(Printjob).offset(skip).limit(limit)).all()
    return printjobs


# Get a print job by id 
@app.get("/printjobs/{printjob_id}", response_model=Printjob)
def get_printjob_by_id(printjob_id: int, session: Session = Depends(get_session)):
    printjob = session.get(Printjob, printjob_id)
    if not printjob:
        raise HTTPException(status_code=404, detail="Printjob not found")
    return printjob


# --------------------------------------------------------------------- 
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