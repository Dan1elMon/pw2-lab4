
# Imprimiendo alfil alfin
#draw(bishop)
def draw_chessboard():
    board = [list(row) for row in SQUARE]  # Convertimos las filas en listas para poder modificar los elementos
    
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:  # Casilla blanca
                board[i][j] = '##'
    
    return [''.join(row) for row in board]  # Convertimos las filas nuevamente en cadenas de texto

def draw_pieces(positions):
    board = draw_chessboard()
    pieces = []
    
    for piece, pos in positions:
        piece_lines = BISHOP[:]  # Copiamos las líneas del dibujo del alfil
        
        # Colocamos el alfil en la posición correspondiente en el tablero
        for i, line in enumerate(piece_lines):
            if i < 53:
                if pos[0] + i // 3 < 8 and pos[1] < 8:
                    piece_lines[i] = line[:2] + board[pos[0] + i // 3][pos[1]:pos[1] + 8] + line[10:]
            else:
                if pos[0] + i // 3 < 8 and pos[1] < 8:
                    piece_lines[i] = line[:2] + board[pos[0] + i // 3][pos[1]:pos[1] + 8] + line[14:]
        
        pieces.append(piece_lines)
    
    return pieces

def print_board(pieces):
    rows = [''] * 64
    
    # Concatenamos las líneas de cada pieza en la posición correspondiente en el tablero
    for piece in pieces:
        for i, line in enumerate(piece):
            rows[i] += line
    
    for row in rows:
        print(row)

# Posiciones de los alfiles
positions = [(0, 0), (0, 8), (8, 0), (8, 8)]

# Dibujamos los alfiles en el tablero
pieces = draw_pieces(positions)

# Imprimimos el tablero con los alfiles
print_board(pieces)


