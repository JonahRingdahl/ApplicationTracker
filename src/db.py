import sqlite3

from models import JobModel


class Database:
    def __init__(self, db_path: str):
        self.db_path: str = db_path
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        self.cursor: sqlite3.Cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS job (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                title TEXT NOT NULL,
                link TEXT NOT NULL,
                date_applied TEXT NOT NULL,
                status INTEGER NOT NULL
            )
            """
        )
        self.conn.commit()

    def insert_job(self, job: JobModel):
        self.cursor.execute(
            """
            INSERT INTO job (name, title, link, date_applied, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (job.company_name, job.title, job.link, job.date_applied, job.status),
        )
        self.conn.commit()

    def get_jobs(self):
        self.cursor.execute(
            """
            SELECT * FROM job
            """
        )
        return self.cursor.fetchall()

    def get_job_by_id(self, id):
        self.cursor.execute(
            """
            SELECT * FROM job WHERE id = ?
            """,
            (id,),
        )
        return self.cursor.fetchone()

    def update_job(self, job):
        self.cursor.execute(
            """
            UPDATE job SET name = ?, title = ?, link = ?, date_applied = ?, status = ?
            WHERE id = ?
            """,
            (job.name, job.title, job.link, job.date_applied, job.status, job.id),
        )

    def delete_job(self, id):
        self.cursor.execute(
            """
            DELETE FROM job WHERE id = ?
            """,
            (id,),
        )
