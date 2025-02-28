"""
Este archivo contiene el nuevo código para el nivel 1 del juego ¿queee?.....
Incluye la definición del nivel, enemigos y mensajes.
"""

# Nivel 1 modificado - Añadir esto a la función nivel_actual_ en el archivo main.py
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
