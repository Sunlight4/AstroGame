import characters, objects, pygame, easygui
def astroHouse():
    good=characters.Astro(pos=[0,320])
    #good2=characters.PoliceGood(pos=[32,320])
    #good3=characters.Door(pos=[256, 320], room=room2)
    
    solid=pygame.sprite.Group()
    for i in range(0, 320, 64):
        s=characters.WoodTile(pos=[i, 320+64])
        solid.add(s)
    for i in range(320, 640, 64):
        s=characters.WoodTile(pos=[i, 530])
        solid.add(s)
    for i in range(384, 640, 64):
        s=characters.WoodTile(pos=[i, 320-128])
        solid.add(s)

    s=characters.WoodTile(pos=[64, 320])
    solid.add(s)
    s=characters.WoodTile(pos=[128, 320])
    solid.add(s)
    s=characters.WoodTile(pos=[128, 320-64])
    solid.add(s)
    s=characters.WoodTile(pos=[192, 320-64])
    solid.add(s)
    s=characters.WoodTile(pos=[384, 320+128])
    s=characters.WoodTile(pos=[320, 320+128])
    solid.add(s)

    heroes=objects.Team()
    heroes.add(good)
    #heroes.add(good2)
    #heroes.add(good3)
    rendered=pygame.sprite.Group()
    rendered.add(good)
    #rendered.add(good2)
    for i in solid.sprites():rendered.add(i)
    #rendered.add(good3)
    #rendered.add(good4)
    return [heroes, objects.Team(), solid, rendered, "AmberCity.ogg", [239,169,119]]



def oldroom():
    easygui.msgbox("POLICE OFFICER:Yikes! What's going on? Protect yourself with the Z key.")
    good=characters.Astro(pos=[0,320])
    good2=characters.PoliceGood(pos=[32,320])
    #good3=characters.Lionel(pos=[64, 320])
    #good4=characters.Ostra(pos=[96, 320])
    #good3=characters.Door(pos=[128, 320], room=room1)
    bad=characters.PoliceEnemy(pos=[256,320])
    bad2=characters.PoliceEnemy(pos=[288,320])
    solid=pygame.sprite.Group()
    for i in range(0, 320, 64):
        s=characters.WoodTile(pos=[i, 320+64])
        solid.add(s)
    for i in range(320, 640, 64):
        s=characters.WoodTile(pos=[i, 530])
        solid.add(s)
    for i in range(384, 640, 64):
        s=characters.WoodTile(pos=[i, 320-128])
        solid.add(s)
    #good4=characters.Door(pos=[i, 320-176], room=room3)
    s=characters.WoodTile(pos=[64, 320])
    solid.add(s)
    s=characters.WoodTile(pos=[128, 320])
    solid.add(s)
    s=characters.WoodTile(pos=[128, 320-64])
    solid.add(s)
    s=characters.WoodTile(pos=[192, 320-64])
    solid.add(s)
    s=characters.WoodTile(pos=[384, 320+128])
    s=characters.WoodTile(pos=[320, 320+128])
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
    return [heroes, villains, solid, rendered, "PDTheme.ogg"]


