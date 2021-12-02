import json
import os


class TestInstance:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):

        with open(os.path.join(os.path.dirname(__file__),
                               'config.json'), 'r') as config_file:
            self._params = json.load(config_file)

    @property
    def application_id(self):
        return self._params.get("application_id")

    @property
    def access_token(self):
        return self._params.get("access_token")


instance = TestInstance()
