branco = " "
icone = ["X", "O"]


def criarb():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return board

def printb(board):
    for i in range(3):
        print("|".join(board[i]))
        if (i < 2):
            print("-----")

def inputValido(mensagem):
    try:
        n = int(input(mensagem))
        
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("só existem linhas do 1 até o 3, digite um número válido.")
            return inputValido(mensagem)
        
    except:
        print("Número não válido")
        return inputValido(mensagem)


def verificaMov(board, i, j):
    if (board[i][j] == branco):
        return True
    else:
        return False


def fazMov(board, i, j, jogador):
    board[i][j] = icone[jogador]




def verificaGanha(board):
    for i in range(3):
        # linhas
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
            return board[i][0]
        # colunas
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
            return board[0][i]
        # diagonais
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != branco):
        return board[0][0]
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != branco):
        return board[0][2]
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                return False
            
    return "EMPATE"


