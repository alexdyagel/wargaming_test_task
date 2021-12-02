"""Authentication tests."""
import requests

import config


class TestAuthentication:

    def test_open_id_login(self):
        """Test that we can login to the app with open id."""
        query = ('https://api.worldoftanks.ru/wot/auth/login/?application_id='
                 f'{config.instance.application_id}&nofollow=1')
        resp = requests.post(query).json()
        assert resp['status'] == 'ok'

    def test_prolonagate_access_token(self):
        """Test that we can prolongate access token."""
        query = ('https://api.worldoftanks.ru/wot/auth/prolongate/'
                 f'?application_id={config.instance.application_id}'
                 f'&access_token={config.instance.access_token}')
        resp = requests.post(query).json()
        assert resp['status'] == 'ok'


