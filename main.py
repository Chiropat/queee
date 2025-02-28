@namespace
class SpriteKind:
    pez = SpriteKind.create()
    chrome = SpriteKind.create()
    Enemy_2 = SpriteKind.create()
    pez_dsef = SpriteKind.create()
    pomelo = SpriteKind.create()
@namespace
class StatusBarKind:
    vida_pez = StatusBarKind.create()
    vida_chrome = StatusBarKind.create()
    vida_dem_sef = StatusBarKind.create()
    pez_par = StatusBarKind.create()
    vida_pomel = StatusBarKind.create()
def gato_pared_demente_colosal():
    global demente_pared, statusbar
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile20
    """)):
        demente_pared = sprites.create(img("""
                ..f..........f..
                            .f1f........f1f.
                            .f1ffffffffff1f.
                            .f111111111111f.
                            .ff11111111f11f.
                            .f1f111111f111f.
                            .f1f11111ff111f.
                            .f1f111111f111f.
                            .f1f111111f111f.
                            .f1f1111111111f.
                            .f1ff11f111111f.
                            .f1f11f1f11111f.
                            .f11111f111111f.
                            .f1111f3f11111f.
                            .f11f1fffff111f.
                            .ff1fff11ff1fff.
                            .f11f1ffff1f1ff.
                            .fff111f1f1ff1f.
                            .f1f1fff1ffff1f.
                            .fff1ff1ff111ff.
                            .ffff11ffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .fffff....fffff.
                            ..fff......fff..
                            ...f........f...
            """),
            SpriteKind.enemy)
        tiles.place_on_tile(demente_pared, value)
        tiles.set_tile_at(value, assets.tile("""
            myTile22
        """))
        statusbar = statusbars.create(40, 4, StatusBarKind.enemy_health)
        statusbar.attach_to_sprite(demente_pared, 5, 0)
        statusbar.set_color(15, 1, 2)
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite, effects.fire, 500)
    statusbars.get_status_bar_attached_to(StatusBarKind.vida_pomel, otherSprite).value += -3
sprites.on_overlap(SpriteKind.projectile, SpriteKind.pomelo, on_on_overlap)

def on_overlap_tile(sprite2, location):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile19
    """),
    on_overlap_tile)

def on_on_overlap2(sprite3, otherSprite2):
    sprites.destroy(sprite3, effects.fire, 500)
    statusbars.get_status_bar_attached_to(StatusBarKind.vida_dem_sef, otherSprite2).value += -5
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Enemy_2, on_on_overlap2)

def on_overlap_tile2(sprite4, location2):
    pass
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile65
    """),
    on_overlap_tile2)

def pared_demente_secret():
    global demen_sec, statusbar2
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        myTile20
    """)):
        demen_sec = sprites.create(img("""
                ..f..........f..
                            .f1f........f1f.
                            .f1ffffffffff1f.
                            .f111111111111f.
                            .ff11111111f11f.
                            .f1f111111f111f.
                            .f1f11111ff111f.
                            .f1f111111f111f.
                            .f1f111111f111f.
                            .f1f1111111111f.
                            .f1ff11f111111f.
                            .f1f11f1f11111f.
                            .f11111f111111f.
                            .f1111f3f11111f.
                            .f11f1fffff111f.
                            .ff1fff11ff1fff.
                            .f11f1ffff1f1ff.
                            .fff111f1f1ff1f.
                            .f1f1fff1ffff1f.
                            .fff1ff1ff111ff.
                            .ffff11ffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .ffffffffffffff.
                            .fffff....fffff.
                            ..fff......fff..
                            ...f........f...
            """),
            SpriteKind.Enemy_2)
        tiles.place_on_tile(demen_sec, value3)
        tiles.set_tile_at(value3, assets.tile("""
            myTile22
        """))
        statusbar2 = statusbars.create(40, 4, StatusBarKind.vida_dem_sef)
        statusbar2.attach_to_sprite(demen_sec, 5, 0)
        statusbar2.set_color(15, 1, 2)
        statusbar2.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)

def on_overlap_tile3(sprite5, location3):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile63
    """),
    on_overlap_tile3)

def pez_espada():
    global pez2, statusbar
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        myTile30
    """)):
        pez2 = sprites.create(img("""
                ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ..................................................fffff.........
                            .................................................ff555f.........
                            ................................................ff5555f.........
                            ................................................f55555f.........
                            ................................................f55775f.........
                            ................................................f77777f.........
                            ................................................f87777f.........
                            ...............................................ff88888f.........
                            ...............................................f888888f.........
                            ...............................................f888888f.........
                            ...............................................f888888f.........
                            ..............................................ffffffffffff......
                            ...........................................fff88888888888fff....
                            .........................................fff888888888888888ff...
                            ........................................ff888888888888888888f...
                            ..................................ffffff888888888111111888888f..
                            ...............................fff8888888888888811ff111888888f..
                            ............................fff8888888888888888811ff111888888ff.
                            .........................ffff8888888888888888868111f1188888888f.
                            ....................fffff8888888888888888888886881118888688888f.
                            ................ffff88888888888822222888888888666666666668888ff.
                            .....fffffffffff98888888882882888882288228888888888888888888ff..
                            ......fff666999999988888888888888888222228888888888888888ffff...
                            .........f6666999999999988882222288882228888888888888fffff......
                            ..........fff666666699999888888888888fffffffffffffffff..........
                            .............fffff66999998888888fffff..........f88888f..........
                            ..................ffffffffffffff...............f88888f..........
                            ...............................................f88888f..........
                            ...............................................f88888f..........
                            ...............................................f88888f..........
                            ..............................................f88888ff..........
                            ..............................................f88888f...........
                            .............................................f88888ff...........
                            .............................................f88888f............
                            ............................................f88888ff............
                            ............................................f7888f..............
                            ...........................................f7788ff..............
                            ...........................................f777f................
                            ..........................................f577f.................
                            ..........................................f555f.................
                            .........................................f555f..................
                            .........................................f5ff...................
                            ........................................f5f.....................
                            ........................................ff......................
                            ........................................ff......................
                            .......................................ff.......................
                            .......................................f........................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
            """),
            SpriteKind.pez)
        tiles.place_on_tile(pez2, value4)
        tiles.set_tile_at(value4, assets.tile("""
            myTile29
        """))
        statusbar = statusbars.create(60, 4, StatusBarKind.vida_pez)
        statusbar.attach_to_sprite(pez2, 5, 0)
        statusbar.set_color(8, 5, 2)
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)

