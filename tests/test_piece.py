import unittest
from game.pieces.piece import Piece
from game.board import Board  

class TestPiece(unittest.TestCase):
    """
    Clase de prueba para la clase Piece. Utiliza la biblioteca unittest para 
    verificar el comportamiento y la funcionalidad de las piezas de ajedrez.
    """

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba. Inicializa un tablero 
        y una pieza blanca para ser utilizados en las pruebas.
        """
        self.__board__ = Board()  
        self.__piece__ = Piece("white", self.__board__)  

    def test_get_color(self):
        """
        Prueba que el método get_color devuelve el color correcto de la pieza.
        Se espera que devuelva "white".
        """
        self.assertEqual(self.__piece__.get_color(), "white")
    
    def test_str(self):
        """
        Prueba la representación en cadena de la pieza. Se espera que
        devuelva una cadena vacía, lo que indica que no se ha definido 
        un método __str__ significativo en la clase Piece.
        """
        self.assertEqual(str(self.__piece__), "")
    
    def test_mov_correcto(self):
        """
        Prueba que el método mov_correcto lanza un NotImplementedError.
        Esto se espera porque el método no está implementado en la clase base 
        Piece y debe ser sobrescrito en las subclases.
        """
        with self.assertRaises(NotImplementedError):
            self.__piece__.mov_correcto(0, 0, 1, 1)

    def test_mov_correcto_invalid_position(self):
        """
        Prueba que el método mov_correcto devuelve False para posiciones 
        inválidas fuera del rango del tablero.
        Se espera que devuelva False si las coordenadas están fuera de los 
        límites del tablero.
        """
        self.assertFalse(self.__piece__.mov_correcto(-1, 0, 1, 1))  # from_x es inválido
        self.assertFalse(self.__piece__.mov_correcto(0, 0, 8, 1))  # to_x es inválido

    def test_mov_correcto_same_position(self):
        """
        Prueba que si las coordenadas de origen y destino son las mismas,
        el método mov_correcto devuelve False, ya que no se puede mover la pieza.
        """
        self.assertFalse(self.__piece__.mov_correcto(0, 0, 0, 0))

    def test_is_position_valid(self):
        """
        Prueba el método is_position_valid para verificar si las posiciones 
        son válidas. Se esperan resultados específicos para posiciones válidas 
        e inválidas.
        """
        self.assertTrue(Piece.is_position_valid(0, 0))  # (0, 0) es válido
        self.assertTrue(Piece.is_position_valid(7, 7))  # (7, 7) es válido
        self.assertFalse(Piece.is_position_valid(-1, 0))  # (-1, 0) es inválido
        self.assertFalse(Piece.is_position_valid(8, 8))  # (8, 8) es inválido
    
    def test_valid_positions(self):
        """
        Prueba el método valid_positions para determinar si se pueden mover 
        a una posición específica en el tablero. Verifica que el movimiento 
        es válido cuando el destino está vacío y que es inválido cuando 
        el destino no es accesible.
        """
        self.__board__.set_piece(0, 1, None)  # Posición vacía
        self.assertTrue(self.__piece__.valid_positions(0, 0, 0, 1))
        self.assertFalse(self.__piece__.valid_positions(0, 0, 7, 7))

    def test_scan_direction(self):
        """
        Prueba el método scan_direction para escanear posiciones en 
        una dirección dada desde la posición inicial. Verifica que 
        las posiciones accesibles se devuelvan correctamente, 
        incluyendo las posiciones ocupadas por piezas enemigas y 
        excluyendo las ocupadas por piezas aliadas.
        """
        self.__board__.set_piece(1, 0, None)  # Posición vacía
        possibles = self.__piece__.scan_direction(0, 0, 1, 0)
        self.assertIn((1, 0), possibles)  # Debe incluir (1, 0)

        enemy_piece = Piece("black", self.__board__)
        self.__board__.set_piece(2, 0, enemy_piece)  # Coloca una pieza enemiga
        possibles = self.__piece__.scan_direction(0, 0, 1, 0)
        self.assertIn((2, 0), possibles)  # Debe incluir (2, 0)

        ally_piece = Piece("white", self.__board__)
        self.__board__.set_piece(3, 0, ally_piece)  # Coloca una pieza aliada
        possibles = self.__piece__.scan_direction(0, 0, 1, 0)
        self.assertNotIn((3, 0), possibles)  # No debe incluir (3, 0)

if __name__ == "__main__":
    unittest.main()
