from pygame import * 
from random import randint
from time import sleep
win_width=500
win_height=500
window = display.set_mode((win_width,win_height))#создаем объект окна игры - и задаем ему размер
display.set_caption("MY GAME")
WHITE=(255,255,255)#Создаем белый цветс помощью RGB
RED=(255,0,0)
BLUE=(0,0,255)
FPS=150
#Создаем персонажа
hero = image.load('platform.png')#загружаем картинку
hero = transform.scale(hero,(70,30))#изменяем размеры картинки
rect1 = hero.get_rect()#создаем хитбокс
rect1.x=230
rect1.y=450
enemy =  image.load('bird.png')
enemy= transform.scale(enemy,(20,20))
rect2 = enemy.get_rect()
rect2.x=50
rect2.y=50
catched=0#пойманные
passed=0#пропущенные
font.init()#Подключаем шрифты
font24=font.SysFont('Arial',24)#Задаем параметры шрифта
text1 = font24.render("Поймано:"+str(catched),True,(255,0,0))
text2 = font24.render("Пропущенные:"+str(passed),True,(255,0,0))
text3 = font24.render('FPS '+str(FPS),True,(255,0,0))
text4 = font24.render('Победа',True,(255,0,0))
text5 = font24.render('Проигрыш',True,(255,0,0))
background=image.load('fon.png')
background=transform.scale(background,(win_width,win_height))
clock = time.Clock()
game = 'in_process'
#Запускаем основной игровой цикл
while True:
    #закрасим фон белым
    if game == 'in_process':
        window.blit(background,(0,0))
        window.blit(text1,(0,20))
        window.blit(text2,(0,40))
        window.blit(enemy,(rect2.x,rect2.y))
        window.blit(hero,(rect1.x,rect1.y))#Располагает объект в указанных координатах
        window.blit(text3,(0,60))
        display.update()#фиксируем изменения - пишется всегда в конце
        #ДВИЖЕНИЯ ВРАГА
        rect2.y+=1
        if rect2.y> win_height:
            passed+=1
            text2 = font24.render("Пропущенные:"+str(passed),True,(255,0,0))
            rect2.x = randint(0,win_width-20) 
            rect2.y = 0
        #rect1.colliderect(rect2) - проверяет столкновения хитбоксов
        #True - если есть столкновение
        if rect1.colliderect(rect2):
            catched=catched+1
            text1 = font24.render("Поймано:"+str(catched),True,(255,0,0))
            rect2.x = randint(0,win_width-20) 
            FPS = FPS+10
            text3 = font24.render('FPS '+str(FPS),True,(255,0,0))
            window.blit(text3,(0,60))
            display.update()
            rect2.y = 0
        #Управление для персонажа
        keys = key.get_pressed()
        if keys[K_LEFT] and rect1.x>0:
            rect1.x-=1
        elif keys[K_RIGHT] and rect1.x+70<win_width:
            rect1.x+=1
        if catched >= 10:
            window.blit(text4,(250,250))
            display.update()
        if passed >=10:
            window.blit(text5,(250,250))
            display.update()
    for i in event.get():
        if i.type==QUIT:
            quit()
        if i.type==KEYDOWN and game !='in_process':
             if i.key==K_SPACE:
                catched=0
                passed=0
                FPS=150
                text1 = font24.render("Поймано:"+str(catched),True,(255,0,0))
                text2 = font24.render("Пропущенные:"+str(passed),True,(255,0,0))
                text3 = font24.render('FPS '+str(FPS),True,(255,0,0))
                rect1.x=230
                rect1.y=450
                rect2.x = randint(0,win_width-20)
                rect2.y = 0 
                game='in_process'
    clock.tick(FPS)
