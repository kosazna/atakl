# -*- coding: utf-8 -*-
from datetime import datetime
from pathlib import Path
from os import startfile

split_char = '@'


def c_2space(text: str):
    return text.replace('_', ' ')


def display_error(text: str):
    print(f"\n[ERROR] - {text}")


def display_warning(text: str):
    print(f"\n[WARNING] - {text}")


def display_info(text: str):
    print(f"\n[INFO] - {text}")


def round2(number):
    return round(float(number), 2)


def datestamp(obj=False):
    datetime_now = datetime.now()
    return datetime_now if obj else datetime_now.strftime("%d%m%Y")


def dtstamp(obj=False):
    datetime_now = datetime.now()
    return datetime_now if obj else datetime_now.strftime("%Y-%m-%d %H:%M:%S")


def count_files(path: (str, Path), pattern="*.xlsx"):
    path_to_count = Path(path)
    xlsx_count = list(path_to_count.glob(pattern))
    return len(xlsx_count)


def open_excel(path):
    startfile(path)


def parse_xlsx(text):
    _text = str(text)
    if split_char in _text:
        _split = _text.split(split_char)
        _path = _split[0]
        _sheet = _split[1]
        return Path(_path), _sheet
    else:
        return Path(_text), 0
