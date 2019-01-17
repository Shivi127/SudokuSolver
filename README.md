## Class Sudoku
Class implementation of a Sudoku in Python.

The class takes in a String Representation of the Board, checks against Null, Invalid boards and throws Value Errors for each case. If the String Format is valid it parses the board and represents it as a 2-D List. Where[row][col] represent a cell on the sudoku.(Running from 0-8).
The Hints Associated in the board is stroed in a 2-D list. Where[row][col] represent a cell on the sudoku.(Running from 0-8).
each index has a list of all the possible values that could be used to fill the board or None if the place in the board is already filled.
