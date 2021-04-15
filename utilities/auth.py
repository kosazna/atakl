# -*- coding: utf-8 -*-

import requests
import json


class Authorize:
    TOKEN = '33e7a243e44dc089cd52476a3baebc59db6677e2'
    OWNER = 'kosazna'
    REPO = 'atauth'
    FILE = 'atakl.json'

    URL = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE}"

    HEADERS = {'accept': 'application/vnd.github.v3.raw',
               'authorization': f"token {TOKEN}"}

    def __init__(self, domain, logger):
        self._domain = domain
        self.log = logger
        self._r = None
        self._user_access = None
        self._counter = 0

        self._reload()

    def _reload(self):
        try:
            self._r = requests.get(Authorize.URL, headers=Authorize.HEADERS)
            self._user_access = json.loads(self._r.text)
        except requests.ConnectionError:
            pass

        self._counter = 0

    def user_is_licensed(self):
        if self._user_access is not None:
            try:
                if self._counter < 10:
                    self._counter += 1
                    return self._user_access[self._domain]
                else:
                    self._reload()
                    self._counter += 1
                    return self._user_access[self._domain]
            except KeyError:
                return True
        else:
            self.log("Internet connection needed")
            return False
