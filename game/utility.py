class Utility:
    @staticmethod
    def printKeys(dict):
        for key, value in dict.items() :
            print(key,end =",")
        print()
    @staticmethod
    def printLegalMoves(list):
        print(list,sep =",")
    
    @staticmethod  
    def print_board(board):
        """Get a string representation of the board."""
        rep = ''
        rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
        for row in range(1, 9):
            begin, end = 10*row + 1, 10*row + 9
            rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
        return rep
