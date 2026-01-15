from pydantic import BaseModel
from datetime import date

class ApplicationCreate(BaseModel):
    company: str
    role: str
    link: str
    status: str
    date_applied: date
    notes: str = ""
