import pygame, random, objects
class PoliceGood(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=5, battle=2, img="PDGood.png", speed=4):
        self.battle=battle
        self.hp=hp
        super(PoliceGood, self).__init__()
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.status="idle"
        self.target=None
        self.speed=speed
    def defend(self, damage, kind):
        self.hp-=damage
    def attack_turn(self):
        self.status="searching"
    def on_destroy(self):return 1
    def update(self, kw):
        if self.status=="searching":
            heroes=kw["villains"]
            try:self.target=random.choice(heroes.sprites())
            except:self.status="idle"
            else:self.status="attack"
        elif self.status=="attack":
            if pygame.sprite.collide_rect(self, self.target):
                dmg=random.randint(0, self.battle)
                self.target.defend(dmg, "melee")
                self.status="idle"
            else:
                tx=self.target.rect.left
                if self.rect.left > tx:
                    self.rect.left -= self.speed
                elif self.rect.left < tx:
                    self.rect.left += self.speed
            heroes=kw["villains"]
            x=pygame.sprite.spritecollide(self, heroes, False)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False):
            self.rect.top+=3
class PoliceEnemy(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=5, battle=2, img="PDBad.png", speed=2):
        self.battle=battle
        self.hp=hp
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.status="idle"
        self.target=None
        self.speed=speed
        super(PoliceEnemy, self).__init__()
    def defend(self, damage, kind):
        self.hp-=damage
    def attack_turn(self):
        self.status="searching"
    def on_destroy(self):return 1
    def update(self, kw):
        if self.status=="searching":
            heroes=kw["heroes"]
            try:self.target=random.choice(heroes.sprites())
            except:self.status="idle"
            else:self.status="attack"
        elif self.status=="attack":
            if self.target.hp<=0:self.status="idle"
            if pygame.sprite.collide_rect(self, self.target):
                dmg=random.randint(0, self.battle)
                print dmg
                self.target.defend(dmg, "melee")
                self.status="idle"
            else:
                tx=self.target.rect.left
                if self.rect.left > tx:
                    self.rect.left -= self.speed
                elif self.rect.left < tx:
                    self.rect.left += self.speed
            heroes=kw["heroes"]
            x=pygame.sprite.spritecollide(self, heroes, False)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False):
            self.rect.top+=3
class Jailer(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=3, img="Jailer.png", speed=2, defense=1):
        self.battle=battle
        self.hp=hp
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.status="idle"
        self.target=None
        self.speed=speed
        self.defense=defense
        super(Jailer, self).__init__()
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        if dmg>0:self.hp-=dmg
    def attack_turn(self):
        self.status="searching"
    def on_destroy(self):return 1
    def update(self, kw):
        if self.status=="searching":
            heroes=kw["heroes"]
            try:self.target=heroes.sprites()[0]
            except:self.status="idle"
            else:self.status="attack"
        elif self.status=="attack":
            if self.target.hp<=0:self.status="idle"
            if pygame.sprite.collide_rect(self, self.target):
                dmg=random.randint(0, self.battle)
                self.target.defend(dmg, "melee")
                self.status="idle"
            else:
                tx=self.target.rect.left
                if self.rect.left > tx:
                    self.rect.left -= self.speed
                elif self.rect.left < tx:
                    self.rect.left += self.speed
            heroes=kw["heroes"]
            x=pygame.sprite.spritecollide(self, heroes, False)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False):
            self.rect.top+=3
class PixelBad(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=2, battle=3, img="PixelBad.png", speed=2, defense=1):
        self.battle=battle
        self.hp=hp
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.status="idle"
        self.target=None
        self.speed=speed
        self.defense=defense
        super(PixelBad, self).__init__()
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        if dmg>0:self.hp-=dmg
    def attack_turn(self):
        self.status="searching"
    def on_destroy(self):return 1
    def update(self, kw):
        if self.status=="searching":
            heroes=kw["heroes"]
            try:self.target=heroes.sprites()[0]
            except:self.status="idle"
            else:self.status="attack"
        elif self.status=="attack":
            if self.target.hp<=0:self.status="idle"
            if pygame.sprite.collide_rect(self, self.target):
                dmg=random.randint(0, self.battle)
                self.target.defend(dmg, "melee")
                self.status="idle"
            else:
                tx=self.target.rect.left
                if self.rect.left > tx:
                    self.rect.left -= self.speed
                elif self.rect.left < tx:
                    self.rect.left += self.speed
            heroes=kw["heroes"]
            x=pygame.sprite.spritecollide(self, heroes, False)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False):
            self.rect.top+=3