def chrome_basico():
    global chrome_intro, statusbar
    # Colocar chrome en posiciones específicas para el nivel introductorio
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile5
    """)):
        chrome_intro = sprites.create(img("""
                ......................................................................
                            ......................................................................
                            ......................................................................
                            ......................................................................
                            ...............fff....................................................
                            .............ffff5fffffffffff.........................................
                            ..........ffff77f555555555555fffffffffffffff..........................
                            .........ff5ff77f555555555555555555555555555fffff.....................
                            ........ff5555f7f55555555555555555555555555555555ffff.................
                            ........f55555f7fff5555555555555555555555555555555555fff..............
                            ........f55555f777ff555555555555555555555555555555555555ff............
                            .......f555555f77777ff555555555555555555555555555555555555ff..........
                            .......f555555f7777777f5555555555555555555555555555555555555ff........
                            ......f555555f77777777ff5555555555555555555555555555555555555ff.......
                            ......f555555f777777777f555555555555555555555555555555555555555ff.....
                            ......f555555ff77777777f55555555555555555555555ffffffffffffffffff....
        """),
        SpriteKind.chrome)
        tiles.place_on_tile(chrome_intro, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))
        statusbar = statusbars.create(60, 4, StatusBarKind.vida_chrome)
        statusbar.attach_to_sprite(chrome_intro, 5, 0)
        statusbar.set_color(5, 7, 8)
        statusbar.max = 10  # Vida reducida para el nivel introductorio
        statusbar.value = 10
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
def on_overlap_tile4(sprite6, location4):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile15
    """),
    on_overlap_tile4)

def bulling_a_pomelo_colosal():
    global bulling_a_pomelo, statusbar3
    for valor_80 in tiles.get_tiles_by_type(assets.tile("""
        myTile47
    """)):
        bulling_a_pomelo = sprites.create(img("""
                ......................................................................
                            ......................................................................
                            ......................................................................
                            .......11.............................................................
                            .......111............................................................
                            ........1111................................................1.11......
                            ........11111.............................................111111......
                            .........111111..........................................1111111......
                            .........11111111.......................................11111111......
                            .........11111111111...................................11111111.......
                            ..........1111111111.................................111111111........
                            ..........111111111111..............................11111111..........
                            ............111111111111...........................11111111...........
                            .............111111111111....fffffffffffff........11111111............
                            ..............111111111111fff4444444422222fff.....1111111.............
                            ..............1111111111ff4444444444222222222ff..1111111..............
                            ................1111111f44444444444222222224444f1111111...............
                            .................1111ff4444444444422222222444444ff11111...............
                            .................111f44444444444442222222244444444f11.................
                            .................11f4444444444442222222224444444444f..................
                            ..................f444444411114422222222444444444444f.................
                            .................f44444441111142222222224444444444111f................
                            .................f44444441111112222222224411ff4444111f................
                            ................f44444444111ff12222222244411ff44411111f...............
                            ...............f444444444411ff2222222224441111144411111f..............
                            ...............f4433334444422222222222244411111444111111..............
                            ..............f44433333344422222222222244441111444411111f.............
                            ..............f44433333334422222222222444444555444444444f.............
                            ..............f44433333334422222222222444444555544444444f.............
                            .............f4444333333334222222222224444445555444444444f............
                            .............f4444333333333222222222222444445555544444444f............
                            .............f4444433333333222225522222444445555555444444f............
                            .............f4444433333332222555555222444445555555444444f............
                            .............f4444433333332225555555222444444444444444444f............
                            .............f4444433333332225555555522224444444444444422f............
                            .............f4444433333332255555555522222224444444422222f............
                            .............f4444443333332225555555522222222222222222222f............
                            .............f4444443333332222225555522222222222222222222f............
                            .............f4444443333332222222222222222222222222222222f............
                            .............f4444443333332222222222222222222222222222222f............
                            .............f4444443333332222222222222222222222552222222f............
                            .............f4444443333332222fff222222222222222555552222f............
                            ..............f444444333333222f2ff2222222222222555555552f.............
                            ..............f444444333333222ff2fffffffffff225555555555f.............
                            ..............f4444443333333222ff22122212212ff5555555555f.............
                            ...............f4444443333332222ff222121221222ff5555555f..............
                            ...............f44444443333333222fffff222212221f5555555f..............
                            ................f44444443333333333222f222222221f555555f...............
                            .................f44444444333333322222ff1222122f55555f................
                            .................f444444444444422222222f122212ff55555f................
                            ..................f444444444444222222222ff22fff22555f.................
                            .................11f4444444444442222222222ff2222225f..................
                            ................1111f44444444444422222222222222222f...................
                            ..............1111111ff4444444444422222222222222ff111.................
                            .............1111111111f44444444442222222222222f11111.................
                            .............111111111..ff4444444444222222222ff1111111................
                            .............111111111....fff4444444222222fff1111111111...............
                            .............111111111.......fffffffffffff....1111111111..............
                            ............111111111.........................1111111111..............
                            ...........111111111...........................1111111111.............
                            ...........111111111.............................111111111............
                            ..........111111111...............................11111111............
                            .........111111...................................111111111...........
                            ........1111111....................................11111111...........
                            ........1111.........................................1111111..........
                            .......111............................................1111111.........
                            ........................................................11111.........
                            ..........................................................1111........
                            ............................................................11........
                            .............................................................11.......
            """),
            SpriteKind.pomelo)
        tiles.place_on_tile(bulling_a_pomelo, valor_80)
        tiles.set_tile_at(valor_80, assets.tile("""
            myTile48
        """))
        statusbar3 = statusbars.create(140, 4, StatusBarKind.vida_pomel)
        statusbar3.attach_to_sprite(bulling_a_pomelo, 5, 0)
        statusbar3.set_color(4, 5, 6)
        statusbar3.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)

