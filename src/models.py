from datetime import datetime
from enum import Enum


class AppStatus(Enum):
    APPLIED = 1
    REJECTED = 2
    PENDING = 3


class JobModel:
    def __init__(self, company_name: str, title: str, link: str):
        self.company_name: str = company_name
        self.title: str = title
        self.link: str = link
        self.date_applied = datetime.date
        self.status: AppStatus = AppStatus.APPLIED
