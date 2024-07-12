import pygame #biblioteca de jogo
pygame.init() #para abrir pygame

#aplicar a dimensão da janela
#dimensão do plano de fundo
window = pygame.display.set_mode([1280,665])


#aplicar o título da janela/display
pygame.display.set_caption('Futebol SENAI')

#criar variáveis para as imagens:

campo = pygame.image.load("Imagens/field.png")
jogador1 = pygame.image.load("Imagens/player1.png")
jogador2 = pygame.image.load("Imagens/player2.png")
bola = pygame.image.load("Imagens/ball.png")
menu = pygame.image.load("Imagens/bar.png")

#colocar a bolinha para rolar
bola_x = 617
bola_y = 337

def draw():
    #carregar as imagens
    window.blit(campo,(0,0))
    window.blit(jogador1,(50,310))
    window.blit(jogador2,(1150,310))
    window.blit(bola,(bola_x,bola_y))

def move_bola():
    global bola_x
    #para mover a bola para a direita
    bola_x+=1



#para manter a janela aberta:
loop = True
while loop:
    for event in pygame.event.get():
        #se ele clicar em X irá fechar
        if event.type == pygame.QUIT:
            loop = False
    draw()
    move_bola()
    #quero que atualize sempre quando houver mudança
    pygame.display.update()


pygame.quit() #para fechar o pygame