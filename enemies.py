class PoliceEnemy(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="PoliceEnemy.png", speed=3):
        self.battle=battle
        self.hp=hp
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
    def update(self, **kw):
        if self.status=="searching":
            heroes=kw["heroes"]
            self.target=random.choice(heroes.sprites())
            self.status="attack"
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
class Jailer(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], hp=10, battle=2, img="Jailer.png", speed=3, defense=1):
        self.battle=battle
        self.hp=hp
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=pos
        self.status="idle"
        self.target=None
        self.speed=speed
        self.defense=defense
    def defend(self, damage, kind):
        defense=random.randint(0, self.defense)
        dmg=damage-defense
        self.hp-=dmg
    def attack_turn(self):
        self.status="searching"
    def on_destroy(self):return 1
    def update(self, **kw):
        if self.status=="searching":
            heroes=kw["heroes"]
            self.target=random.choice(heroes.sprites())
            self.status="attack"
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