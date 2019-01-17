import unittest
from sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku()

    def test_parseBoard_None(self):
        board = None
        self.assertRaises(ValueError,self.sudoku.parseBoard,board)
    
    def test_parseBoard_Empty(self):
        board = ""
        self.assertRaises(ValueError,self.sudoku.parseBoard,board)

    def test_parseBoard_Small(self):
        board = ".5....3"
        self.assertRaises(ValueError,self.sudoku.parseBoard,board)

    def test_parseBoard_Large(self):
        board = ".5....3"+'.'*81
        self.assertRaises(ValueError,self.sudoku.parseBoard,board)
    
    def test_parseBoard_InvalidCharacter(self):
        board = "."*80 +"u"
        self.assertRaises(ValueError,self.sudoku.parseBoard,board)

    def test_parseBoard_EmptyValid(self):
        board = ""
        for i in range(81):
            board+='.'
        self.sudoku.parseBoard(board)
        temp_empty = [[None]*9]*9
        self.assertEqual(temp_empty, self.sudoku.board)

    def test_parseBoard_ValidBoard(self):
        board = "1"
        for i in range(80):
            board+='.'
        self.sudoku.parseBoard(board)
        temp_empty = [[ None for i in range(9)] for i in range(9)]
        temp_empty[0][0] = 1
        print("")
        self.assertEqual(temp_empty, self.sudoku.board)

    def test_HintsForEmptyBoard(self):
        board = ""
        for i in range(81):
            board+='.'
        self.sudoku.parseBoard(board)
        hints = [[[i for i in range(1,10)]for i in range(9)] for i in range(9)]
        self.assertEqual(hints, self.sudoku.hints)

    def test_HintsForNonEmptyBoard(self):
        board = "1"
        for i in range(80):
            board+='.'

        self.sudoku.parseBoard(board)
        hints = [[[i for i in range(1,10)]for i in range(9)] for i in range(9)]
        # Remove from Row
        for i in range(9):
            hints[0][i].remove(1)
        # Remove from Column
        for col in range(9):
            if 1 in hints[col][0]:
                hints[col][0].remove(1)
        # Remove from BOX

        for i in range(3):
            for j in range(3):
                if 1 in hints[i][j]:
                    hints[i][j].remove(1)

        hints[0][0] = None
        self.assertEqual(hints, self.sudoku.hints)
        
    def test_getHintsAt_Valid(self):
        board = "1"
        for i in range(80):
            board+='.'
        self.sudoku.parseBoard(board)
        actual_hints = [i for i in range(2,10)]
        retrieved_hints = self.sudoku.getHintAt(0,1)
        self.assertEqual(actual_hints, retrieved_hints)
    
    def test_getHintsAt_Invalid(self):
        board = "1"
        for i in range(80):
            board+='.'
        self.sudoku.parseBoard(board)
        self.assertRaises(IndexError,self.sudoku.getHintAt,-1,5)
    
    def test_isValidBoard_True(self):
        board = "1"
        for i in range(80):
            board+='.'
        self.sudoku.parseBoard(board)
        self.assertEqual(True, self.sudoku.isValidBoard())
    
    def test_isValidBoard_False(self):
        board = "11"
        for i in range(79):
            board+='.'
        self.sudoku.parseBoard(board)
        self.assertEqual(False, self.sudoku.isValidBoard())
