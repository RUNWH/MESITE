import pygame

#короче тут размер и название
pygame.init()
size=(1200,567)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("МОЙ ШЕДЕВЕР")
sound_effect=pygame.mixer.Sound("МОНСТРИК.wav")
#КАРТИНКА И ГРАФА
image=pygame.image.load("knight.png")
x=200
y=89
velocity_x = 0.0
velocity_y = 0.0
acceleration_x = 0.1
acceleration_y = 0.5
gravity = 0.5
jump_height = 10
jumping = False
screen.blit(image,(x,y))

done= False
clock=pygame.time.Clock()

while not done:
    for event in pygame.event.get():        #ОБРАБОТка событий
        if event.type== pygame.QUIT:
            done=True
        elif event.type==pygame.KEYDOWN:
            if event.key== pygame.K_ESCAPE:
                done=True
            if event.key == pygame.K_LEFT:
                velocity_x = -5
            elif event.key == pygame.K_RIGHT:
                velocity_x = 5
            elif event.key== pygame.K_SPACE and not jumping:
                velocity_y = -jump_height
                jumping = True
                sound_effect.play()  
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and velocity_x < 0:
                    velocity_x = 0
            elif event.key == pygame.K_RIGHT and velocity_x > 0:
                    velocity_x = 0
        

    velocity_y += gravity
    y += velocity_y
        # Применение закона упругости
   
    x += velocity_x
    velocity_x += acceleration_x
    if velocity_x > 5:
        velocity_x = 5
    elif velocity_x < -5:
        velocity_x = -5

    
    screen.fill((255, 255, 255))
    screen.blit(image,(x,y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()