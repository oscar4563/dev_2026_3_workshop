import random


class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        opciones_validas = {"piedra", "papel", "tijera"}
        j1 = jugador1.lower()
        j2 = jugador2.lower()

        if j1 not in opciones_validas:
            return jugador1
        if j2 not in opciones_validas:
            return jugador2

        if j1 == j2:
            return "empate"
        
        gana_jugador1 = (
            (j1 == "piedra" and j2 == "tijera") or
            (j1 == "tijera" and j2 == "papel") or
            (j1 == "papel" and j2 == "piedra")
        )
        
        if gana_jugador1:
            return "jugador1"
        else:
            return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        # Revisar filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]
        
        # Revisar columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]
        
        # Revisar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]
        
        # Revisar si hay casillas vacías
        for fila in tablero:
            for celda in fila:
                if celda == " ":
                    return "continua"
        
        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        if not (0 <= hasta_fila <= 7 and 0 <= hasta_col <= 7):
            return False
        if not (0 <= desde_fila <= 7 and 0 <= desde_col <= 7):
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] is not None and tablero[desde_fila][col] != " ":
                    return False
        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] is not None and tablero[fila][desde_col] != " ":
                    return False
        
        return True