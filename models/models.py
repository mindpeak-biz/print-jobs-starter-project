from typing import Optional
from sqlmodel import Field, Relationship, SQLModel


# Define the models --------------------------------------------------
class PrintJobCitationLink(SQLModel, table=True):
    __tablename__ = "print_job_citation_link"
    # This is a many-to-many relationship table between PrintJob and Citation
    print_job_id: Optional[int] = Field(
        default=None, foreign_key="print_jobs.id", primary_key=True
    )
    citation_id: Optional[int] = Field(
        default=None, foreign_key="citations.id", primary_key=True
    )


class Partner(SQLModel, table=True):
    __tablename__ = "partners"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    # Relationships
    citations: list["Citation"] = Relationship(back_populates="partner")


class Citation(SQLModel, table=True):
    __tablename__ = "citations"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    issue_date: str
    amount: Optional[float] = None
    partner_id: Optional[int] = Field(default=None, foreign_key="partners.id")
    # Relationships
    partner: Optional[Partner] = Relationship(back_populates="citations")
    print_jobs: list["PrintJob"] = Relationship(
        back_populates="citations", link_model=PrintJobCitationLink
    )


class PrintJob(SQLModel, table=True):
    __tablename__ = "print_jobs"
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    # Relationships
    citations: list[Citation] = Relationship(
        back_populates="print_jobs", link_model=PrintJobCitationLink
    )
# ---------------------------------------------------------------------