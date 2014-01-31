import pygame, random, characters
class Team(pygame.sprite.Group):
    """Convenience group, when characters run out of HP calls sprite.on_destroy()
then destroys it if on_destroy() returns True."""
    def update(self, kw):
        for i in self.sprites():
            if i.hp <= 0:
                try:cond=i.on_destroy()
                except NameError:cond=True
                if cond:i.kill()
            i.update(kw)
class Projectile(pygame.sprite.Sprite):
    def __init__(self, battle, img, speed=3, direction=[-1, 0], pos=[0,0], target="heroes", kind="melee", hp=1):
        self.battle=battle
        self.image=pygame.image.load(img)
        self.speed=speed
        self.direction=direction
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.target=target
        self.hp=hp
        self.kind=kind
        self.status="N/A"
        super(Projectile, self).__init__()
    def attack_turn(self):pass
    def defend(self, damage, kind):
        if self.kind==kind:pass
        else:
            self.hp-=damage
    def on_destroy(self):return 1
    def update(self, kw):
        target=kw[self.target]
        self.hp-=1
        x=pygame.sprite.spritecollide(self, target, False, pygame.sprite.collide_rect)
        if x:
            for i in x:
                dmg=random.randrange(0, self.battle)
                i.defend(dmg, self.kind)
                self.hp-=self.battle
        xspeed=self.direction[0]*self.speed
        yspeed=self.direction[1]*self.speed
        self.rect.left+=xspeed
        self.rect.top+=yspeed
class ShadowBall(pygame.sprite.Sprite):
    def __init__(self, battle, pos, img="ShadowBall.png", target="heroes"):
        self.battle=battle
        self.image=pygame.image.load(img)
        self.hp=5
        self.target=target
        self.status="DOOM"
        self.rect=self.image.get_rect(topleft=pos)
        super(ShadowBall, self).__init__()
    def defend(self, *args):pass
    def on_destroy(self):
        if random.random() < 0.25:
            good=characters.PoliceEnemy(pos=[self.rect.left, 0], hp=0.1, battle=1, speed=2)
            for i in self.groups():
                i.add(good)
            return 1
    def update(self, kw):
        self.hp-=1
        self.villains=kw["villains"]
        self.renderer=kw["rendered"]
        targets=kw[self.target]
        for i in pygame.sprite.spritecollide(self, targets, False, pygame.sprite.collide_rect):
             i.defend(self.battle, "shadow")
        



    
            
        
    
