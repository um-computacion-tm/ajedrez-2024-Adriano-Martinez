import unittest
from game.pieces.king import King
from game.board import Board
from game.exceptions import InvalidPieceMove

class TestKing(unittest.TestCase): 

    def setUp(self):
        """Configura el entorno de prueba antes de cada método de prueba."""
        self.__board__ = Board()  
        self.__white_king__ = King("WHITE", self.__board__)  
        self.__black_king__ = King("BLACK", self.__board__)  
        self.__board__.set_piece(4, 4, self.__white_king__)  

    def test_str(self):
        """Verifica la representación en cadena del rey blanco y negro."""
        self.assertEqual(str(self.__white_king__), "♔")
        self.assertEqual(str(self.__black_king__), "♚")

    def test_valid_moves(self):
        """Verifica que los movimientos válidos del rey sean aceptados."""
        self.assertTrue(self.__white_king__.mov_correcto(4, 4, 4, 5))  # Movimiento vertical hacia arriba
        self.assertTrue(self.__white_king__.mov_correcto(4, 4, 4, 3))  # Movimiento vertical hacia abajo
        self.assertTrue(self.__white_king__.mov_correcto(4, 4, 5, 4))  # Movimiento horizontal hacia la derecha
        self.assertTrue(self.__white_king__.mov_correcto(4, 4, 3, 4))  # Movimiento horizontal hacia la izquierda
        self.assertTrue(self.__white_king__.mov_correcto(4, 4, 5, 5))  # Movimiento diagonal hacia abajo derecha
        self.assertTrue(self.__white_king__.mov_correcto(4, 4, 3, 3))  # Movimiento diagonal hacia arriba izquierda

    def test_invalid_moves(self):
        """Verifica que se lancen excepciones para movimientos inválidos."""
        with self.assertRaises(InvalidPieceMove):
            self.__white_king__.mov_correcto(4, 4, 6, 4)  # Movimiento vertical de dos casillas
        
        with self.assertRaises(InvalidPieceMove):
            self.__white_king__.mov_correcto(4, 4, 4, 6)  # Movimiento horizontal de dos casillas
        
        with self.assertRaises(InvalidPieceMove):
            self.__white_king__.mov_correcto(4, 4, 6, 6)  # Movimiento diagonal de dos casillas

    def test_blocked_by_own_piece(self):
        """Verifica que el rey no pueda moverse a una casilla ocupada por una pieza propia."""
        self.__board__.set_piece(5, 4, King("WHITE", self.__board__))  
        with self.assertRaises(InvalidPieceMove):
            self.__white_king__.mov_correcto(4, 4, 5, 4)  

    def test_can_capture_opponent_piece(self):
        """Verifica que el rey pueda moverse a una posición ocupada por una pieza del oponente."""
        self.__board__.set_piece(5, 5, King("BLACK", self.__board__))  
        self.assertTrue(self.__white_king__.mov_correcto(4, 4, 5, 5))  # Movimiento diagonal hacia abajo derecha
    
    def test_move_to_same_color_piece(self):
        """Verifica que el rey no pueda moverse a una casilla ocupada por otra pieza del mismo color."""
        self.__board__.set_piece(5, 5, King("WHITE", self.__board__))  
        with self.assertRaises(InvalidPieceMove):
            self.__white_king__.mov_correcto(4, 4, 5, 5)  # Movimiento inválido (misma pieza)

if __name__ == "__main__":
    unittest.main()
