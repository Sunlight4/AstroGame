import pygame, enemies, objects
pygame.init()
screen=pygame.display.set_mode([640,480])
fill=screen.fill
blit=screen.blit
flip=pygame.display.flip
load=pygame.image.load
good=enemies.PoliceGood(pos=[0,320])
bad=enemies.PoliceEnemy(pos=[320,320])
solid=pygame.sprite.Group()
for i in range(0, 320, 64):
    s=enemies.SolidTile(pos=[i, 320+64])
    solid.add(s)
heroes=objects.Team()
heroes.add(good)
villains=objects.Team()
villains.add(bad)
rendered=pygame.sprite.Group()
rendered.add(good)
rendered.add(bad)
for i in solid.sprites():rendered.add(i)
while True:
    screen.fill([0,0,0])
    rendered.draw(screen)
    heroes.update({"heroes":heroes, "villains":villains, "solid":solid})
    for s in heroes.sprites():s.attack_turn()
    print heroes.sprites()[0].status
    villains.update({"heroes":heroes, "villains":villains, "solid":solid})
    for s in villains.sprites():s.attack_turn()
    flip()
