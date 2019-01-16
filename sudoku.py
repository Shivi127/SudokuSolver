# Generate a list of hints
class Sudoku:
    def __init__(self):
        ''' 
        Initialization:
        self.board = List[List[Int]]
        self.hints = List[List[List[Int]]]
        2-D array that stores a list of possible values at that location
        '''
        self.board = [[0]*9]*9 
        self.hints = [[None]*9]*9 

    def getHints(self,rowIndex,colIndex):
        '''
        Given an index if Hints are available return a list of the possiblity or None
        Return : List[Int] or None
        '''
        return self.hints[rowIndex][colIndex]

    def parseBoard(self, BoardString):
        '''
        Throw Expceptions when:
            Case 1: String == None
            Case 2: len(string) != 81
            Case 3: String contains invalid characters
        Else Parse
        '''
        if BoardString== None:
            raise ValueError("Invalid Board: EMPTY BOARD")
        elif len(BoardString)!= 81 :
            raise ValueError("Invalid Board: INVALID SIZE BOARD")

        else:
            # Fill in self.board 
            for row in range(9):
                for col in range(9):
                    # check if the char at the position is valid
                    charAtIndex = BoardString[col+(row)*9]
                    if charAtIndex == '.':
                        self.hints[row][col] = [i for i in range(1,10)]
                        continue
                    elif charAtIndex.isdigit():
                        if int(charAtIndex)<0 or int(charAtIndex)>9:
                            # This case will not be reached as we are looking at one characters at a time.
                            raise ValueError("Invalid Board : BOARD CONTAINS INVALID VALUE" )
                        self.board[row][col] = int(charAtIndex)
                    else:
                        raise ValueError("Invalid Board: BOARD CONTAINS INVALID CHARACTERS")

    def hintRowUpdate(self):
        pass
    def hintColUpdate(self):
        pass
    def hintBlockUpodate(self):
        pass
    

            
