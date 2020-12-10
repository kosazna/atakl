# -*- coding: utf-8 -*-
import os
from datetime import datetime
from pathlib import Path


def c_2space(text: str):
    return text.replace('_', ' ')


def display_error(text: str):
    print(f"\n[ERROR] - {text}")


def display_warning(text: str):
    print(f"\n[WARNING] - {text}")


def display(text: str):
    print(f"\n[INFO] - {text}")


def round2(number):
    return round(float(number), 2)


def timestamp(obj=False):
    datetime_now = datetime.now()
    return datetime_now if obj else datetime_now.strftime("%d%m%Y")


def count_files(path: (str, Path), pattern="*.xlsx"):
    path_to_count = Path(path)
    xlsx_count = list(path_to_count.glob(pattern))
    return len(xlsx_count)


def open_excel(path):
    os.startfile(path)
