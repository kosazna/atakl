# -*- coding: utf-8 -*-
from datetime import datetime
from pathlib import *


def undercore2space(text: str):
    return text.replace('_', ' ')


def display_error(text: str):
    print(f"[ERROR] - {text}")


def display_warning(text: str):
    print(f"[WARNING] - {text}")


def round2(number):
    return round(float(number), 2)


def timestamp(obj=False):
    datetime_now = datetime.now()
    return datetime_now if obj else datetime_now.strftime("%d%m%Y")


def count_xlsx(path: (str, Path), pattern="*.xlsx"):
    path_to_count = Path(path)
    xlsx_count = list(path_to_count.glob(pattern))
    return len(xlsx_count)
