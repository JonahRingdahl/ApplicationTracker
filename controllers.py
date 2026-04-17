from models import JobModel
from views import JobView


class JobController:
    def __init__(self):
        self.jobs = []
        self.view = JobView()

        self.view.add_button.clicked.connect(self.add_name)
        self.view.show()

    def add_name(self):
        name, title, link = self.view.create_job()
        self.jobs.append(JobModel(name, title, link))
        self.view.update_list(self.jobs)
        self.view.clear_input()