def on_on_zero(status):
    global currentlevel
    sprites.destroy(statusbar.sprite_attached_to(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
statusbars.on_zero(StatusBarKind.vida_pez, on_on_zero)

def chromeeeeeeeeee():
    global chrome2, statusbar
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile35
    """)):
        chrome2 = sprites.create(img("""
                ......................................................................
                            ......................................................................
                            ......................................................................
                            ......................................................................
                            ...............fff....................................................
                            .............ffff5fffffffffff.........................................
                            ..........ffff77f555555555555fffffffffffffff..........................
                            .........ff5ff77f555555555555555555555555555fffff.....................
                            ........ff5555f7f55555555555555555555555555555555ffff.................
                            ........f55555f7fff5555555555555555555555555555555555fff..............
                            ........f55555f777ff555555555555555555555555555555555555ff............
                            .......f555555f77777ff555555555555555555555555555555555555ff..........
                            .......f555555f7777777f5555555555555555555555555555555555555ff........
                            ......f555555f77777777ff5555555555555555555555555555555555555ff.......
                            ......f555555f777777777f555555555555555555555555555555555555555ff.....
                            ......f555555ff77777777f55555555555555555555555555555555ffffffffff....
                            ......f55555555f7777777f5555555555555555555555555555555f77777777fff...
                            .....f555555555f7777777f5555555555555555555555555555555f7777777777f...
                            .....f5555555555f77777ff555555555555555555555555555555f77777777777f...
                            .....f55555555555f7777f5555555555555555555555555555555f7777777777ff...
                            .....f55555555555f77777f555555555555555555555555555555f7777777777ff...
                            .....f555555555555f77777f55555555555555555555555555555f777777777f5f...
                            .....f555555555555f777777f5555555555555555555555555555f777777777f5f...
                            .....f5555555555555f777777f555555555555555555555555555f77777777f55f...
                            .....f5555555555555f777777ff55555555555555555555555555f7777777f555f...
                            .....f5555555555555f7777777f55fffffffff55555555555555f77777777f555f...
                            ....f55555555555555ff777777fff222222222ff55555555555ff7777777f5555f...
                            ....f555555555555555f777777f2222222222222f55ffffffff777777777f5555f...
                            ....f5555555555555555f7777f222222222222222f5f777777777777777f55555f...
                            ....f55555555555555555f77f22222222222222222ff77777777777777f555555f...
                            ....f55555555555555555fff22222222222222222f2f7777777777777f5555555f...
                            ....f555555555555555555ff222222222222f222ffff7fffff777777f5555555f....
                            ....f555555555555555555f22222f2222222f222f9f2f55555fffffff5555555f....
                            ....f5555fff55555555555f22222f222222f2222f9f2f5555555555555555555f....
                            ....f555ff77ffffff555fff222222f22222f2222fff2f5555555555555555555f....
                            ....f555f777777777ffffff22222ff2222ff22222222f5555555555555555555f....
                            ....f5ff777777777fffffff222fffff22fff22222222f5555555555555555555f....
                            ....fff777777ffff555555f22ffffff22fff22222222f555555555555555555f.....
                            ....ff7777777f555555555f2222222222fff2222f222f555555555555555555f.....
                            .....f7777777f555555555f222222222222f222fff22f555555555555555555f.....
                            .....ff777777f555555555f2222222222222222f9f22f555555555555555555f.....
                            ......f77777ff5555555555f222222222222222f9f2f5555555555555555555f.....
                            ......f777fff55555555555f222222fffff2222fff2f5555555555555555555f.....
                            .......fff555555555555555f2222ff2222f222222fff55555555555555555f......
                            .......f555555555555555555f222222222ff2222f77f55555555555555555f......
                            .......f5555555555555555555f2222222222222fff77f5555555555555555f......
                            .......f55555555555555555555ff222222222ff55f777f555555555555555f......
                            .......f5555555555555555555555fffffffff5555f7777f55555555555555f......
                            .......ff555555555555555555fff7ff5555555555f7777f55555555555555f......
                            ........f5555555555555555ff7777f555555555555f7777f5555555555555f......
                            ........f55555555555555ff7777777ff5555555555ff777f5555555555555f......
                            .........f55555555555ff77777777777f5555555555ff77f555555555555f.......
                            .........f5555555555ff777777777777f55555555555f77f555555555555f.......
                            ..........f555555555f7777777777777f555555555555f77f55555555555f.......
                            ..........f555555555f7777777777777f555555555555ff7f55555555555f.......
                            ..........ff55555555f7777777777777f5555555555555f77ff555555555f.......
                            ...........f5555555f77777777777777f5555555555555ff777ff555555f........
                            ...........ff555555f77777777777777f55555555555555f77777f55555f........
                            ............ff55555f7777777777777f555555555555555ff77777f5555f........
                            .............f5555f7777777777777f55555555555555555ff77777ff55f........
                            .............ff55ff77777777777ff5555555555555555555f777777f5ff........
                            ..............ffff777777777fff5555555555555555555555f777777ff.........
                            ..............ffffffff777ff5555555555555555555555555ff77777f..........
                            ..............f.......fff.ffffffff5555555555555555555ff7777f..........
                            ..................................fffffffffffffff55555f7777f..........
                            .................................................fffffff777f..........
                            ......................................................ff777f..........
                            .......................................................ff77f..........
                            .........................................................f7f..........
                            .........................................................fff..........
            """),
            SpriteKind.chrome)
        tiles.place_on_tile(chrome2, value2)
        tiles.set_tile_at(value2, assets.tile("""
            myTile36
        """))
        statusbar = statusbars.create(80, 4, StatusBarKind.vida_chrome)
        statusbar.attach_to_sprite(chrome2, 5, 0)
        statusbar.set_color(5, 7, 8)
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
def easter_egg(número: number):
    if número == 1:
        tiles.set_current_tilemap(tilemap("""
            nivel4
        """))
    elif False:
        pass
    tiles.place_on_random_tile(mySprite, assets.tile("""
        transparency16
    """))

def on_overlap_tile5(sprite7, location5):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile42
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite8, location6):
    global currentlevel
    currentlevel += 1
    nivel_actual_(currentlevel)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile6)

def on_on_zero2(status2):
    global currentlevel
    sprites.destroy(statusbar.sprite_attached_to(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
statusbars.on_zero(StatusBarKind.vida_chrome, on_on_zero2)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 5 2 2 4 . . . . . . . . 
                    . . . . 2 2 5 2 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 2 2 2 2 2 . . . . . 
                    . . . . 2 2 2 4 4 4 2 2 2 . . . 
                    . . 2 2 4 4 4 4 5 5 5 4 4 4 . . 
                    . . . 2 4 4 5 5 5 1 1 5 5 4 4 . 
                    . . . . 2 4 4 5 5 1 1 1 5 5 4 . 
                    . . . . 2 2 4 4 5 5 5 5 5 5 4 . 
                    . . . . . 2 2 4 4 4 5 4 4 2 2 . 
                    . . . . . . 2 2 2 4 4 4 2 2 . . 
                    . . 2 2 . . . . 2 2 2 2 2 . . . 
                    . 2 4 4 . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        50,
        50)
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            1,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    game.game_over(False)
info.on_countdown_end(on_countdown_end)

def on_on_zero3(status3):
    global currentlevel
    sprites.destroy(statusbar.sprite_attached_to(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero3)

def on_overlap_tile7(sprite9, location7):
    global CURRENT_LEVEL_SECRET
    CURRENT_LEVEL_SECRET += 1
    secreto_1(CURRENT_LEVEL_SECRET)
scene.on_overlap_tile(SpriteKind.player,
    sprites.swamp.swamp_tile13,
    on_overlap_tile7)

def on_on_overlap3(sprite10, otherSprite3):
    sprites.destroy(sprite10, effects.fire, 500)
    statusbars.get_status_bar_attached_to(StatusBarKind.vida_pez, otherSprite3).value += -3
sprites.on_overlap(SpriteKind.projectile, SpriteKind.pez, on_on_overlap3)

def on_overlap_tile8(sprite11, location8):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile21
    """),
    on_overlap_tile8)

