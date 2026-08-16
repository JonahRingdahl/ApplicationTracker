import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

from controllers import JobController


def main():
    app = QApplication(sys.argv)
    controller = JobController()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
