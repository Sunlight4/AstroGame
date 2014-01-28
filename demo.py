import pygame, characters, objects
pygame.init()
mixer=pygame.mixer
mixer.init()
music=mixer.music
music.load("PDTheme.ogg")
music.set_volume(1)
music.play(-1)
pygame.key.set_repeat(25, 25)
screen=pygame.display.set_mode([640,480])
fill=screen.fill
blit=screen.blit
flip=pygame.display.flip
load=pygame.image.load
clock=pygame.time.Clock()
good=characters.PoliceGood(pos=[0,320])
good2=characters.Astro(pos=[32,320])
bad=characters.PoliceEnemy(pos=[320,320])
bad2=characters.Jailer(pos=[288,320])
solid=pygame.sprite.Group()
for i in range(0, 320, 64):
    s=characters.SolidTile(pos=[i, 320+64])
    solid.add(s)
s=characters.SolidTile(pos=[64, 320])
solid.add(s)
heroes=objects.Team()
heroes.add(good)
heroes.add(good2)
villains=objects.Team()
villains.add(bad)
villains.add(bad2)
rendered=pygame.sprite.Group()
rendered.add(good)
rendered.add(bad)
rendered.add(bad2)
rendered.add(good2)
for i in solid.sprites():rendered.add(i)
while True:
    screen.fill([0,0,0])
    rendered.draw(screen)
    clock.tick(30)
    heroes.update({"heroes":heroes, "villains":villains, "solid":solid, "rendered":rendered})
    for s in heroes.sprites():
        if s.status=="idle":s.attack_turn()

    villains.update({"heroes":heroes, "villains":villains, "solid":solid, "rendered":rendered})
    for s in villains.sprites():
        if s.status=="idle":s.attack_turn()
    flip()