def on_overlap_tile9(sprite12, location9):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile16
    """),
    on_overlap_tile9)

def on_overlap_tile10(sprite13, location10):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile40
    """),
    on_overlap_tile10)

def on_overlap_tile11(sprite14, location11):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile44
    """),
    on_overlap_tile11)

def on_overlap_tile12(sprite15, location12):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile43
    """),
    on_overlap_tile12)

def secreto_1(intelilli_JAVA: number):
    if intelilli_JAVA == 1:
        tiles.set_current_tilemap(tilemap("""
            level16
        """))
        pared_demente_secret()
        game.splash("demencia")
        info.start_countdown(120)
    elif intelilli_JAVA == 2:
        tiles.set_current_tilemap(tilemap("""
            level17
        """))
        game.splash("cieguitud 4")
    elif intelilli_JAVA == 3:
        tiles.set_current_tilemap(tilemap("""
            level18
        """))
        game.splash("pense que gane")
    elif intelilli_JAVA == 3:
        tiles.set_current_tilemap(tilemap("""
            level19
        """))
        game.splash("primate")
    elif intelilli_JAVA == 4:
        tiles.set_current_tilemap(tilemap("""
            level20
        """))
        game.splash("¡La edad de oro!")
    elif intelilli_JAVA == 5:
        tiles.set_current_tilemap(tilemap("""
            level21
        """))
        game.splash("Traje de prcionero")
    elif intelilli_JAVA == 6:
        tiles.set_current_tilemap(tilemap("""
            level22
        """))
        game.splash("pato mecanico")
    elif intelilli_JAVA == 7:
        tiles.set_current_tilemap(tilemap("""
            level23
        """))
        pez_espada()
        game.splash("¡A la pesca!")
    elif intelilli_JAVA == 8:
        tiles.set_current_tilemap(tilemap("""
            level24
        """))
        game.splash("caracolessss")
    elif intelilli_JAVA == 9:
        tiles.set_current_tilemap(tilemap("""
            level26
        """))
        game.splash("cables de colores")
    elif intelilli_JAVA == 10:
        tiles.set_current_tilemap(tilemap("""
            level27
        """))
        game.splash("¡Abajo!")
    elif intelilli_JAVA == 11:
        tiles.set_current_tilemap(tilemap("""
            level28
        """))
        game.splash("\"¿Cuantos arcoriris hay?\"")
    elif intelilli_JAVA == 12:
        tiles.set_current_tilemap(tilemap("""
            level29
        """))
        game.splash("copa de vino")
    elif intelilli_JAVA == 13:
        tiles.set_current_tilemap(tilemap("""
            level30
        """))
        game.splash("bosque de la muerte")
    elif intelilli_JAVA == 14:
        tiles.set_current_tilemap(tilemap("""
            level31
        """))
        game.splash("computadores")
    tiles.place_on_random_tile(mySprite, assets.tile("""
        transparency16
    """))
