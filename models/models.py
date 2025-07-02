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
    # Relationships
    citations: list["Citation"] = Relationship(back_populates="partner")


class Citation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    issue_date: str
    amount: Optional[float] = None
    partner_id: Optional[int] = Field(default=None, foreign_key="partner.id")
    # Relationships
    partner: Optional[Partner] = Relationship(back_populates="citations")
    printjobs: list["Printjob"] = Relationship(
        back_populates="citations", link_model=PrintjobCitationLink
    )


class Printjob(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    # Relationships
    citations: list[Citation] = Relationship(
        back_populates="printjobs", link_model=PrintjobCitationLink
    )
# ---------------------------------------------------------------------