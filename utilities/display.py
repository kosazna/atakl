# -*- coding: utf-8 -*-
# from atakl.utilities.utils import *


class Display:
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'

    def __init__(self, mode=None):
        self._mode = mode
        self._content = []

    @staticmethod
    def _display(content, kind=None):
        if kind is None:
            return content
        else:
            return f"[{kind}] - {content}"

    def set_mode(self, mode):
        self._mode = mode

    def get_content(self):
        to_show = '\n'.join(self._content)
        return to_show

    def erase(self):
        self._content = []

    def get_raw(self):
        return self._content

    def add_message(self, message):
        self._content.extend(message)

    def __call__(self, content, kind=None):
        if self._mode == 'CMD':
            print(self._display(content, kind))
        elif self._mode == 'GUI':
            self._content.append(self._display(content, kind))
        else:
            pass
