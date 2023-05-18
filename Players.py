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
        self.eval_type = eval_type
        self.prune = prune
        self.max_depth = int(max_depth) 
        self.max_depth_seen = 0
        self.total_nodes_seen = 0
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.count = 0


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
        

    def minimax(self, board, depth, maxPlayer):
        self.count += 1
        self.total_nodes_seen += 1
        bestMove = None
        temp = board.cloneOBoard()
        if self.terminal_state(temp) or depth == 0:
            return self.eval_board(board), bestMove
        
        if maxPlayer: # max player turn
            maxEval = -1000
            temp.children = self.get_successors(temp, temp.p1_symbol) # get successors from current state
            for i in temp.children: # for each successor...
                temp2 = temp.cloneOBoard() # create a new board

                temp2.play_move(i[0],i[1], temp2.p1_symbol) # play the successor move on new board
                val = self.minimax(temp2, depth - 1, False) # recursive call to minimax for all next successors
                if val[0] >= maxEval:
                    maxEval = val[0]
                    bestMove = i
                
            return maxEval, bestMove
        
        if not maxPlayer: # min player turn
            minEval = 1000
            temp.children = self.get_successors(temp, temp.p2_symbol)
            for i in temp.children:
                temp2 = temp.cloneOBoard()
                temp2.play_move(i[0], i[1], temp2.p2_symbol)
                val = self.minimax(temp2, depth - 1, True)
                if val[0] <= minEval:
                    minEval = val[0]
                    bestMove = i
            return minEval, bestMove


    def minimax_prune(self, board, depth, alpha, beta, maxPlayer):
        self.count += 1
        self.total_nodes_seen += 1
        bestMove = None
        temp = board.cloneOBoard()
        if self.terminal_state(temp) or depth == 0:
            return self.eval_board(board), bestMove
        
        if maxPlayer: # max player turn
            maxEval = -1000
            temp.children = self.get_successors(temp, temp.p1_symbol) # get successors from current state
            for i in temp.children: # for each successor...
                temp2 = temp.cloneOBoard() # create a new board
                temp2.play_move(i[0],i[1], temp2.p1_symbol) # play the successor move on new board
                val = self.minimax(temp2, depth - 1, False) # recursive call to minimax for all next successors
                if val[0] >= maxEval:
                    maxEval = val[0]
                    bestMove = i
                alpha = max(alpha, val[0])
                if beta <= alpha:
                    break
            return maxEval, bestMove
        
        if not maxPlayer: # min player turn
            minEval = 1000
            temp.children = self.get_successors(temp, temp.p2_symbol)
            for i in temp.children:
                temp2 = temp.cloneOBoard()
                temp2.play_move(i[0], i[1], temp2.p2_symbol)
                val = self.minimax(temp2, depth - 1, True)
                if val[0] <= minEval:
                    minEval = val[0]
                    bestMove = i
                beta = min(beta, val[0])
                if beta <= alpha:
                    break
            return minEval, bestMove


    def alphabeta(self, board):
        # Write minimax function here using eval_board and get_successors
        # type:(board) -> (int, int)
        col, row = 0, 0
        if(self.prune == '1'):

            if self.symbol == "X": # if alphabeta is p1
                val, bestMove = self.minimax_prune(board, self.max_depth, -1000, 1000, True)
            if self.symbol == "O": # if alphabeta is p2
                val, bestMove = self.minimax_prune(board, self.max_depth, -1000, 1000, False)
        else:
            if self.symbol == "X": # if alphabeta is p1
                val, bestMove = self.minimax(board, self.max_depth, True)
            if self.symbol == "O": # if alphabeta is p2
                val, bestMove = self.minimax(board, self.max_depth, False)
        col = bestMove[0]
        row = bestMove[1]
        return col, row

    # takes p1 number of tiles and subtracts p2 tiles for a value
    def number_pieces(self, board):
        temp = board.cloneOBoard()
        p1_score = temp.count_score(temp.p1_symbol)
        p2_score = temp.count_score(temp.p2_symbol)
        value = p1_score - p2_score
        return value

    # takes p1 number of available moves - p2 number of available moves
    def mobility(self, board):
        p1_val = len(self.get_successors(board, board.p1_symbol))
        p2_val = len(self.get_successors(board, board.p2_symbol))
        value = p1_val - p2_val
        return value

    def eval_board(self, board):
        # Write eval function here
        # type:(board) -> (float)
        value = 0
        # number of pieces heuristic
        if self.eval_type == '0':
            value = self.number_pieces(board)
        # number of available moves heuristic
        elif self.eval_type == '1':
            value = self.mobility(board)
        # my own heuristic
        elif self.eval_type == '2':
            value = 2
        return value


    def get_successors(self, board, player_symbol):
        # Write function that takes the current state and generates all successors obtained by legal moves
        # type:(board, player_symbol) -> (list)
        successors = []
        for i in range(0,4):
            for j in range(0,4):
                if(board.is_legal_move(i, j, player_symbol)):
                    validMove = [i,j]
                    successors.append(validMove)
        return successors 


    def get_move(self, board):
        # Write function that returns a move (column, row) here using minimax
        # type:(board) -> (int, int)
        self.count = 0
        return self.alphabeta(board)

       
        





