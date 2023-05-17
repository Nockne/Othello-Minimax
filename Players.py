from OthelloBoard import *


class Player:
    """Base player class"""
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol
    
    def get_move(self, board):
        raise NotImplementedError()
    

class HumanPlayer(Player):
    """Human subclass with text input in command line"""
    def __init__(self, symbol):
        Player.__init__(self, symbol)
        self.total_nodes_seen = 0

    def clone(self):
        return HumanPlayer(self.symbol)
        
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return  (col, row)


class AlphaBetaPlayer(Player):
    """Class for Alphabeta AI: implement functions minimax, eval_board, get_successors, get_move
    eval_type: int
        0 for H0, 1 for H1, 2 for H2
    prune: bool
        1 for alpha-beta, 0 otherwise
    max_depth: one move makes the depth of a position to 1, search should not exceed depth
    total_nodes_seen: used to keep track of the number of nodes the algorithm has searched through
    symbol: X for player 1 and O for player 2
    """
    def __init__(self, symbol, eval_type, prune, max_depth):
        Player.__init__(self, symbol)
        self.turn = 0
        self.eval_type = eval_type
        self.prune = prune
        self.max_depth = int(max_depth) 
        self.max_depth_seen = 0
        self.total_nodes_seen = 0
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'


    def terminal_state(self, board):
        # If either player can make a move, it's not a terminal state
        for c in range(board.cols):
            for r in range(board.rows):
                if board.is_legal_move(c, r, "X") or board.is_legal_move(c, r, "O"):
                    return False 
        return True 


    def terminal_value(self, board):
        # Regardless of X or O, a win is float('inf')
        state = board.count_score(self.symbol) - board.count_score(self.oppSym)
        if state == 0:
            return 0
        elif state > 0:
            return float('inf')
        else:
            return -float('inf')


    def flip_symbol(self, symbol):
        # Short function to flip a symbol
        if symbol == "X":
            return "O"
        else:
            return "X"
        

    def minimax(self, board, maxPlayer):
        temp = board.cloneOBoard()
        if self.depth == 0 or self.terminal_state(temp):
            return temp.eval_board
        
        if maxPlayer: # player 1's turn
            maxEval = 10000
            temp.children = temp.get_successors(temp, temp.p1_symbol)
            for i in temp.children:
                temp2 = temp.cloneOBoard()
                temp2.play_move(i[0],i[1], temp2.p1_symbol, False)
                val, bestMove = self.minimax(temp, maxPlayer)
                maxEval = max(maxEval, val)
                
            return maxEval
        
        if not maxPlayer: # player 2's turn
            minEval = -10000
            temp.children = temp.get_successors(temp, temp.p2_symbol)
            for i in temp.children:
                temp2 = temp.cloneOBoard()
                temp2.play_move(i[0], i[1], temp2.p2_symbol, True)
                val = self.minimax(temp, maxPlayer)
                minEval = min(minEval, val)



    def alphabeta(self, board):
        # Write minimax function here using eval_board and get_successors
        # type:(board) -> (int, int)
        col, row = 0, 0
        
        return col, row

    # takes p1 number of tiles and subtracts p2 tiles for a value
    def number_pieces(self, board):
        temp = board.cloneOBoard()
        p1_score = temp.count_score(temp, temp.p1_symbol)
        p2_score = temp.count_score(temp, temp.p2_symbol)
        value = p1_score - p2_score
        return value

    # takes p1 number of available moves - p2 number of available moves
    def mobiliy(self, board):
        temp = board.cloneOBoard()
        p1_val = len(temp.get_successors(temp.board, temp.p1_symbol))
        p2_val = len(temp.get_successors(temp.board, temp.p2_symbol))
        value = p1_val - p2_val
        return value

    def eval_board(self, board):
        # Write eval function here
        # type:(board) -> (float)
        value = 0
        # number of pieces heuristic
        if self.eval_type == 0:
            value = self.number_pieces(board)
        # number of available moves heuristic
        elif self.eval_type == 1:
            value = self.mobility(board)
        # my own heuristic
        elif self.eval_type == 2:
            value = 2
        return value


    def get_successors(self, board, player_symbol):
        # Write function that takes the current state and generates all successors obtained by legal moves
        # type:(board, player_symbol) -> (list)
        successors = []
        for i in range(0,4):
            for j in range(0,4):
                if(board.is_legal_move(board, i, j, player_symbol)):
                    validMove = [i,j]
                    successors.append(validMove)
        return successors 


    def get_move(self, board):
        # Write function that returns a move (column, row) here using minimax
        # type:(board) -> (int, int)
        return self.alphabeta(board)

       
        





