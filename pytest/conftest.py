import sqlite3

import pytest


@pytest.fixture(scope="function")
def db_connection(tmp_path):
    
    db_path = tmp_path / "test_database.sqlite3"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute(
            """CREATE TABLE messages (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   text TEXT NOT NULL
               )"""
        )
        connection.commit()

        yield connection
    finally:
        try:
            connection.execute("DELETE FROM messages")
            connection.commit()
        finally:
            connection.close()
            db_path.unlink(missing_ok=True)
