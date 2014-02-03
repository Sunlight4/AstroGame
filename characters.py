import pygame, random, objects, rooms, load
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
            if pygame.sprite.collide_mask(self, self.target):
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
            x=pygame.sprite.spritecollide(self, heroes, False, pygame.sprite.collide_mask)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False, pygame.sprite.collide_mask):
            self.rect.top+=3
class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=5, battle=2, img="Ghost.png", speed=4):
        self.battle=battle
        self.hp=hp
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.status="idle"
        self.target=None
        self.speed=speed
        super(Ghost, self).__init__()
    def defend(self, damage, kind):
        self.hp-=damage
    def attack_turn(self):
        self.status="attack"
    def on_destroy(self):return 1
    def update(self, kw):
        if self.status=="attack":
            shots=random.randrange(5)
            for i in range(shots):
                proj=objects.Projectile(img="BulletL.png", battle=4, hp=48, speed=8,
                                        pos=self.rect.topleft)
                kw["villains"].add(proj)
                kw["rendered"].add(proj)
            self.status="idle"
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False, pygame.sprite.collide_mask):
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
        self.status="attack"
    def on_destroy(self):return 1
    def update(self, kw):
        if self.status=="attack":
            shots=random.randrange(5)
            for i in range(shots):
                proj=objects.Projectile(img="BulletL.png", battle=2, hp=32, speed=4,
                                        pos=self.rect.topleft)
                kw["villains"].add(proj)
                kw["rendered"].add(proj)
            self.status="idle"
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False, pygame.sprite.collide_mask):
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
            if pygame.sprite.collide_mask(self, self.target):
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
            x=pygame.sprite.spritecollide(self, heroes, False, pygame.sprite.collide_mask)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False, pygame.sprite.collide_mask):
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
            if pygame.sprite.collide_mask(self, self.target):
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
            x=pygame.sprite.spritecollide(self, heroes, False, pygame.sprite.collide_mask)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False, pygame.sprite.collide_mask):
            self.rect.top+=3
class Sotve(pygame.sprite.Sprite):
    powerups=[]
    selected=True
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
                if event.key==pygame.K_LEFT and self.selected:
                    self.rect.left-=self.speed
                elif event.key==pygame.K_RIGHT and self.selected:
                    self.rect.right+=self.speed
                elif event.key==pygame.K_UP and self.selected:
                    if self.jump > 0:
                        self.rect.top-=8
                        self.jump-=1
                elif event.key==pygame.K_x:
                    if self.attack >= 1:
                        self.attacking=True
                        self.attack-=1
                elif event.key==pygame.K_q:
                    self.selected=False
                elif event.key==pygame.K_w:
                    self.selected=True
                elif event.key==pygame.K_e:
                    self.selected=False
                elif event.key==pygame.K_r:
                    self.selected=False
                elif event.key==pygame.K_SPACE:
                    self.selected=True
                        
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_x:
                    self.attacking=False

        if self.selected:
            self.image=pygame.image.load("Sotve_selected.png")
        else:
            self.image=pygame.image.load("Sotve.png")
        if not self.attacking:
            if self.attack < 1:
                self.attack+=0.05
        attacking=self.attack > 0 and self.attacking
        if attacking:
            proj=objects.Projectile(img="FireR.png", battle=2, hp=20, speed=4,
                                    pos=self.rect.topleft, direction=[1,0], target="villains")
            kw["heroes"].add(proj)
            kw["rendered"].add(proj)
        if not pygame.sprite.spritecollide(self, solid, False, pygame.sprite.collide_mask):
            self.rect.top+=3
        else:
            self.jump=12
        self.attacking=False