def pez_sef():
    global pez_ssef, statusbar
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        myTile30
    """)):
        pez_ssef = sprites.create(img("""
                ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ..................................................fffff.........
                            .................................................ff555f.........
                            ................................................ff5555f.........
                            ................................................f55555f.........
                            ................................................f55775f.........
                            ................................................f77777f.........
                            ................................................f87777f.........
                            ...............................................ff88888f.........
                            ...............................................f888888f.........
                            ...............................................f888888f.........
                            ...............................................f888888f.........
                            ..............................................ffffffffffff......
                            ...........................................fff88888888888fff....
                            .........................................fff888888888888888ff...
                            ........................................ff888888888888888888f...
                            ..................................ffffff888888888111111888888f..
                            ...............................fff8888888888888811ff111888888f..
                            ............................fff8888888888888888811ff111888888ff.
                            .........................ffff8888888888888888868111f1188888888f.
                            ....................fffff8888888888888888888886881118888688888f.
                            ................ffff88888888888822222888888888666666666668888ff.
                            .....fffffffffff98888888882882888882288228888888888888888888ff..
                            ......fff666999999988888888888888888222228888888888888888ffff...
                            .........f6666999999999988882222288882228888888888888fffff......
                            ..........fff666666699999888888888888fffffffffffffffff..........
                            .............fffff66999998888888fffff..........f88888f..........
                            ..................ffffffffffffff...............f88888f..........
                            ...............................................f88888f..........
                            ...............................................f88888f..........
                            ...............................................f88888f..........
                            ..............................................f88888ff..........
                            ..............................................f88888f...........
                            .............................................f88888ff...........
                            .............................................f88888f............
                            ............................................f88888ff............
                            ............................................f7888f..............
                            ...........................................f7788ff..............
                            ...........................................f777f................
                            ..........................................f577f.................
                            ..........................................f555f.................
                            .........................................f555f..................
                            .........................................f5ff...................
                            ........................................f5f.....................
                            ........................................ff......................
                            ........................................ff......................
                            .......................................ff.......................
                            .......................................f........................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
                            ................................................................
            """),
            SpriteKind.pez_dsef)
        tiles.place_on_tile(mySprite, value5)
        tiles.set_tile_at(value5, assets.tile("""
            myTile29
        """))
        statusbar = statusbars.create(60, 4, StatusBarKind.pez_par)
        statusbar.attach_to_sprite(pez_ssef, 5, 0)
        statusbar.set_color(15, 1, 2)
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)

def on_overlap_tile13(sprite16, location13):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        silla matadora
    """),
    on_overlap_tile13)

def on_overlap_tile14(sprite17, location14):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile14)

