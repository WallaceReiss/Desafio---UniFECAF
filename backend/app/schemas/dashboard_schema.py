from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    name: str
    ra: str
    course: str
    total_progress: int

class TodayClass(BaseModel):
    subject: str
    time: str
    room: str

class Notification(BaseModel):
    id: int
    text: str
    read: bool

class AcademicSummary(BaseModel):
    subject: str
    grade: float
    absences: int

class FinancialSummary(BaseModel):
    next_due_date: str
    value: float
    status: str

class DashboardResponse(BaseModel):
    student: Student
    today_classes: List[TodayClass]
    notifications: List[Notification]
    academic_summary: List[AcademicSummary]
    financial_summary: FinancialSummary
