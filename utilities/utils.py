# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from pathlib import Path
from typing import Union

if sys.platform == 'win32':
    from os import startfile

    def open_excel(path):
        startfile(path)
else:
    def open_excel(path):
        print("Platform does not support os.startfile")
        print(f"{path} is not used.")

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


def count_files(path: Union[str, Path], pattern="*.xlsx"):
    path_to_count = Path(path)
    xlsx_count = list(path_to_count.glob(pattern))
    return len(xlsx_count)


def parse_xlsx(text):
    _text = str(text)
    if split_char in _text:
        _split = _text.split(split_char)
        _path = _split[0]
        _sheet = _split[1]
        return Path(_path), _sheet
    else:
        return Path(_text), 0


def check_idxs(data, index, cols: list):
    bools = []
    for col in cols:
        idx1 = data.loc[index, col]
        try:
            idx2 = data.loc[index + 1, col]
        except KeyError:
            idx2 = None

        bools.append(idx1 == idx2)

    return all(bools)


def col_has_na(df, col, idx_shift=0):
    _nas = df.loc[df[col].isna(), col]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs


def col_values_equal_zero(df, col, idx_shift=0):
    _nas = df.loc[df[col] == 0, col]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs


def col_values_not_equal_zero(df, col, idx_shift=0):
    _nas = df.loc[df[col] != 0, col]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs


def col_values_over(df, col, value, idx_shift=0):
    _nas = df.loc[df[col] > value, col]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs


def col_values_over_or_equal(df, col, value, idx_shift=0):
    _nas = df.loc[df[col] >= value, col]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs


def col_values_under(df, col, value, idx_shift=0):
    _nas = df.loc[df[col] < value, col]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs


def col_values_under_or_equal(df, col, value, idx_shift=0):
    _nas = df.loc[df[col] <= value, col]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs


def duplicated_data(df, cols, idx_shift=0):
    _cols = [cols] if isinstance(cols, str) else cols

    _nas = df.loc[df.duplicated(subset=_cols, keep=False), _cols[0]]
    _idxs = (_nas.index + idx_shift).tolist()

    return not _nas.empty, _idxs
