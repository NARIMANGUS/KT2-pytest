"""Проверка SQLite с изоляцией и очисткой после каждого теста."""


def test_sqlite_initially_empty(db_connection):
    count = db_connection.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    assert count == 0


def test_sqlite_insert_and_select(db_connection):
    # Каждый тест получает отдельную пустую базу данных.
    assert db_connection.execute("SELECT COUNT(*) FROM messages").fetchone()[0] == 0

    db_connection.execute("INSERT INTO messages (text) VALUES (?)", ("Привет из SQLite",))
    db_connection.commit()

    result = db_connection.execute("SELECT text FROM messages").fetchone()
    assert result == ("Привет из SQLite",)


def test_sqlite_multiple_records(db_connection):
    assert db_connection.execute("SELECT COUNT(*) FROM messages").fetchone()[0] == 0

    db_connection.executemany(
        "INSERT INTO messages (text) VALUES (?)",
        [("Первая строка",), ("Вторая строка",), ("Третья строка",)],
    )
    db_connection.commit()

    texts = db_connection.execute("SELECT text FROM messages ORDER BY id").fetchall()
    assert texts == [("Первая строка",), ("Вторая строка",), ("Третья строка",)]
