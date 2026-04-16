import random
import math
import time

def main():  
    nome_jogador = input('Olá, como você se chama? ')
    print(f'Que nome legal, {nome_jogador}!')
    print(f'Vamos lutar!\nVocê começa.')
    vida_jogador = 40
    vida_CPU = 40
    mana_jogador = 20

    while True:
        print(f'O que você deseja fazer? Você possuí {vida_jogador} de vida e {mana_jogador} de mana.\nSeu oponente possuí {vida_CPU} de vida.')
        escolha1 = int(input('1- Atacar\n2- Defender\n3- Conjurar uma magia\n'))

#escolha_CPU vem antes, pois caso contrário ele não consegueria defender do jeito que quero.
#Posso consertar isso depois fazendo um sistema de "speed", mas aí eu teria que pensar mais.
        defesa_CPU = False
        escolha_CPU = random.randrange(1,10)
        if escolha_CPU >= 8:
            defesa_CPU = True

        if escolha1 == 1:
            acertou = random.randrange(1,10)
            defesa = False
            if acertou <= 7:
                dano_jogador = random.randrange(3,6)
                if defesa_CPU:
                    dano_jogador //= 2
                vida_CPU -= dano_jogador
                print(f'Você o atingiu, Causando {dano_jogador} de dano e o deixando com {vida_CPU} de vida!')
            elif acertou >= 8:
                print('Você o errou!')
        elif escolha1 == 2:
            defesa = True
            print('Você defende!')
        elif escolha1 == 3:
            defesa = False
            escolha_magia = int(input('Qual magia você quer conjurar?\n1- Bola de fogo(-5 de mana)\n2- Raios(-10 de mana)\n3- Canalizar(-0 de mana)\n'))
            if escolha_magia == 1:
                if mana_jogador < 5:
                    print('Você levanta suas mãos para conjurar uma magia, porém saem somente faíscas. Talvez você tenha esquecido quanto de mana possuía?')
                else:
                    mana_jogador -= 5
                    dano_jogador = random.randrange(5,9)
                    vida_CPU -= dano_jogador
                    print(f'Você conjura uma bola de fogo e atira em seu inimigo, causando {dano_jogador} de dano a ele e o deixando com {vida_CPU} de vida!')
            elif escolha_magia == 2:
                if mana_jogador < 10:
                    print('Você levanta suas mãos para conjurar uma magia, porém saem somente faíscas. Talvez você tenha esquecido quanto de mana possuía?')
                else:
                    mana_jogador -= 10
                    atingiu_mais = random.randrange(1,11)
                    dano_jogador = random.randrange(3,6)
                    vida_CPU -= dano_jogador
                    print(f'Você conjura raios que caem dos céus e atingem seu oponente, causando {dano_jogador} de dano e o deixando com {vida_CPU} de vida!')
                    if atingiu_mais <= 6:
                        dano_jogador = random.randrange(3,6)
                        vida_CPU -= dano_jogador
                        print(f'Os raios atingem seu oponente uma vez a mais, o causando {dano_jogador} de dano e o deixando com {vida_CPU} de vida!')
            elif escolha_magia == 3:
                recuperacao_mana = random.randrange(5,11)
                mana_jogador += recuperacao_mana
                print(f'Você recupera {recuperacao_mana} de mana, ficando com {mana_jogador} no total!')
            

#Checagem de morte, caso o jogador mate o CPU antes do turno dele.
        if vida_CPU <= 0:
            print(f'Você venceu! Parabéns, {nome_jogador}!')

            break
        print('Vez da CPU!')
        if escolha_CPU <= 7:
            acertou_CPU = random.randrange(1,10)
            defesa_CPU = False
            if acertou_CPU <= 7:
                dano_CPU = random.randrange(4,9)
                if defesa:
                    dano_CPU //= 2
                vida_jogador -= dano_CPU
                print(f'Ele te atingiu! Causando {dano_CPU} de dano.')
            elif acertou_CPU >= 8:
                print('Ele te errou!')
        elif escolha_CPU >= 8:
            print('Ele defende!')

#Chegagem de morte do player, já que só é possível ele tomar dano
#Após o turno do CPU, isso é feito logo após o dito turno.
        if vida_jogador <= 0:
            print(f'Que pena, você perdeu.')
            break







if __name__ == '__main__':
    while True:
        main()
        jogar_novamente = int(input('Quer jogar novamente?\n1- Sim\n2- Não\n'))
        if jogar_novamente == 2:
            break


