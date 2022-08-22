import numpy as np

def displayGame(velha):
    for i in velha:
        print(i)

def changePlayerTime(player):
    if player == 2:
        return 1;
    return 2;

def isValidValueForPlay(value):
    return value <= 2

def insertGame(velha, line, colum, player):
    if velha[line][colum] == '_':
        if player == 2:
            velha[line][colum] = 'X'
        else:
            velha[line][colum] = 'O'
    else:
        print ("A posicao já está preenchida")

        
if __name__ == '__main__':
   player = 2
   print("---------------------------")
   print("Bem vindo ao jogo da velha")
   print("---------------------------")
   velha = np.array([['_', '_', '_'],['_', '_', '_'],['_', '_', '_']])
   displayGame(velha)

   while True:
        player = changePlayerTime(player)
        print(f"Bem vindo jogador {player}")
        while True:
            try:
                linhas = int(input("Informe a linha que voce quer jogar:"))
                colunas = int(input("Informe a coluna que voce quer jogar:"))
                if (isValidValueForPlay(linhas) and isValidValueForPlay(colunas)):
                    insertGame(velha, linhas, colunas, player)
                    displayGame(velha)
                    break
            except:
                 raise Exception("Invalid caracters")
        

  
  

