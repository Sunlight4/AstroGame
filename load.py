import pygame, random
def loadroom(room):
    pygame.init()
    mixer=pygame.mixer
    mixer.init()
    music=mixer.music
    heroes, villains, solid, rendered, music_name, bg=room()
    print villains.sprites()
    music.load(music_name)
    music.set_volume(0.5)
    music.play(-1)
    pygame.key.set_repeat(10, 10)
    screen=pygame.display.set_mode([640,480])
    fill=screen.fill
    blit=screen.blit
    flip=pygame.display.flip
    load=pygame.image.load
    clock=pygame.time.Clock()
    while True:
        screen.fill(bg)
        rendered.draw(screen)
        clock.tick(30)
        events=pygame.event.get()
        heroes.update({"heroes":heroes, "villains":villains, "solid":solid, "rendered":rendered,
                       "events":events})

        villains.update({"heroes":heroes, "villains":villains, "solid":solid, "rendered":rendered,
                         "events":events})
        for s in villains.sprites():
            if s.status=="idle" and random.random() < 0.075:s.attack_turn()
        flip()
