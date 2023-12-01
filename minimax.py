from jogo_da_velha import branco, icone, verificaGanha

def movimentoIA(board, jogador):
    possibilidades = pegarPosicoes(board)
    melhorValor = None
    melhor_mov = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = icone[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco
        print(possibilidade, valor)
        if(melhorValor is None):
            melhorValor = valor
            melhor_mov = possibilidade
        elif(jogador == 0):
            if(valor > melhorValor):
                melhorValor = valor
                melhor_mov = possibilidade
        elif(jogador == 1):
            if(valor < melhorValor):
                melhorValor = valor
                melhor_mov = possibilidade

    return melhor_mov[0], melhor_mov[1]

def pegarPosicoes(board):
    posicoes = []
    for i in range (3):
        for j in range(3):
            if(board[i][j] == branco):
                posicoes.append([i, j])

    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1

}

def minimax(board, jogador):
    ganhador = verificaGanha(board)
    if(ganhador):
        return score[ganhador]
    jogador = (jogador + 1)%2

    possibilidades = pegarPosicoes(board)
    melhorValor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = icone[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = branco

        if(melhorValor is None):
            melhorValor = valor
        elif(jogador == 0):
            if(valor > melhorValor):
                melhorValor = valor
        elif(jogador == 1):
            if(valor < melhorValor):
                melhorValor = valor

    return melhorValor