class Sotve(pygame.sprite.Sprite):
    powerups=[]
    def __init__(self, pos=[0,0], hp=20, battle=3, jump=12, img="Sotve.png", speed=2, defense=2):
        self.battle=battle
        self.hp=10
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.target=None
        self.speed=speed
        self.defense=defense
        self.attacking=False
        self.trying=False
        self.jump=jump
        self.attack=1
        self.status="N/A"
        super(Sotve, self).__init__()
    def on_destroy(self):return 1
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        if dmg>0:self.hp-=dmg
    def attack_turn(self):pass
    def update(self, kw):
        solid=kw["solid"]
        print "HP: "+str(self.hp)
        print "Attack: "+str(self.attack)
        print self.attacking
        villains=kw["villains"]
        for event in kw["events"]:
            if event.type==pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.rect.left-=self.speed
                elif event.key==pygame.K_RIGHT:
                    self.rect.right+=self.speed
                elif event.key==pygame.K_UP:
                    if self.jump > 0:
                        self.rect.top-=8
                        self.jump-=1
                elif event.key==pygame.K_x:
                    if self.attack >= 1:
                        self.attacking=True
                        self.attack-=1
                        
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_x:
                    self.attacking=False


        if not self.attacking:
            if self.attack < 1:
                self.attack+=0.05
        attacking=self.attack > 0 and self.attacking
        if attacking:
            proj=objects.Projectile(img="FireR.png", battle=2, hp=20, speed=4,
                                    pos=self.rect.topleft, direction=[1,0], target="villains")
            kw["heroes"].add(proj)
            kw["rendered"].add(proj)
        if not pygame.sprite.spritecollide(self, solid, False):
            self.rect.top+=3
        else:
            self.jump=12
        self.attacking=False
class Lionel(pygame.sprite.Sprite):
    powerups=["Gold Jewel"]
    def __init__(self, pos=[0,0], hp=20, battle=2, jump=12, img="Lionel.png", speed=4, defense=1):
        self.battle=battle
        self.hp=10
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.target=None
        self.speed=speed
        self.defense=defense
        self.attacking=False
        self.trying=False
        self.jump=jump
        self.attack=10
        self.status="N/A"
        super(Lionel, self).__init__()
    def on_destroy(self):return 1
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        if dmg>0:self.hp-=dmg
    def attack_turn(self):pass
    def update(self, kw):
        solid=kw["solid"]
        print "HP: "+str(self.hp)
        print "Attack: "+str(self.attack)
        print self.attacking
        villains=kw["villains"]
        for event in kw["events"]:
            if event.type==pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.rect.left-=self.speed
                elif event.key==pygame.K_RIGHT:
                    self.rect.right+=self.speed
                elif event.key==pygame.K_UP:
                    if self.jump > 0:
                        self.rect.top-=8
                        self.jump-=1
                elif event.key==pygame.K_c:
                    if self.attack > 0:
                        self.attacking=True
                        self.attack-=1

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_c:
                    self.attacking=False
                elif event.key==pygame.K_d:
                    self.image=pygame.image.load("Lionel.png")

        if self.attacking:
            self.image=pygame.image.load("LionelAttack.png")
        else:
            self.image=pygame.image.load("Lionel.png")
        if not self.attacking:
            if self.attack < 10:
                self.attack+=1
        attacking=self.attack > 0 and self.attacking
        if attacking:
            x=pygame.sprite.spritecollide(self, kw["villains"], False)
            if x:
                for sprite in x:
                    sprite.defend(random.randrange(0, self.battle), "melee")
        if not pygame.sprite.spritecollide(self, solid, False):
            self.rect.top+=3
        else:
            self.jump=12
