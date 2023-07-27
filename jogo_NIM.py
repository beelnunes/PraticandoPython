#### Jogo NIM ####

def computador_escolhe_jogada(n,m):
    """
    Recebe quantas pecas estarao no tabuleiro
    e qual o numero maximo de pecas que podem ser
    retiradas em um so jogada.
    Devolve um numero inteiro que o computador deve
    retirar do tabuleiro.
    """
    x = 1
    
    while x <= m:
        restante = n - x
        if restante % (m + 1) == 0: # Quando o meu restante= 0 funciona pq o python considera que 0 % int = 0
            return x
        else:
            x = x + 1

    return m

def usuario_escolhe_jogada(n,m):
    """
    Recebe quantas pecas estarao no tabuleiro
    e qual o numero maximo de pecas que podem ser
    retiradas em uma so jogada

    Solicita que o jogador informe sua jogada e
    verifica se o valor informado e valido.

    Se o valor informado for valido, a funcao deve
    devolve-lo; caso contrario, deve solicitar
    novamente ao usuario que informe uma jogada
    valida.
    """


    xvalido = False
    
    while not xvalido:
        x = int(input("Quantas pecas voce vai tirar? "))
        xvalido = (x >= 1) and (x <= m) and (x <= n)
        if xvalido:
            return x
        else:
            print ("Oops! Jogada invalida! Tente de novo.")
    

def partida():

    # Receber e conferir se n >= m
    nmvalido = False

    while not nmvalido:
        n = int(input("Quantas pecas? "))
        m = int(input("Limite de pecas por jogada? "))
        nmvalido = (n >= m)
        if not nmvalido:
            print ("Oops! Jogada invalida! Tente de novo.")


    # Decidir quem comeca o jogo e dar inicio a partida
    if n % (m+1) == 0:
        print ("Voce comeca!")
        while n >= 0: # e se for n >0?
            z = usuario_escolhe_jogada(n,m)
            restante = n - z
            n = restante
            print ("Voce tirou", z," peca(s), agora restam", n," peca(s)")
            if n == 0:
                return "Voce ganhou!"
                

            y = computador_escolhe_jogada(n,m)
            restante = n - y
            n = restante
            print ("Computador tirou", y," peca(s), agora restam", n," peca(s)")
            if n == 0:
                return "Computador ganhou!"
         
    else:
        print ("Computador comeca!")
        while n >= 0:
            y = computador_escolhe_jogada(n,m)
            restante = n - y
            n = restante
            print ("Computador tirou", y," peca(s), agora restam", n," peca(s)")
            if n == 0:
                return "Computador ganhou!"

            z = usuario_escolhe_jogada(n,m)
            restante = n - z
            n = restante
            print ("Voce tirou", z," peca(s), agora restam", n," peca(s)")
            if n == 0:
                return "Voce ganhou!"


def campeonato():

    usuario = 0
    computador = 0
    for i in range(3):
        rodada = i + 1
        print ('**** Rodada', rodada, '****')
        
        w = partida()
        print(w)
        if w == "Voce ganhou!":
            usuario = usuario + 1
        else:
            computador = computador + 1

    placar = 'Placar: Voce', usuario, 'X', computador, ' Computador'

    return placar


def main():
    opcao = int(input('Bem-vindo ao jogo do NIM! Escolha:'
                      '1 - para jogar uma partida'
                      '2 - para jogar um campeonato'))
    if opcao == 1:
        print ('Voce escolheu uma partida!')
        print(partida())
    else:
        print ('Voce escolheu um campeonato!')
        print(campeonato())


main()
