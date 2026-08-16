from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from models import JobModel


class JobView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 MVC Example")

        # Widgets
        self.name = QLineEdit()
        self.name.setPlaceholderText("Enter a Company:")

        self.title = QLineEdit()
        self.title.setPlaceholderText("Enter a Title:")

        self.link = QLineEdit()
        self.link.setPlaceholderText("Enter the link:")

        inputs = QHBoxLayout()
        inputs.addWidget(self.name)
        inputs.addWidget(self.title)
        inputs.addWidget(self.link)

        self.add_button = QPushButton("Add Job")
        self.remove_button = QPushButton("Remove Job")
        self.list_widget = QListWidget()

        layout = QVBoxLayout()
        layout.addLayout(inputs)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def clear_input(self) -> None:
        self.name.clear()
        self.title.clear()
        self.link.clear()

    def update_list(self, jobs: list[JobModel]) -> None:
        self.list_widget.clear()
        self.list_widget = jobs

    def create_job(self) -> JobModel:
        return JobModel(self.name.text(), self.title.text(), self.link.text())

    def delete_job(self, deleted_job: JobModel | str) -> bool:
        if isinstance(deleted_job, JobModel):
            job = self.list_widget.takeItem(deleted_job)
            del job
        elif isinstance(deleted_job, str):
            for job in self.list_widget:
                if job.company_name == deleted_job:
                    job = self.list_widget.takeItem(job)
                    del job
                    return True

        return False
