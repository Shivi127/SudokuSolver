## Class Sudoku
Class implementation of a Sudoku in Python.

The class takes in a String Representation of the Board, checks against Null, Invalid boards and throws Value Errors for each case. If the String Format is valid it parses the board and represents it as a 2-D List. Where[row][col] represent a cell on the sudoku.(Running from 0-8).


The Hints Associated in the board is stored in a 2-D list. Where[row][col] represent a cell on the sudoku.(Running from 0-8).
each index has a list of all the possible values that could be used to fill the board or None if the place in the board is already filled.



#API
## isValidBoard():
Return:  True if the input board is valid not necessarily solvable. 
         Valid = No valid number(1-9) occurs more than once in a row, col, box.
         Else: False

## getHintAt(rowIndex,colIndex):
Given an index if Hints are available return a list of the possiblity or None
Error Handeling  : Valid Index: List[Int] or None     
                   Invalid Index: throws IndexError
         
 ## updateHintsAt(row,col,value):
  Updates the Hints given you want to update the board[row][col] with value.
  Error Handeling  :  IndexError if index not on board
                      ValueError if value not in [0,8]
 
