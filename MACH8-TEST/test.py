import unittest
import requests
from main import index_or_none, get_player_add_height

class TestAddHeightPlayers(unittest.TestCase):
    
    def test_api_response(self):
        url = 'https://mach-eight.uc.r.appspot.com/'
        data = requests.get(url=url).json()
        self.assertIsNotNone(data['values'])
    
    def test_index_or_none(self):
        url = 'https://mach-eight.uc.r.appspot.com/'
        data = requests.get(url=url).json()
        players_temp = [p["h_in"] for p in data['values']]
        result = index_or_none(players_temp, 200, 0, data['values'])
        self.assertIsNone(result)
        result = index_or_none(players_temp, 70, 0, data['values'])
        self.assertIsNotNone(result)
        
    def test_result_add_height(self):
        result_expected = str([u'Brevin Knight Nate Robinson', u'Nate Robinson Mike Wilks'])
        result = str(get_player_add_height(139))
        self.assertEqual(result_expected,result)
        

if __name__=='__main__':
    unittest.main()