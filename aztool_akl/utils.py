# -*- coding: utf-8 -*-

def undercore2space(text: str):
    return text.replace('_', ' ')


def display_error(text: str):
    print(f"[ERROR] - {text}")


def display_warning(text: str):
    print(f"[WARNING] - {text}")


def round2(number):
    return round(float(number), 2)
