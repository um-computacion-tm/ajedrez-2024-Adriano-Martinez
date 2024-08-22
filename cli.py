from chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))  #De la fila
        from_col = int(input("From col: "))  #De la columna
        to_row = int(input("To Row: "))      #A la fila
        to_col = int(input("To Col: "))      #A la columna
        # :)
        chess.move(from_row, from_col, to_row,to_col)

    except Exception as e:
        print("error", e)
        return 
    

if __name__ == '__main__':
    main()