class GhostAstro(pygame.sprite.Sprite):
    powerups=[]
    def __init__(self, pos=[0,0], hp=20, battle=3, jump=12, img="GhostAstro.png", speed=4, defense=1):
        self.battle=battle
        self.hp=10
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.target=None
        self.speed=speed
        self.defense=defense
        self.attacking=False
        self.trying=False
        self.jump=jump
        self.attack=3
        self.status="N/A"
        super(GhostAstro, self).__init__()
    def on_destroy(self):return 1
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        if dmg>0:self.hp-=dmg
    def attack_turn(self):pass
    def update(self, kw):
        solid=kw["solid"]
        print "HP: "+str(self.hp)
        print "Attack: "+str(self.attack)
        print self.attacking
        villains=kw["villains"]
        for event in kw["events"]:
            if event.type==pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.rect.left+=self.speed
                elif event.key==pygame.K_RIGHT:
                    self.rect.right-=self.speed
                elif event.key==pygame.K_UP:
                    if self.jump > 0:
                        self.rect.top-=8
                        self.jump-=1
                elif event.key==pygame.K_z:
                    if self.attack > 0:
                        self.attacking=True
                        self.attack-=1
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_z:
                    self.attacking=False


        if not self.attacking:
            if self.attack < 3:
                self.attack+=1
        x=pygame.sprite.spritecollide(self, kw["heroes"], False)
        for sprite in x:
            sprite.hp-=0.1
        attacking=self.attack > 0 and self.attacking
        if attacking:
            proj=objects.Projectile(img="Bullet.png", battle=2, hp=10, speed=8,
                                    pos=self.rect.topleft, direction=[-1,0], target="heroes")
            kw["villains"].add(proj)
            kw["rendered"].add(proj)
        if not pygame.sprite.spritecollide(self, solid, False):
            self.rect.top+=3
        else:
            self.jump=12
class Astro(pygame.sprite.Sprite):
    powerups=["Pure Crystal"]
    def __init__(self, pos=[0,0], hp=20, battle=3, jump=12, img="Astro.png", speed=4, defense=1):
        self.battle=battle
        self.hp=10
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.target=None
        self.speed=speed
        self.defense=defense
        self.attacking=False
        self.trying=False
        self.jump=jump
        self.attack=3
        self.status="N/A"
        super(Astro, self).__init__()
    def on_destroy(self):return 1
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        if dmg>0:self.hp-=dmg
    def attack_turn(self):pass
    def update(self, kw):
        solid=kw["solid"]
        print "HP: "+str(self.hp)
        print "Attack: "+str(self.attack)
        print self.attacking
        villains=kw["villains"]
        for event in kw["events"]:
            if event.type==pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.rect.left-=self.speed
                elif event.key==pygame.K_RIGHT:
                    self.rect.right+=self.speed
                elif event.key==pygame.K_UP:
                    if self.jump > 0:
                        self.rect.top-=8
                        self.jump-=1
                elif event.key==pygame.K_z:
                    if self.attack > 0:
                        self.attacking=True
                        self.attack-=1
                elif event.key==pygame.K_a and "Pure Crystal" in self.powerups:
                    if self.attack > 0:
                        sb = objects.ShadowBall(battle=self.battle, pos=self.rect.topleft, target="villains", img="EnergyBall.png")
                        self.attack = -2
                        kw["heroes"].add(sb)
                        kw["rendered"].add(sb)
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_z:
                    self.attacking=False


        if not self.attacking:
            if self.attack < 3:
                self.attack+=1
        attacking=self.attack > 0 and self.attacking
        if attacking:
            proj=objects.Projectile(img="Bullet.png", battle=2, hp=10, speed=8,
                                    pos=self.rect.topleft, direction=[1,0], target="villains")
            kw["heroes"].add(proj)
            kw["rendered"].add(proj)
        if not pygame.sprite.spritecollide(self, solid, False):
            self.rect.top+=3
        else:
            self.jump=12
class Shado(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=15, battle=3, img="Shado.png", speed=2, defense=0):
        self.battle=battle
        self.hp=hp
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.status="idle"
        self.target=None
        self.speed=speed
        self.defense=defense
        super(Shado, self).__init__()
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        if dmg>0:self.hp-=dmg
    def attack_turn(self):
        self.status="searching"
    def on_destroy(self):return 1
    def update(self, kw):
        print "Boss HP: "+str(self.hp)
        if self.status=="searching":
            heroes=kw["heroes"]
            try:self.target=heroes.sprites()[0]
            except:self.status="idle"
            else:self.status="attack"
        elif self.status=="attack":
            if self.target.hp<=0:self.status="idle"
            if pygame.sprite.collide_rect(self, self.target):
                dmg=random.randint(0, self.battle)
                self.target.defend(dmg, "melee")
                self.status="idle"
            else:
                tx=self.target.rect.left
                if self.rect.left > tx:
                    self.rect.left -= self.speed
                elif self.rect.left < tx:
                    self.rect.left += self.speed
            heroes=kw["heroes"]
            x=pygame.sprite.spritecollide(self, heroes, False)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False):
            self.rect.top+=3
class SolidTile(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="Tile.png", speed=4, defense=1):
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        super(SolidTile, self).__init__()
class PixelTile(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="PixelTile.png", speed=4, defense=1):
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        super(PixelTile, self).__init__()

 
        
