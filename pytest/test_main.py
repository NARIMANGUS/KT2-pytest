"""Тестирование работы со строками и файлами."""

from main import save_string_to_file, string_length


def test_empty_string():
    assert string_length("") == 0


def test_spaces_only():
    assert string_length("     ") == 5


def test_multiline_string():
    assert string_length("Hello\nWorld") == 11


def test_save_string_to_file(tmp_path):
    path = tmp_path / "message.txt"
    save_string_to_file("Привет, мир!\nВторая строка.", path)

    assert path.exists()
    assert path.read_text(encoding="utf-8") == "Привет, мир!\nВторая строка."


def test_save_empty_string(tmp_path):
    path = tmp_path / "empty.txt"
    save_string_to_file("", path)

    assert path.is_file()
    assert path.read_text(encoding="utf-8") == ""


def test_save_overwrites_existing_file(tmp_path):
    path = tmp_path / "message.txt"
    save_string_to_file("Старый текст", path)
    save_string_to_file("Новый текст", path)

    assert path.read_text(encoding="utf-8") == "Новый текст"
