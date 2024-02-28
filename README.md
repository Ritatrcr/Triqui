This Python program allows players to play the classic game of Triqui. Players take turns placing their marks ('X' or 'O') on a 3x3 grid. The first player to get three of their marks in a row, column, or diagonal wins the game. If all cells are filled and no player achieves a winning combination, the game ends in a draw.

Instructions
Running the Game:

Run the Python script.
Follow the prompts to enter the cell number (1-9) where you want to place your mark.

Gameplay Rules:
Players take turns to place their marks on the board.
The game ends when one player wins or the board is full (resulting in a draw).

Functions
printBoard(matrix): Prints the current state of the Triqui board.
player(player): Returns the opponent's player number.
win(matrix, player): Checks if the given player has won the game.
check_win_next_move(board, player): Checks if the given player has the possibility of winning on the next move.
check_two_options(board, player): Checks if the given player has at least two options to win.


To play the game:
Run the Python script.
Follow the instructions to enter the cell number for your move.
Keep playing until one player wins or the game ends in a draw.