def nivel_actual_(_123ETS_XD: number):
    if _123ETS_XD == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        game.splash("nivel 1")
    elif _123ETS_XD == 2:
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
        game.splash("patito,patito")
    elif _123ETS_XD == 3:
        tiles.set_current_tilemap(tilemap("""
            level6
        """))
        game.splash("de locos")
    elif _123ETS_XD == 4:
        tiles.set_current_tilemap(tilemap("""
            level10
        """))
        game.splash("confia en nada")
    elif _123ETS_XD == 5:
        tiles.set_current_tilemap(tilemap("""
            nivel1
        """))
        game.splash("X")
    elif _123ETS_XD == 6:
        tiles.set_current_tilemap(tilemap("""
            level15
        """))
        game.splash("paredes")
    elif _123ETS_XD == 7:
        tiles.set_current_tilemap(tilemap("""
            level16
        """))
        gato_pared_demente_colosal()
        game.splash("demencia")
    elif _123ETS_XD == 8:
        tiles.set_current_tilemap(tilemap("""
            level17
        """))
        game.splash("cieguitud 4")
    elif _123ETS_XD == 9:
        tiles.set_current_tilemap(tilemap("""
            level18
        """))
        game.splash("pense que gane")
    elif _123ETS_XD == 10:
        tiles.set_current_tilemap(tilemap("""
            level19
        """))
        game.splash("primate")
    elif _123ETS_XD == 11:
        tiles.set_current_tilemap(tilemap("""
            level20
        """))
        game.splash("¡La edad de oro!")
    elif _123ETS_XD == 12:
        tiles.set_current_tilemap(tilemap("""
            level21
        """))
        game.splash("Traje de pricionero")
    elif _123ETS_XD == 13:
        tiles.set_current_tilemap(tilemap("""
            level22
        """))
        game.splash("pato mecanico")
    elif _123ETS_XD == 14:
        tiles.set_current_tilemap(tilemap("""
            level23
        """))
        pez_espada()
        game.splash("¡A la pesca!")
    elif _123ETS_XD == 15:
        tiles.set_current_tilemap(tilemap("""
            level24
        """))
        game.splash("caracolessss")
    elif _123ETS_XD == 16:
        tiles.set_current_tilemap(tilemap("""
            level26
        """))
        game.splash("cables de colores")
    elif _123ETS_XD == 17:
        tiles.set_current_tilemap(tilemap("""
            level27
        """))
        game.splash("¡Abajo!")
    elif _123ETS_XD == 18:
        tiles.set_current_tilemap(tilemap("""
            level28
        """))
        game.splash("\"¿Cuantos arcoriris hay?\"")
    elif _123ETS_XD == 19:
        tiles.set_current_tilemap(tilemap("""
            level29
        """))
        game.splash("copa de vino")
    elif _123ETS_XD == 20:
        tiles.set_current_tilemap(tilemap("""
            level30
        """))
        game.splash("bosque de la muerte")
    elif _123ETS_XD == 21:
        tiles.set_current_tilemap(tilemap("""
            level31
        """))
        game.splash("computadores")
        chromeeeeeeeeee()
    elif _123ETS_XD == 22:
        tiles.set_current_tilemap(tilemap("""
            level60
        """))
        game.splash("cigarrillo cayendo al agua")
    elif _123ETS_XD == 23:
        tiles.set_current_tilemap(tilemap("""
            level63
        """))
        game.splash("\"El gran pincho\"")
    elif _123ETS_XD == 24:
        tiles.set_current_tilemap(tilemap("""
            level64
        """))
        game.splash("2,3,4 y algo raro")
    elif _123ETS_XD == 25:
        tiles.set_current_tilemap(tilemap("""
            level65
        """))
        game.splash("titeres e isleños")
    elif _123ETS_XD == 26:
        tiles.set_current_tilemap(tilemap("""
            level66
        """))
        game.splash("caracol pinchudo")
    elif _123ETS_XD == 27:
        tiles.set_current_tilemap(tilemap("""
            level67
        """))
        game.splash("desfile de paredes")
    elif _123ETS_XD == 28:
        tiles.set_current_tilemap(tilemap("""
            nivel2
        """))
        game.splash("mate con pomelo")
        bulling_a_pomelo_colosal()
    elif _123ETS_XD == 29:
        tiles.set_current_tilemap(tilemap("""
            nivel3
        """))
        game.splash("laberinto de muros")
    elif _123ETS_XD == 30:
        tiles.set_current_tilemap(tilemap("""
            nivel5
        """))
        game.splash("barco")
    elif _123ETS_XD == 31:
        tiles.set_current_tilemap(tilemap("""
            nivel7
        """))
        game.splash("cinquito")
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile4
    """))

def on_overlap_tile15(sprite18, location15):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile62
    """),
    on_overlap_tile15)

def on_on_zero4(status4):
    global CURRENT_LEVEL_SECRET
    sprites.destroy(statusbar.sprite_attached_to(), effects.rings, 500)
    CURRENT_LEVEL_SECRET += 1
    secreto_1(CURRENT_LEVEL_SECRET)
statusbars.on_zero(StatusBarKind.pez_par, on_on_zero4)

