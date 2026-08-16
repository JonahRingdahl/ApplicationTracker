from db import Database
from models import JobModel
from views import JobView

DB_NAME: str = "jobs_db"

class JobController:
    def __init__(self):
        self.jobs: list[JobModel] = []
        self.view: JobView = JobView()
        self.db_name: str= f"./{DB_NAME}"
        self.db: Database = Database(self.db_name)
        self.db.create_table()

        self.view.add_button.clicked.connect(self.add_name)
        self.view.show()

    def add_name(self):
        job: JobModel = self.view.create_job()
        self.jobs.append(job)
        self.db.insert_job(job)
        self.view.update_list(self.jobs)
        self.view.clear_input()
