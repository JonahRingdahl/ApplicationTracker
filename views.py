from PyQt6.QtCore import QLine
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
        self.list_widget = QListWidget()

        layout = QVBoxLayout()
        layout.addLayout(inputs)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def clear_input(self):
        self.name.clear()
        self.title.clear()
        self.link.clear()

    def update_list(self, jobs: list[JobModel]):
        self.list_widget.clear()

        for job in jobs:
            self.list_widget.addItem(job.name + job.title + job.link)

    def create_job(self):
        return self.name.text(), self.title.text(), self.link.text()
