# Generate a list of hints
class Sudoku:
    def __init__(self):
        ''' 
        Initialization:
        self.board = List[List[Int]]
        self.hints = List[List[List[Int]]]
        self.box_identifiers = List[List]
        '''
        self.board = [[ None for i in range(9)] for i in range(9)]
        self.hints = [[ None for i in range(9)] for i in range(9)]
        self.box_identifiers = [set([i for i in range(3)]),set([i for i in range(3,6)]),set([i for i in range(6,9)])]
        
    def isValidBoard(self):
        invalid = None
        for r in range(9):
            for c in range(9):
                invalid = self.checkRow(r,c,self.board[r][c]) and self.checkCol(r,c,self.board[r][c]) and self.checkBox(r,c,self.board[r][c])
                if not invalid:
                    return invalid
        return True
    
    def checkRow(self,rowNumber,colNumber,val):
        '''
        Given a rowNumber, colNumber and value checks for the occurance of another val in the row.
        '''
        for c in range(9):
            if self.board[rowNumber][c] :
                if c!=colNumber and self.board[rowNumber][c] == val:

                    return False
        return True

    def checkCol(self,rowNumber,colNumber,val):
        '''
        Given a rowNumber, colNumber and value checks for the occurance of another val in the col.
        '''
        for r in range(9):
            if self.board[r][colNumber]:
                if r!=rowNumber and self.board[r][colNumber] == val:
                    return False
        return True

    def checkBox(self, rowNumber, colNumber, val):
        '''
        Given a rowNumber, colNumber and value checks for the occurance of another val in the box.
        '''
        rows = self.findBlockIndex(rowNumber)
        cols = self.findBlockIndex(colNumber)

        for r in rows:
            for c in cols:
                if self.board[r][c]:
                    if r!=rowNumber and c!=colNumber and self.board[r][c]==val:
                        return False

        return True

    def getHintAt(self,rowIndex,colIndex):
        '''
        Given an index if Hints are available return a list of the possiblity or None
        Return : Valid Index: List[Int] or None     
                 Invalid Index: throws IndexError
        '''
        if rowIndex<0 or rowIndex>8 or colIndex<0 or colIndex>8:
            raise IndexError("Invalid Index Requested")
        return self.hints[rowIndex][colIndex]

    def parseBoard(self, BoardString):
        '''
        Throw Expecptions when:
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
            for row in range(9):
                for col in range(9):
                    # check if the char at the position is valid
                    charAtIndex = BoardString[col+(row)*9]
                    if charAtIndex == '.':
                        self.hints[row][col] = [i for i in range(1,10)]
                    elif charAtIndex.isdigit():
                        self.board[row][col] = int(charAtIndex)
                    else:
                        raise ValueError("Invalid Board: BOARD CONTAINS INVALID CHARACTERS")
        self.updateHints()

    def updateHints(self):
        """
        Updates the Hints given the Board has been parsed.
        """
        for row in range(9):
            for col in range(9):
                if self.board[row][col]!=None:
                    value = self.board[row][col]
                    self.hints[row][col]= None
                    self.hintColUpdate(col,value)
                    self.hintRowUpdate(row,value)
                    self.hintBlockUpdate(row,col,value)
                

    def hintRowUpdate(self,rowNumber,value):
        '''
        Input:      rowNumber = INT
                    value = INT 

        Function :  Updates the Hints : ROW
        '''
        for colNumber in range(9):
            if self.hints[rowNumber][colNumber] != None:
                if value in self.hints[rowNumber][colNumber]:
                    self.hints[rowNumber][colNumber].remove(value)


    def hintColUpdate(self,colNumber,value):
        '''
        Input:      rowNumber = INT
                    value = INT 

        Function :  Updates the Hints : COL
        '''
        
        for rowNumber in range(9):
            if self.hints[rowNumber][colNumber]:
                if value in self.hints[rowNumber][colNumber]:
                    self.hints[rowNumber][colNumber].remove(value)
    
    def findBlockIndex(self,coordinate):
        for indexSet in self.box_identifiers:
            if coordinate in indexSet:
                return indexSet

    def hintBlockUpdate(self,rowNumber,colNumber,value):
        '''
        Input:      rowNumber = INT
                    value = INT 

        Function :  Updates the Hints : BOX
        '''
        rows = self.findBlockIndex(rowNumber)
        cols = self.findBlockIndex(colNumber)

        for r in rows:
            for c in cols:
                if self.hints[r][c] != None:
                    if value in self.hints[r][c]:
                        self.hints[r][c].remove(value)

    
    
        

    

            
