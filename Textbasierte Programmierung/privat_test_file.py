
from itertools import count
import unittest
import tictactoe
from unittest.mock import patch


class TestComputerWins(unittest.TestCase):

    @patch('tictactoe.computer_clicks')
    def test_computer_wins_left_coloum_and_clicks_UL(self, mock_helper):
        tictactoe.computer = [1,0,0,1,0,0,0,0,0] 
        tictactoe.blocked_boxes = [0,0,0,0,0,0,0,0,0]

        tictactoe.computer_wins()

        mock_helper.assert_called_once_with(tictactoe.UL)

    @patch('tictactoe.computer_clicks')
    def test_computer_does_not_wins_and_clicks_no_field_to_win(self, mock_helper):
        tictactoe.computer = [1,0,0,1,0,0,0,0,0] 
        tictactoe.blocked_boxes = [1,1,1,1,1,1,1,1,1]
        
        tictactoe.computer_wins()

        mock_helper.assert_not_called()


class TestComputerDefends(unittest.TestCase):
    @patch('tictactoe.computer_clicks')
    def test_computer_defends_left_coloum_and_clicks_UL(self, mock_helper):
        tictactoe.player = [1,0,0,1,0,0,0,0,0] 
        tictactoe.blocked_boxes = [1,0,0,1,0,0,0,0,0]

        tictactoe.computer_defends()

        mock_helper.assert_called_once_with(tictactoe.UL)

    @patch('tictactoe.computer_clicks')
    def test_computer_defends_left_coloum_and_clicks_UL(self, mock_helper):
        tictactoe.player = [0,1,0,0,1,0,0,0,0] 
        tictactoe.blocked_boxes = [0,1,0,0,1,0,0,0,0]

        tictactoe.computer_defends()

        mock_helper.assert_called_once_with(tictactoe.UM)


class TestCaseMiddle(unittest.TestCase):

    @patch('tictactoe.computer_clicks')
    def test_case_middle_calls_computer_clicks_when_cross_count_is_one_with_OR(self, mock_helper):
        tictactoe.cross_count = 1

        tictactoe.case_middle()

        mock_helper.assert_called_once_with(tictactoe.OR)

    @patch('tictactoe.computer_clicks')
    def test_case_middle_does_not_call_computer_clicks_when_cross_count_is_not_one(self, mock_helper):
        tictactoe.cross_count = 3
        
        tictactoe.case_middle()

        mock_helper.assert_not_called()


class TestCaseEdge(unittest.TestCase):
    @patch('tictactoe.computer_clicks')
    def test_case_edge_calls_computer_clicks_when_cross_count_is_one_with_MM(self, mock_helper):
        tictactoe.cross_count = 1

        tictactoe.case_edge()

        mock_helper.assert_called_once_with(tictactoe.MM)

    @patch('tictactoe.computer_plays_to_win')
    def test_case_edge_calls_computer_plays_to_win_when_cross_count_is_not_one_computer_does_not_defend(self, mock_helper):
        tictactoe.cross_count = 3
        tictactoe.player = [1,1,0,0,0,0,0,0,0] 
        tictactoe.blocked_boxes = [1,1,1,0,0,0,0,0,0]
        tictactoe.computer = [0,0,1,0,0,0,0,0,0]
        tictactoe.on_turn = tictactoe.COMPUTER

        tictactoe.case_edge()

        mock_helper.assert_called_once()


class TestCaseCorner(unittest.TestCase):
    @patch('tictactoe.computer_puts_second_cross_on_edge')
    def test_case_corner_calls_computer_puts_second_cross_on_edge_when_cross_count_is_three(self, mock_helper):
        tictactoe.cross_count = 3

        tictactoe.case_corner()

        mock_helper.assert_called_once()

    @patch('tictactoe.computer_defends')
    def test_case_corner_does_not_call_computer_defends_when_cross_count_is_five_and_computer_wins_before(self, mock_helper):
        tictactoe.cross_count = 5
        tictactoe.player = [1,1,0,1,0,0,0,0,0] 
        tictactoe.blocked_boxes = [1,1,1,1,0,0,1,0,0]
        tictactoe.computer = [0,0,1,0,0,0,1,0,0]
        tictactoe.on_turn = tictactoe.COMPUTER

        tictactoe.case_corner()

        mock_helper.assert_not_called()


class TestComputerOnTurn(unittest.TestCase):
    @patch('tictactoe.case_middle')
    def test_computer_on_turn_calls_case_middle_when_case_was_set_to_middle(self, mock_helper):
        tictactoe.case = tictactoe.MIDDLE

        tictactoe.computer_on_turn()

        mock_helper.assert_called_once()

    @patch('tictactoe.case_corner')
    def test_computer_on_turn_calls_case_corner_when_case_was_set_to_corner(self, mock_helper):
        tictactoe.case = tictactoe.CORNER

        tictactoe.computer_on_turn()

        mock_helper.assert_called_once()


class TestReset(unittest.TestCase):
    
    def test_player_list_is_set_back_when_reset_function_was_called(self):
        tictactoe.player = [1,1,1,1,1,1,1,1,1] 

        tictactoe.reset()

        self.assertEqual(tictactoe.player, [0,0,0,0,0,0,0,0,0])

    def test_winner_is_set_back_when_reset_function_was_called(self):
        tictactoe.winner = tictactoe.COMPUTER_WINS

        tictactoe.reset()

        self.assertEqual(tictactoe.winner, tictactoe.IN_GAME)


class TestCheckComputerWins(unittest.TestCase):
    
    def test_winner_is_set_right_when_computer_wins(self):
        tictactoe.winner = tictactoe.IN_GAME
        tictactoe.computer = [1,1,1,0,0,0,0,0,0]

        tictactoe.check_computer_wins()

        self.assertEqual(tictactoe.winner, tictactoe.COMPUTER_WINS)

    def test_winner_does_not_change_when_computer_has_not_won(self):
        tictactoe.winner = tictactoe.IN_GAME
        tictactoe.computer = [1,1,0,0,0,1,0,0,0]

        tictactoe.check_computer_wins()

        self.assertEqual(tictactoe.winner, tictactoe.IN_GAME)


class TestCheckPlayerWins(unittest.TestCase):
    
    def test_winner_is_set_right_when_player_wins(self):
        tictactoe.winner = tictactoe.IN_GAME
        tictactoe.player = [1,0,0,1,0,0,1,0,0]

        tictactoe.check_player_wins()

        self.assertEqual(tictactoe.winner, tictactoe.PLAYER_WINS)

    def test_winner_does_not_change_when_player_has_not_won(self):
        tictactoe.winner = tictactoe.IN_GAME
        tictactoe.player = [1,1,0,0,0,1,0,0,0]

        tictactoe.check_player_wins()

        self.assertEqual(tictactoe.winner, tictactoe.IN_GAME)


class TestCheckDraw(unittest.TestCase):
    
    def test_all_fields_are_full_and_there_is_a_draw(self):
        tictactoe.blocked_boxes = [1,1,1,1,1,1,1,1,1] 
        tictactoe.winner = tictactoe.IN_GAME

        tictactoe.check_draw()

        self.assertEqual(tictactoe.winner, tictactoe.NO_WINNER)

    def test_not_all_fields_are_full_and_there_no_draw(self):
        tictactoe.blocked_boxes = [1,0,1,1,1,1,1,1,1] 
        tictactoe.winner = tictactoe.IN_GAME

        tictactoe.check_draw()
        
        self.assertEqual(tictactoe.winner, tictactoe.IN_GAME)


if __name__ == '__main__':
    unittest.main()