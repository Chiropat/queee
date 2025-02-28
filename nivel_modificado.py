"""
Script para modificar el archivo main.py del juego ¿queee?.....
Este script contiene todas las modificaciones necesarias para crear un nivel introductorio balanceado.
"""

# Modificaciones necesarias para el archivo main.py

# 1. Agregar el enemigo Chrome básico para el nivel introductorio
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

# 2. Modificar la función nivel_actual_ para incluir nuestras mejoras al nivel 1
def nivel_actual_(_123ETS_XD: number):
    if _123ETS_XD == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        # Añadir enemigos básicos para el nivel introductorio
        pez_espada()  # Añadir peces básicos
        chrome_basico()  # Añadir enemigos Chrome
        
        # Mensaje de bienvenida para el primer nivel
        game.splash("¡Bienvenido a ¿queee?.....")
        game.show_long_text("Usa las flechas para moverte y A para disparar", DialogLayout.BOTTOM)
        info.start_countdown(180)  # Dar 3 minutos para completar el nivel introductorio
    elif _123ETS_XD == 2:
        # Resto del código original
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
        game.splash("patito,patito")
