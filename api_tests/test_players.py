"""Test players api."""
import requests

import config


class TestPlayers:

    def test_get_players(self):
        """Test search players via API."""
        query = ('https://api.worldoftanks.ru/wot/account/list/'
                 f'?application_id={config.instance.application_id}&'
                 'search=alex')
        resp = requests.get(query).json()
        assert resp['status'] == 'ok'

    def test_get_players_with_not_enough_search_length(self):
        """Test search players with wrong 'search' parameter."""
        query = ('https://api.worldoftanks.ru/wot/account/list/'
                 f'?application_id={config.instance.application_id}&'
                 'search=al')
        resp = requests.get(query).json()
        assert resp['status'] == 'error'
