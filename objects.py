import pygame, random
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
    def attack_turn(self):pass
    def defend(self, damage, kind):
        if self.kind==kind:pass
        else:
            self.hp-=damage
    def update(self, **kw):
        target=kw[self.target]
        x=pygame.sprite.spritecollide(self, target, False)
        if x:
            for i in x:
                i.defend(self.battle, self.kind)
                self.hp-=self.battle
        xspeed=self.direction[0]*self.speed
        yspeed=self.direction[1]*self.speed
        self.rect.left+=xspeed
        self.rect.top+=yspeed



    
            
        
    
