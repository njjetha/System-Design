import unittest
from unittest.mock import Mock, patch

import requests



def get_user_data(user_id):
    responses=requests.get(f"https://api/example.com/user/{user_id}")
    return responses.json()

class TestUserData(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_data(self,m_get):
        mock_reponse=Mock()
        response_dict={'name':'john', 'email':'john@gmail.com'}
        mock_reponse.json.return_value=response_dict
        m_get.return_value=mock_reponse

        out=get_user_data(1)
        self.assertEqual(response_dict, out)

if __name__=='__main__':
    unittest.main()