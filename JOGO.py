import time

def calcula_jogada(n, m):
    peças_a_retirar = 0
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:  # tem como tirar as peças
            peças_a_retirar = i
    return peças_a_retirar


def computador_escolhe_jogada(n, m):
    if n <= m:  # quando o computador pode tirar mais do que tem no tabuleiro
        time.sleep(2)
        print(f"O computador tirou {n} peças.")
        print(f"Não resta nenhuma peça no tabuleiro\n")
        proxima_jogada = n

    elif calcula_jogada(n, m) != 0:  # calcula a qtnd de peças para retirar
        proxima_jogada = calcula_jogada(n, m)
        time.sleep(2)
        print(f"O computador tirou {proxima_jogada} peças.")
        print(f"Agora restam {n - proxima_jogada} peças no tabuleiro.\n")

    else:  # retira o maior número de peças possíveis
        time.sleep(2)
        print(f"O computador tirou {m} peças.")
        print(f"Agora restam {n - m} peças no tabuleiro.\n")
        proxima_jogada = m

    return proxima_jogada


def usuario_escolhe_jogada(n, m):
    time.sleep(2)
    jogada_usuario = int(input("Informe sua jogada: "))
    while jogada_usuario <= 0 or jogada_usuario > n or jogada_usuario > m:
        print(f"Valor incorreto. O valor deve estar entre 1 e {m}, ou ser menor que a quantidade de peças disponíveis (m)")
        jogada_usuario = int(input("Informe sua jogada: "))

    print(f"\nVocê tirou {jogada_usuario} peças.")
    print(f"Agora resta {n - jogada_usuario} peças no tabuleiro.\n")

    return jogada_usuario


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    peças_restantes = n
    if n % (m + 1) == 0:  # computador deixa o usuário começar
        print("Você começa!\n")
        while peças_restantes > 0:
            # usuaŕio
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 0
                break

            # computador
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 1
                break

    else:  # computador começa a partida
        print("Computador começa!\n")
        while peças_restantes > 0:
            # jogada computador
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 1
                break

            # jogada usuaŕio
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 0
                break

    if vencedor == 1:
        print("Fim de jogo! O computador ganhou!\n")
        return 1
    else:
        print("Fim de jogo! Você ganhou!\n")
        return 0


def campeonato():
    rodada = 1
    vitorias_computador = 0
    vitorias_usuario = 0

    time.sleep(3)
    while rodada <= 3:
        print(f"**** Rodada {rodada} ****")
        vencedor = partida()
        if vencedor == 1:
            vitorias_computador += 1
        elif vencedor == 0:
            vitorias_usuario += 1
        rodada += 1

    print("**** Final do campeonato! ****\n")
    print(f"Placar: Você {vitorias_usuario} x {vitorias_computador} Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()

if __name__ == "__main__":
    main()