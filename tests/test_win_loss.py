import unittest
from unittest.mock import patch
from utils.stratz_api import get_player_win_loss

# to-do ajustar isso aqui em algum momento

class TestWinLossCommand(unittest.TestCase):

    @patch('utils.stratz.api.get_player_win_loss')
    def test_win_loss(self, mock_get_player_win_loss):
        mock_get_player_win_loss.return_value = {'wins': 5, 'losses': 3}

        performance = get_player_win_loss(123456)
        self.assertEqual(performance['wins'], 5)
        self.assertEqual(performance['losses'], 3)


if __name__ == '__main__':
    unittest.main()