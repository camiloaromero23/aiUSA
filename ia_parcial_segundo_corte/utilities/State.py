"""
Juan José Montenegro Pulido
Camilo Andrés Romero Maldonado
Clases para manejar estados de cada uno de los ejercicios.
La clase TicTacToeState se refiere al estado del triqui minimax
La clase AlphaBetaState se refiere al estado del triqui con poda alfa beta
La clase SudokuState se refiere al estado de ambos ejercicios con el Sudoku
 """


class TicTacToeState:

    def __init__(self, board):
        self.board = board
        self.children = []
        self.value = None

    def __str__(self):
        return self.board.__str__()

    def __repr__(self):
        return '\n' + self.__str__() + '\n'

    def addChild(self, new_child):
        self.children.append(new_child)

    def __eq__(self, other_state):
        return (self.board == other_state.board).all()


class AlphaBetaState(TicTacToeState):

    def __init__(self, board, parent=None):
        super().__init__(board)
        self.parent = parent


class SudokuState:

    def __init__(self, board, value=None):
        self.board = board
        self.value = value

    def __str__(self):
        return self.board.__str__()

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other_state):
        return ((self.board == other_state.board).all())
