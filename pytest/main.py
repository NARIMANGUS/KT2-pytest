"""Функции для контрольной работы № 2 по pytest."""

from pathlib import Path


def string_length(text: str) -> int:
    """Вернуть количество символов в строке, включая пробелы и переносы."""
    return len(text)


def save_string_to_file(text: str, file_path: str | Path) -> None:
    """Сохранить текст в UTF-8 файл, создав или перезаписав его."""
    Path(file_path).write_text(text, encoding="utf-8")
