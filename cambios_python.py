# Nuevas Funciones para ¿queee?.... - Nivel 1 Introductorio

def chrome_basico():
    """
    Crea enemigos Chrome más simples para el nivel introductorio.
    Tienen menos vida (10 en lugar del valor predeterminado) y se colocan 
    en posiciones estratégicas marcadas con myTile5 en el tilemap.
    """
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

def nivel_actual_(_123ETS_XD):
    """
    Gestiona la configuración de cada nivel
    Modificado para incluir un nivel 1 más acogedor para jugadores nuevos
    """
    if _123ETS_XD == 1:
        tiles.set_current_tilemap(tilemap("""level1"""))
        pez_espada()  # Añadir peces básicos
        chrome_basico()  # Añadir enemigos Chrome simplificados
        
        # Mensajes de bienvenida para el nivel introductorio
        game.splash("¡Bienvenido a ¿queee?.....")
        game.show_long_text("Usa las flechas para moverte y A para disparar", 
                         DialogLayout.BOTTOM)
        info.start_countdown(180)  # 3 minutos para el nivel inicial
    elif _123ETS_XD == 2:
        tiles.set_current_tilemap(tilemap("""level5"""))
        game.splash("patito,patito")
    elif _123ETS_XD == 3:
        tiles.set_current_tilemap(tilemap("""level6"""))
        game.splash("de locos")
    elif _123ETS_XD == 4:
        tiles.set_current_tilemap(tilemap("""level10"""))
        game.splash("confia en nada")
    elif _123ETS_XD == 5:
        tiles.set_current_tilemap(tilemap("""nivel1"""))
        game.splash("X")
    elif _123ETS_XD == 6:
        tiles.set_current_tilemap(tilemap("""level15"""))
        game.splash("paredes")
    elif _123ETS_XD == 7:
        tiles.set_current_tilemap(tilemap("""level16"""))
        gato_pared_demente_colosal()
        game.splash("demencia")
