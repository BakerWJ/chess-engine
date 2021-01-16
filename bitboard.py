"""
Code pertaining to representation of the chess board
"""


class Board:
    """
    Dataclass using bitboards to represent board state.
    Arrays go A1, B1, C1, D1 ... E8, F8, H8, G8
    """
    w_king = []
    b_king = []
    w_queen = []
    b_queen = []
    w_rook = []
    b_rook = []
    w_bishop = []
    b_bishop = []
    w_knight = []
    b_knight = []
    w_pawn = []
    b_pawn = []

    def __init__(self) -> None:
        self.w_king = [0] * 4 + [1] + [0] * 59
        self.b_king = 60 * [0] + [1] + 3 * [0]
        self.w_queen = [0] * 3 + [1] + [0] * 60
        self.b_queen = 59 * [0] + [1] + 4 * [0]
        self.w_rook = [1] + 6 * [0] + [1] + 56 * [0]
        self.b_rook = 56 * [0] + [1] + 6 * [0] + [1]
        self.w_bishop = 2 * [0] + [1] + 2 * [0] + [1] + 58 * [0]
        self.b_bishop = 56 * [0] + [0] * 2 + [1] + 2 * [0] + [1] + 2 * [0]
        self.w_knight = [0, 1] + 4 * [0] + [1] + 57 * [0]
        self.b_knight = 57 * [0] + [1] + 4 * [0] + [1] + [0]
        self.w_pawn = [0] * 8 + [1] * 8 + 48 * [0]
        self.b_pawn = 48 * [0] + 8 * [1] + 8 * [0]

    def print_board(self) -> None:
        """
        Outputs the board in string form
        """
        pieces = [self.w_king, self.b_king, self.w_bishop, self.b_bishop,
                  self.w_rook, self.b_rook, self.w_queen, self.b_queen,
                  self.w_knight, self.b_knight, self.w_pawn, self.b_pawn]
        names = ['k', 'K', 'b', 'B', 'r', 'R', 'q', 'Q', 'n', 'N', 'p', 'P']
        empty_board = ['E'] * 64
        for i in range(len(pieces)):
            print(names[i])
            for p in range(64):
                if pieces[i][p] != 0:
                    empty_board[p] = names[i]
        print(empty_board)
