from jogo_da_velha import criarb, fazMov, inputValido, printb, verificaGanha, verificaMov

from minimax import movimentoIA

jogador = 0
board = criarb()
ganhador = verificaGanha(board)
while(not ganhador):
    printb(board)
    print("----------------")
    if(jogador == 0):
        i,j = movimentoIA(board, jogador)
    else:
        i = inputValido("Digite a linha: ")
        j = inputValido("Digite a coluna: ")
    
    if (verificaMov(board, i, j)):
        fazMov(board, i, j, jogador)
        jogador = (jogador + 1)%2
    else:
        print("A posição informada já está preenchida")

    ganhador = verificaGanha(board)

print("----------------")
print("Ganhador = ", ganhador)
print("----------------")