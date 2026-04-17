from enum import Enum


class AppStatus(Enum):
    APPLIED = 1
    REJECTED = 2
    PENDING = 3


from datetime import datetime


class JobModel:
    def __init__(self, name: str, title: str, link: str):
        self.name: str = name
        self.title: str = title
        self.link: str = link
        self.date_applied: datetime = datetime.now()
        self.status: AppStatus = AppStatus.APPLIED

    def add_name(self, name: str):
        if name.strip():
            self.names.append(name)

    def get_names(self):
        return self.names
