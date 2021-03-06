import pygame, characters, objects
pygame.init()
mixer=pygame.mixer
mixer.init()
music=mixer.music
music.load("AmberCity.ogg")
music.set_volume(1)
music.play(-1)
pygame.key.set_repeat(10, 10)
screen=pygame.display.set_mode([640,480])
fill=screen.fill
blit=screen.blit
flip=pygame.display.flip
load=pygame.image.load
clock=pygame.time.Clock()
good=characters.Astro(pos=[0,320])
good2=characters.PoliceGood(pos=[32,320])
good3=characters.Lionel(pos=[64, 320])
good4=characters.Ostra(pos=[96, 320])
bad=characters.PoliceEnemy(pos=[320,320])
bad2=characters.PoliceEnemy(pos=[288,320])
solid=pygame.sprite.Group()
for i in range(0, 320, 64):
    s=characters.CityTile(pos=[i, 320+64])
    solid.add(s)
for i in range(320, 640, 64):
    s=characters.CityTile(pos=[i, 530])
    solid.add(s)
for i in range(384, 640, 64):
    s=characters.CityTile(pos=[i, 320-128])
    solid.add(s)

s=characters.CityTile(pos=[64, 320])
solid.add(s)
s=characters.CityTile(pos=[128, 320])
solid.add(s)
s=characters.CityTile(pos=[128, 320-64])
solid.add(s)
s=characters.CityTile(pos=[192, 320-64])
solid.add(s)
s=characters.CityTile(pos=[384, 320+128])
s=characters.CityTile(pos=[320, 320+128])
solid.add(s)

heroes=objects.Team()
heroes.add(good)
heroes.add(good2)
#heroes.add(good3)
#heroes.add(good4)
villains=objects.Team()
villains.add(bad)
villains.add(bad2)
rendered=pygame.sprite.Group()
rendered.add(good)
rendered.add(bad)
rendered.add(bad2)
rendered.add(good2)
#rendered.add(good3)
#rendered.add(good4)
for i in solid.sprites():rendered.add(i)
while True:
    screen.fill([255,255,255])
    rendered.draw(screen)
    clock.tick(30)
    events=pygame.event.get()
    heroes.update({"heroes":heroes, "villains":villains, "solid":solid, "rendered":rendered,
                   "events":events})
    for s in heroes.sprites():
        if s.status=="idle":s.attack_turn()

    villains.update({"heroes":heroes, "villains":villains, "solid":solid, "rendered":rendered,
                     "events":events})
    for s in villains.sprites():
        if s.status=="idle":s.attack_turn()
    flip()