def on_overlap_tile16(sprite19, location16):
    pass
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile64
    """),
    on_overlap_tile16)

def on_on_zero5(status5):
    global currentlevel
    sprites.destroy(statusbar3.sprite_attached_to(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
statusbars.on_zero(StatusBarKind.vida_pomel, on_on_zero5)

def on_on_overlap4(sprite20, otherSprite4):
    sprites.destroy(sprite20, effects.fire, 500)
    statusbars.get_status_bar_attached_to(StatusBarKind.vida_chrome, otherSprite4).value += -3
sprites.on_overlap(SpriteKind.projectile, SpriteKind.chrome, on_on_overlap4)

def on_on_overlap5(sprite21, otherSprite5):
    sprites.destroy(sprite21, effects.fire, 500)
    statusbars.get_status_bar_attached_to(StatusBarKind.pez_par, mySprite).value += -5
sprites.on_overlap(SpriteKind.projectile, SpriteKind.pez_dsef, on_on_overlap5)

def on_on_zero6(status6):
    global CURRENT_LEVEL_SECRET
    sprites.destroy(statusbar2.sprite_attached_to(), effects.rings, 500)
    CURRENT_LEVEL_SECRET += 1
    secreto_1(CURRENT_LEVEL_SECRET)
statusbars.on_zero(StatusBarKind.vida_dem_sef, on_on_zero6)

def on_on_overlap6(sprite22, otherSprite6):
    sprites.destroy(sprite22, effects.fire, 500)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite6).value += -5
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap6)

pez_ssef: Sprite = None
CURRENT_LEVEL_SECRET = 0
projectile: Sprite = None
chrome2: Sprite = None
statusbar3: StatusBarSprite = None
bulling_a_pomelo: Sprite = None
pez2: Sprite = None
statusbar2: StatusBarSprite = None
demen_sec: Sprite = None
statusbar: StatusBarSprite = None
demente_pared: Sprite = None
currentlevel = 0
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . 2 2 . . . . . . 
            . . . . . . . 2 2 2 2 . . . . . 
            . . . . . . 2 2 . . 2 . . . . . 
            . . . . . . 2 . . . 2 . . . . . 
            . . . . 2 2 . . . . 2 . . . . . 
            . . . . 2 . . f . . 2 . f . . . 
            . . . . . . . . . . 2 . . . . . 
            . . . . . . . . . . 2 . . . . . 
            . . . . . . . f f . 2 . . f f . 
            . . . . . . . . . f 2 f f . . . 
            . . . . . . . 2 . . 2 . . 2 2 . 
            . . . . . 2 2 . 2 2 2 2 2 2 . 2 
            . . . . 2 . . . . . . . . . . 2 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 70, 98)
scene.set_background_image(img("""
    3111111111111111111111111111111111111111111111111111111111111111111111132222222222222222222222222222222222222222222222222222222222222222222222222399999999999999
        8311111111111111111111111111111111111111111111111111111111111111111111322222222222222222222222222222222222222222222222222222222222222222222222222399999999999999
        8833111111111111111111111111111111111111111111111111111111111111111113222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999
        8888311111111111111111111111111111111111111111111111111111111111111132222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999
        8888833111111111111111111111111111111111111111111111111111111111111322222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999
        8888888311111111111111111111111111111111111111111111111111111111133222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999
        8888888833111111111111111111111111111111111111111111111111111111322222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999
        8888888888311111111111111111111111111111111111111111111111111133222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999
        8888888888833111111111111111111111111111111111111111111111111322222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999
        8888888888888311111111111111111111111111111111111111111111113222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999
        8888888888888833111111111111111111111111111111111111111111332222222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999
        8888888888888888311111111111111111111111111111111111111113222222222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999
        8888888888888888833111111111111111111111111111111111111132222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999
        8888888888888888888311111111111111111111111111111111111322222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999
        8888888888888888888833111111111111111111111111111111133222222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999
        8888888888888888888888311111111111111111111111111111322222222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999
        8888888888888888888888833111111111111111111111111113222222222222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999
        8888888888888888888888888311111111111111111111111332222222222222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999
        8888888888888888888888888833111111111111111111113222222222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999
        8888888888888888888888888888311111111111111111132222222222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999
        8888888888888888888888888888833111111111111111322222222222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999999
        8888888888888888888888888888888311111111111133222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999999
        8888888888888888888888888888888833111111111322222222222222222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999999
        8888888888888888888888888888888888311111113222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999999
        8888888888888888888888888888888888833111332222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999999
        8888888888888888888888888888888888888313222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999999999
        8888888888888888888888888888888888888833222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999999999
        8888888888888888888888888888888888888355322222222222222222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999999999
        8888888888888888888888888888888888833555533222222222222222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999999999
        8888888888888888888888888888888888355555555322222222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999999999
        8888888888888888888888888888888883555555555533222222222222222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999999999
        8888888888888888888888888888888335555555555555322222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999999999999
        8888888888888888888888888888883555555555555555533222222222222222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999999999999
        8888888888888888888888888888835555555555555555555322222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999999999999
        8888888888888888888888888888355555555555555555555533222222222222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999999999999
        8888888888888888888888888833555555555555555555555555322222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999999999999
        8888888888888888888888888355555555555555555555555555533222222222222222222222222222222222222222222222222222222222222222222222222399999999999999999999999999999999
        8888888888888888888888883555555555555555555555555555555322222222222222222222222222222222222222222222222222222222222222222222223999999999999999999999999999999999
        8888888888888888888888335555555555555555555555555555555533222222222222222222222222222222222222222222222222222222222222222222239999999999999999999999999999999999
        8888888888888888888883555555555555555555555555555555555555322222222222222222222222222222222222222222222222222222222222222222239999999999999999999999999999999999
        8888888888888888888835555555555555555555555555555555555555533222222222222222222222222222222222222222222222222222222222222222399999999999999999999999999999999999
        8888888888888888888355555555555555555555555555555555555555555322222222222222222222222222222222222222222222222222222222222222399999999999999999999999999999999999
        8888888888888888833555555555555555555555555555555555555555555533222222222222222222222222222222222222222222222222222222222223999999999999999999999999999999999999
        8888888888888888355555555555555555555555555555555555555555555555322222222222222222222222222222222222222222222222222222222223999999999999999999999999999999999999
        8888888888888883555555555555555555555555555555555555555555555555533222222222222222222222222222222222222222222222222222222239999999999999999999999999999999999999
        8888888888888335555555555555555555555555555555555555555555555555555322222222222222222222222222222222222222222222222222222239999999999999999999999999999999999999
        8888888888883555555555555555555555555555555555555555555555555555555533222222222222222222222222222222222222222222222222222399999999999999999999999999999999999999
        8888888888835555555555555555555555555555555555555555555555555555555555322222222222222222222222222222222222222222222222222399999999999999999999999999999999999999
        8888888888355555555555555555555555555555555555555555555555555555555555533222222222222222222222222222222222222222222222223999999999999999999999999999999999999999
        8888888833555555555555555555555555555555555555555555555555555555555555555322222222222222222222222222222222222222222222223999999999999999999999999999999999999999
        8888888355555555555555555555555555555555555555555555555555555555555555355533222222222222222222222222222222222222222222239999999999999999999999999999999999999999
        8888883555555555555555555555555555555555555555555555555555555555555533355555322222222222222222222222222222222222222222239999999999999999999999999999999999999999
        8888335555555555555555555555555555555555555555555555555555555555553377735555533222222222222222222222222222222222222222399999999999999999999999999999999999999999
        8883555555555555555555555555555555555555555555555555555555555555337777773555555322222222222222222222222222222222222223999999999999999999999999999999999999999999
        8835555555555555555555555555555555555555555555555555555555555533777777773555555533222222222222222222222222222222222223999999999999999999999999999999999999999999
        8355555555555555555555555555555555555555555555555555555555553377777777777355555555322222222222222222222222222222222239999999999999999999999999999999999999999999
        3555555555555555555555555555555555555555555555555555555555337777777777777735555555533222222222222222222222222222222239999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555555533777777777777777773555555555322222222222222222222222222222399999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555553377777777777777777777355555555533322222222222222222222222222399999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555337777777777777777777777355555555555322222222222222222222222223999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555533777777777777777777777777735555555555533222222222222222222222223999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555553377777777777777777777777777773555555555555322222222222222222222239999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555337777777777777777777777777777777355555555555533222222222222222222239999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555553777777777777777777777777777777777735555555555555322222222222222222399999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555533337777777777777777777777777777777735555555555555533222222222222222399999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555553333377777777777777777777777777773555555555555555322222222222223999999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555533333777777777777777777777777355555555555555533222222222223999999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555555555333337777777777777777777735555555555555555322222222239999999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555553333337777777777777773555555555555555533222222399999999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555553333377777777773555555555555555555322222399999999999999999999999999999999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555533333777777355555555555555555533223999999999999999999999999999999999999999999999999999
        5555ff5555555555555555555555555555555555555555555555555555555555555555555555555333337735555555555555555555323999999999999999999999999999999999999999999999999999
        55555ff555555555555555555555555555555555555555555555555555555555555555555555555555553333555555555555555555533999999999999999999999999999999999999999999999999999
        55555f4ff5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555536399999999999999999999999999999999999999999999999999
        55555f44ffffff55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555366633999999999999999999999999999999999999999999999999
        555555f4444444ffffffff555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666399999999999999999999999999999999999999999999999
        555555f44444444444444f555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666633999999999999999999999999999999999999999999999
        555555f44444444444444f555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666399999999999999999999999999999999999999999999
        555555f44444444444444f555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666633999999999999999999999999999999999999999999
        555555f44444444444444f555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666399999999999999999999999999999999999999999
        555555f4444ff44444444f555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666633999999999999999999999999999999999999999
        555555fffffff44444444f555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666399999999999999999999999999999999999999
        555555555555f44444444f555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666633999999999999999999999999999999999999
        555555555555ff44444444f55555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666399999999999999999999999999999999999
        5555555555555f44444444f55555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666633999999999999999999999999999999999
        5555555555555f444444444f5555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666399999999999999999999999999999999
        5555555555555f444444444f5555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666633999999999999999999999999999999
        5555555555555f444444444f5555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666399999999999999999999999999999
        5555555555555f4444444444f555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666633999999999999999999999999999
        5555555555555f4444444444f555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666399999999999999999999999999
        5555555555555ff444444444f555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666639999999999999999999999999
        55555555555555fffffffffff555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666639999999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666663999999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666399999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666639999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666663999999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666399999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666399999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666639999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666663999999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666666666399999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666666666639999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666666666663999999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666666666666399999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666666666666399999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666666666666639999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666666666666666663999999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666666666666666666399999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666666666666666666639999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666666666666666666663999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666666666666666666663999999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666666666666666666666399999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666666666666666666666666639999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666666666666666666666666663999999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666666666666666666666666666399999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666666666666666666666666666639999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555553666666666666666666666666666666666666666666666666666666666666666666666639999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666666666666666666666666666666663999
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555536666666666666666666666666666666666666666666666666666666666666666666666666399
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555366666666666666666666666666666666666666666666666666666666666666666666666666639
"""))
scene.camera_follow_sprite(mySprite)
currentlevel = 1
nivel_actual_(1)

def on_forever():
    music.play(music.create_song(hex("""
            0078000408060a00001c00010a006400f401640000040000000000000000000000000005000004100000000400051b1e22252a0c001000011b01001c000f05001202c102c20100040500280000006400280003140006020004b50000000400011d10001400011d1400180001241c002000021b1e28002c000220272c003000012530003400011d3400380001203c004000031b202448004c0001254c005000012054005800012258005c00011d5c006000011b64006800021d2468006c0001206c00700001207000740001207400780001208400880001228c009000012c90009400011d94009800012298009c00011ba000a4000120ac00b0000125b000b400021e22b800bc000124bc00c00002252902001c000c960064006d019001000478002c010000640032000000000a0600053f000c0010000125100014000129a000a4000119a400a800011ba800ac00011eac00b0000120b000b40003242527b400b80002292cb800bc00012cbc00c000012c03001c0001dc00690000045e010004000000000000000000000564000104000311007c0080000c191b1d1e2022242527292a2c04001c00100500640000041e000004000000000000000000000000000a040004160038003c00032022273c00400002222a4000440002202205001c000f0a006400f4010a0000040000000000000000000000000000000002240008000c00011b10001400012218001c00011e20002400012728002c00011e38003c00011d06001c00010a006400f401640000040000000000000000000000000000000002300014001800011e1c002000011920002400012928002c0001192c00300001293000340001204c005000012954005800012407001c00020a006400f401640000040000000000000000000000000000000003060020002400012508001c000e050046006603320000040a002d000000640014000132000201000212001c002000012920002400012028002c00012909010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8004c0014001500010a1c001d0001052400250002040634003500040002090a380039000301090a3c003d0001024400450003010508480049000200024c004d00010450005100020306580059000107
        """)),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)

