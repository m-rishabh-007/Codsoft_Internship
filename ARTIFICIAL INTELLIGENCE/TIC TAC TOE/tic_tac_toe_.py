"""                     IC-TAC-TOE AI
    Implement an AI agent that plays the classic game of Tic-Tac-Toe
    against a human player. You can use algorithms like Minimax with
    or without Alpha-Beta Pruning to make the AI player unbeatable.
    This project will help you understand game theory and basic search
    algorithms                                                     """
import logging

# Set up logging
logging.basicConfig(filename='tictactoe.log', level=logging.DEBUG)

# Constants for player symbols
PLAYER_X = 'X'
PLAYER_O = 'O'

class TicTacToeGame:
    """A class representing the game logic for Tic Tac Toe."""

    def __init__(self):
        """Initialize the game board."""
        self.board = self.create_board()

    def create_board(self):
        """Create a new game board."""
        return [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        """Print the game board."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        """Check if the game board is full."""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_winner(self, player):
        """Check if the specified player has won the game."""
        # Check rows
        for row in self.board:
            if row.count(player) == 3:
                return True

        # Check columns
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count(player) == 3:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def get_empty_cells(self):
        """Get a list of empty cells on the game board."""
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    empty_cells.append((row + 1, col + 1))
        return empty_cells

    def make_move(self, row, col, player):
        """Make a move on the game board."""
        if self.board[row-1][col-1] == ' ':
            self.board[row-1][col-1] = player
            return True
        return False

    def minimax(self, depth, maximizing_player, alpha, beta):
        """
        Implement the minimax algorithm with alpha-beta pruning.

        This function recursively explores the game tree to find the optimal move
        for the current player. It uses the minimax algorithm to evaluate the game
        positions, and it uses alpha-beta pruning to ignore branches that don't
        need to be explored.

        Args:
        depth: The current depth in the game tree.
        maximizing_player: True if the current player is the maximizing player, False otherwise.
        alpha: The best value that the maximizing player can achieve.
        beta: The best value that the minimizing player can achieve.

        Returns:
        The minimax value of the current game position.
        """
        logging.debug(f"minimax - depth: {depth}, maximizing_player: {maximizing_player}, alpha: {alpha}, beta: {beta}")
        if self.is_winner(PLAYER_X):
            return 1 / depth
        elif self.is_winner(PLAYER_O):
            return -1 / depth
        elif self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for row, col in self.get_empty_cells():
                if self.board[row-1][col-1] == ' ':
                    self.board[row-1][col-1] = PLAYER_X
                    eval_score = self.minimax(depth + 1, False, alpha, beta)
                    self.board[row-1][col-1] = ' '
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for row, col in self.get_empty_cells():
                if self.board[row-1][col-1] == ' ':
                    self.board[row-1][col-1] = PLAYER_O
                    eval_score = self.minimax(depth + 1, True, alpha, beta)
                    self.board[row-1][col-1] = ' '
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break
            return min_eval

    def get_best_move(self):
        """Get the best move for the 'X' player."""
        best_score = float('-inf')
        best_move = None
        for row, col in sorted(self.get_empty_cells(), key=lambda x: (abs(x[0] - 2), abs(x[1] - 2))):
            if self.board[row-1][col-1] == ' ':
                self.board[row-1][col-1] = PLAYER_X
                move_score = self.minimax(1, False, float('-inf'), float('inf'))
                self.board[row-1][col-1] = ' '
                if move_score > best_score:
                    best_score = move_score
                    best_move = (row, col)
        return best_move

def play_game(game):
    """Play a game of Tic Tac Toe."""
    print("Welcome to Tic-Tac-Toe!")
    game.print_board()
    while not game.is_board_full():
        move_made = False
        while not move_made:
            try:
                row = int(input("Enter the row (1-3): "))
                if row not in [1, 2, 3]:
                    print("Invalid input. Please enter numbers between 1 and 3.")
                    continue
                col = int(input("Enter the column (1-3): "))
                if col not in [1, 2, 3]:
                    print("Invalid input. Please enter numbers between 1 and 3.")
                    continue
                move_made = game.make_move(row, col, PLAYER_O)
                if not move_made:
                    print("Invalid move. The selected cell is already occupied. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
        game.print_board()
        if game.is_winner(PLAYER_O):
            print("You win!")
            return
        if game.is_board_full():
            print("It's a tie!")
            return
        print("AI's turn...")
        best_move = game.get_best_move()
        if best_move is not None:
            ai_row, ai_col = best_move
            game.make_move(ai_row, ai_col, PLAYER_X)
            game.print_board()
        if game.is_winner(PLAYER_X):
            print("AI wins!")
            return
    print("It's a tie!")

# Testing functions
def test_create_board():
    """Test the create_board method."""
    game = TicTacToeGame()
    assert game.create_board() == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], "Error in create_board()"

def test_make_move():
    """Test the make_move method."""
    game = TicTacToeGame()
    assert game.make_move(1, 1, PLAYER_X) == True, "Error in make_move()"
    assert game.board == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], "Error in make_move()"

def test_is_winner():
    """Test the is_winner method."""
    game = TicTacToeGame()
    game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert game.is_winner(PLAYER_X) == True, "Error in is_winner()"

def test_get_empty_cells():
    """Test the get_empty_cells method."""
    game = TicTacToeGame()
    game.board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert game.get_empty_cells() == [(1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)], "Error in get_empty_cells()"

def test_minimax():
    """Test the minimax method."""
    game = TicTacToeGame()
    game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', ' ', ' ']]
    assert game.minimax(0, True, float('-inf'), float('inf')) == 1, "Error in minimax()"

def test_get_best_move():
    """Test the get_best_move method."""
    game = TicTacToeGame()
    game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', ' ', ' ']]
    assert game.get_best_move() == (3, 1), "Error in get_best_move()"

# Run the tests
test_create_board()
test_make_move()
test_is_winner()
test_get_empty_cells()
test_minimax()
test_get_best_move()

# Create a new game and play
game = TicTacToeGame()
play_game(game)