class Lionel(pygame.sprite.Sprite):
    powerups=["Gold Sword"]
    selected=True
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
        self.gold_attack=False
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
                if event.key==pygame.K_LEFT and self.selected:
                    self.rect.left-=self.speed
                elif event.key==pygame.K_RIGHT and self.selected:
                    self.rect.right+=self.speed
                elif event.key==pygame.K_UP and self.selected:
                    if self.jump > 0:
                        self.rect.top-=8
                        self.jump-=1
                elif event.key==pygame.K_c:
                    if self.attack > 0:
                        self.attacking=True
                        self.attack-=1
                elif event.key==pygame.K_q:
                    self.selected=False
                elif event.key==pygame.K_w:
                    self.selected=False
                elif event.key==pygame.K_e:
                    self.selected=True
                elif event.key==pygame.K_r:
                    self.selected=False
                elif event.key==pygame.K_SPACE:
                    self.selected=True
                elif event.key==pygame.K_d and "Gold Sword" in self.powerups:
                    self.gold_attack=True
                    self.attack-=1
                    

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_c:
                    self.attacking=False
                elif event.key==pygame.K_d:
                    self.gold_attack=False



        if not self.attacking and not self.gold_attack:
            if self.attack < 10:
                self.attack+=1
        attacking=self.attack > 0 and self.attacking
        gold_attack=self.attack > 0 and self.gold_attack
        if gold_attack:
            x=pygame.sprite.spritecollide(self, kw["villains"], False, pygame.sprite.collide_mask)
            if x:
                for sprite in x:
                    sprite.defend((self.battle + self.attack), "melee")
        elif attacking:
            x=pygame.sprite.spritecollide(self, kw["villains"], False, pygame.sprite.collide_mask)
            if x:
                for sprite in x:
                    sprite.defend((self.battle + self.attack) // 2, "melee")
        if self.gold_attack:
            self.image=pygame.image.load("LionelGoldAttack.png")
        elif self.attacking:
            self.image=pygame.image.load("LionelAttack.png")
        elif self.selected:
            self.image=pygame.image.load("Lionel_selected.png")
        else:
            self.image=pygame.image.load("Lionel.png")
        if gold_attack:self.attack-=1
        if not pygame.sprite.spritecollide(self, solid, False, pygame.sprite.collide_mask):
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
        x=pygame.sprite.spritecollide(self, kw["heroes"], False, pygame.sprite.collide_mask)
        for sprite in x:
            sprite.hp-=0.1
        attacking=self.attack > 0 and self.attacking
        if attacking:
            proj=objects.Projectile(img="Bullet.png", battle=2, hp=10, speed=8,
                                    pos=self.rect.topleft, direction=[-1,0], target="heroes")
            kw["villains"].add(proj)
            kw["rendered"].add(proj)
        if not pygame.sprite.spritecollide(self, solid, False, pygame.sprite.collide_mask):
            self.rect.top+=3
        else:
            self.jump=12
class Ostra(pygame.sprite.Sprite):
    powerups=["Pure Crystal"]
    selected=True
    def __init__(self, pos=[0,0], hp=20, battle=2, jump=16, img="Astro.png", speed=8, defense=2):
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
        super(Ostra, self).__init__()
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
                if event.key==pygame.K_LEFT and self.selected:
                    self.rect.left-=self.speed
                elif event.key==pygame.K_RIGHT and self.selected:
                    self.rect.right+=self.speed
                elif event.key==pygame.K_UP and self.selected:
                    if self.jump > 0:
                        self.rect.top-=8
                        self.jump-=1
                elif event.key==pygame.K_v:
                    if self.attack > 0:
                        self.attacking=True
                        self.attack-=1
                elif event.key==pygame.K_f and "Pure Crystal" in self.powerups:
                    if self.attack > 0:
                        sb = objects.ShadowBall(battle=self.battle, pos=self.rect.topleft, target="villains", img="ShadowBall.png")
                        self.attack = -2
                        kw["villains"].add(sb)
                        kw["rendered"].add(sb)
                elif event.key==pygame.K_q:
                    self.selected=False
                elif event.key==pygame.K_w:
                    self.selected=False
                elif event.key==pygame.K_e:
                    self.selected=False
                elif event.key==pygame.K_r:
                    self.selected=True
                elif event.key==pygame.K_SPACE:
                    self.selected=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_v:
                    self.attacking=False

        if self.selected:
            self.image=pygame.image.load("Ostra_selected.png")
        else:
            self.image=pygame.image.load("Ostra.png")
        if not self.attacking:
            if self.attack < 3:
                self.attack+=1
        attacking=self.attack > 0 and self.attacking
        if attacking:
            proj=objects.Projectile(img="Bullet.png", battle=1, hp=10, speed=16,
                                    pos=self.rect.topleft, direction=[1,0], target="villains")
            kw["heroes"].add(proj)
            kw["rendered"].add(proj)
        if not pygame.sprite.spritecollide(self, solid, False, pygame.sprite.collide_mask):
            self.rect.top+=3
        else:
            self.jump=16
class Astro(pygame.sprite.Sprite):
    powerups=["Pure Crystal"]
    selected=True
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
                if event.key==pygame.K_LEFT and self.selected:
                    self.rect.left-=self.speed
                elif event.key==pygame.K_RIGHT and self.selected:
                    self.rect.right+=self.speed
                elif event.key==pygame.K_UP and self.selected:
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
                        kw["villains"].add(sb)
                        kw["rendered"].add(sb)
                elif event.key==pygame.K_q:
                    self.selected=True
                elif event.key==pygame.K_w:
                    self.selected=False
                elif event.key==pygame.K_e:
                    self.selected=False
                elif event.key==pygame.K_r:
                    self.selected=False
                elif event.key==pygame.K_SPACE:
                    self.selected=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_z:
                    self.attacking=False

        if self.selected:
            self.image=pygame.image.load("Astro_selected.png")
        else:
            self.image=pygame.image.load("Astro.png")
        if not self.attacking:
            if self.attack < 3:
                self.attack+=1
        attacking=self.attack > 0 and self.attacking
        if attacking:
            proj=objects.Projectile(img="Bullet.png", battle=2, hp=10, speed=8,
                                    pos=self.rect.topleft, direction=[1,0], target="villains")
            kw["heroes"].add(proj)
            kw["rendered"].add(proj)
        if not pygame.sprite.spritecollide(self, solid, False, pygame.sprite.collide_mask):
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
            if pygame.sprite.collide_mask(self, self.target):
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
            x=pygame.sprite.spritecollide(self, heroes, False, pygame.sprite.collide_mask)
            if x:
                for sprite in x:
                    dmg=random.randint(0, self.battle)
                    self.target.defend(dmg, "melee")
        solid_group=kw["solid"]
        if not pygame.sprite.spritecollide(self, solid_group, False, pygame.sprite.collide_mask):
            self.rect.top+=3
class SolidTile(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="Grass.png", speed=4, defense=1):
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
class WoodTile(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="WoodBlock.png", speed=4, defense=1):
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        super(WoodTile, self).__init__()
class Door(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="Door.png", speed=4, defense=1, room=None):
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.room=room
        self.hp=10
        self.status="Being a door"
        super(Door, self).__init__()
    def defend(self, *args):pass
    def update(self,kw):
        for i in kw["events"]:
            if i.type==pygame.KEYDOWN and i.key==pygame.K_SPACE:
                kw["heroes"].remove(self)
                x=pygame.sprite.spritecollide(self, kw["heroes"], False, pygame.sprite.collide_mask)
                if x:
                    load.loadroom(self.room)
                kw["heroes"].add(self)
class CityTile(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="Metal.png", speed=4, defense=1):
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        super(CityTile, self).__init__()
         
