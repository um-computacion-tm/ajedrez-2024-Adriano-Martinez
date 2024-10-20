import unittest
from game.board import Board
from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.exceptions import PieceNotFound, InvalidMove, OutOfBoard

class TestBoard(unittest.TestCase):

    def setUp(self):
        """
        Inicializa un tablero nuevo antes de cada prueba.
        """
        self.__board__ = Board()

    def test_str_board(self):
        """
        Verifica la representación en cadena del tablero inicial.

        Compara la salida de la función str del tablero con la representación
        esperada que muestra las piezas en sus posiciones iniciales.
        """
        expected_str = (
            "  a b c d e f g h\n"
            "8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
            "7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
            "6 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "4 . . . . . . . . \n"
            "3 . . . . . . . . \n"
            "2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
            "1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
        )
        self.assertEqual(str(self.__board__), expected_str)

    def test_initialization(self):
        """
        Verifica que el tablero inicial tenga las piezas correctas.

        Asegura que las piezas estén colocadas correctamente en sus filas iniciales
        y que las posiciones intermedias estén vacías.
        """
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)
        self.assertIsInstance(self.__board__.get_piece(1, 0), Pawn)
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.__board__.get_piece(row, col))
    
    def test_remove_piece(self):
        """
        Verifica la funcionalidad de eliminar piezas del tablero.

        Asegura que al eliminar una pieza, esta ya no esté presente en el tablero,
        y que se lancen las excepciones adecuadas si se intenta eliminar una
        pieza que no existe o si se intenta eliminar fuera de los límites del tablero.
        """
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)  
        self.__board__.remove_piece(0, 0)
        self.assertIsNone(self.__board__.get_piece(0, 0))

        with self.assertRaises(PieceNotFound):
            self.__board__.remove_piece(0, 0)

        with self.assertRaises(OutOfBoard):
            self.__board__.remove_piece(8, 0)

    def test_move_piece(self):
        """
        Verifica la funcionalidad de mover piezas en el tablero.

        Asegura que una pieza se mueva correctamente a una nueva posición,
        que se lance una excepción si se intenta mover una pieza que no existe,
        y que no se permita capturar piezas del mismo color.
        """
        self.__board__.mover_pieza(1, 0, 3, 0)
        self.assertIsInstance(self.__board__.get_piece(3, 0), Pawn)
        self.assertIsNone(self.__board__.get_piece(1, 0))

        with self.assertRaises(PieceNotFound):
            self.__board__.mover_pieza(1, 0, 3, 0)

        self.__board__.set_piece(2, 0, Pawn("WHITE", self.__board__))
        with self.assertRaises(InvalidMove):
            self.__board__.mover_pieza(3, 0, 2, 0)

    def test_move_piece_out_of_board(self):
        """
        Verifica que se lancen excepciones al intentar mover piezas fuera del tablero.

        Asegura que se lancen excepciones adecuadas si se intenta mover una pieza
        desde o hacia posiciones fuera de los límites del tablero.
        """
        with self.assertRaises(OutOfBoard):
            self.__board__.mover_pieza(8, 0, 3, 0)
        with self.assertRaises(OutOfBoard):
            self.__board__.mover_pieza(0, 8, 3, 0)

    def test_get_piece(self):
        """
        Verifica la funcionalidad para obtener piezas del tablero.

        Asegura que se pueda obtener la pieza correcta y que se lancen excepciones
        si se intenta acceder a posiciones fuera de los límites del tablero.
        """
        piece = self.__board__.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.get_color(), "BLACK")

        with self.assertRaises(OutOfBoard):
            self.__board__.get_piece(-1, 0)
        with self.assertRaises(OutOfBoard):
            self.__board__.get_piece(8, 0)

    def test_remove_all_pieces(self):
        """
        Verifica la eliminación de todas las piezas de un color del tablero.

        Asegura que se puedan eliminar todas las piezas de un color especificado
        y que las piezas de otro color permanezcan en el tablero.
        """
        self.__board__.set_piece(0, 0, Rook("WHITE", self.__board__))
        self.__board__.set_piece(1, 0, Pawn("WHITE", self.__board__))
        self.__board__.set_piece(6, 0, Pawn("BLACK", self.__board__))

        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)
        self.assertIsInstance(self.__board__.get_piece(1, 0), Pawn)

        self.__board__.remove_all_pieces("WHITE")

        self.assertIsNone(self.__board__.get_piece(0, 0))
        self.assertIsNone(self.__board__.get_piece(1, 0))
        self.assertIsInstance(self.__board__.get_piece(6, 0), Pawn)
        self.assertEqual(self.__board__.get_piece(6, 0).get_color(), "BLACK")
    
    def test_set_piece_out_of_board(self):
        """
        Verifica que se lancen excepciones al intentar colocar piezas fuera del tablero.

        Asegura que se lancen excepciones adecuadas si se intenta colocar una pieza
        en una posición fuera de los límites del tablero.
        """
        with self.assertRaises(OutOfBoard):
            self.__board__.set_piece(8, 0, Rook("WHITE", self.__board__))
        with self.assertRaises(OutOfBoard):
            self.__board__.set_piece(0, 8, Rook("WHITE", self.__board__))
        with self.assertRaises(OutOfBoard):
            self.__board__.set_piece(-1, 0, Rook("WHITE", self.__board__))

    def test_move_piece_invalid_move(self):
        """
        Verifica que se lancen excepciones al intentar realizar un movimiento inválido.

        Asegura que no se pueda mover una pieza a una posición ocupada por una
        pieza del mismo color, lanzando la excepción correspondiente.
        """
        self.__board__.set_piece(0, 0, Rook("WHITE", self.__board__))
        self.__board__.set_piece(1, 0, Pawn("WHITE", self.__board__))

        with self.assertRaises(InvalidMove):
            self.__board__.mover_pieza(0, 0, 1, 0)

    def test_no_king_alive(self):
        """
        Verifica la funcionalidad para comprobar si hay reyes en el tablero.

        Asegura que se devuelva False si no hay reyes de ningún color en el tablero.
        """
        empty_board = [[None for _ in range(8)] for _ in range(8)]
        self.__board__.__positions__ = empty_board
        
        result_white_king = self.__board__.is_king_alive("WHITE")
        result_black_king = self.__board__.is_king_alive("BLACK")

        self.assertFalse(result_white_king)
        self.assertFalse(result_black_king)

if __name__ == "__main__":
    unittest.main()
