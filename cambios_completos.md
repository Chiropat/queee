# Cambios completos para implementar el nuevo nivel

## 1. Actualización de main.ts

Abrir el archivo `main.ts` y añadir la siguiente función después de la función `pez_espada()`:

```typescript
function chrome_basico() {
    for (let value2 of tiles.getTilesByType(assets.tile`myTile5`)) {
        chrome_intro = sprites.create(img`
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
        `, SpriteKind.chrome)
        tiles.placeOnTile(chrome_intro, value2)
        tiles.setTileAt(value2, assets.tile`transparency16`)
        statusbar = statusbars.create(60, 4, StatusBarKind.vida_chrome)
        statusbar.attachToSprite(chrome_intro, 5, 0)
        statusbar.setColor(5, 7, 8)
        statusbar.max = 10
        statusbar.value = 10
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
```

## 2. Actualizar la función nivel_actual_ en main.ts

Buscar la función `nivel_actual_` y modificar la parte del nivel 1 para que quede así:

```typescript
function nivel_actual_(_123ETS_XD: number) {
    if (_123ETS_XD == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        pez_espada()
        chrome_basico()
        game.splash("¡Bienvenido a ¿queee?.....")
        game.showLongText("Usa las flechas para moverte y A para disparar", DialogLayout.Bottom)
        info.startCountdown(180)
    } else if (_123ETS_XD == 2) {
        // El resto queda igual...
```

## 3. Actualización de main.py

Añadir la siguiente función después de la función `pez_espada()`:

```python
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
```

## 4. Actualizar la función nivel_actual_ en main.py

Buscar la función `nivel_actual_` y modificar la parte del nivel 1 para que quede así:

```python
def nivel_actual_(_123ETS_XD: number):
    if _123ETS_XD == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        pez_espada()
        chrome_basico()
        game.splash("¡Bienvenido a ¿queee?.....")
        game.show_long_text("Usa las flechas para moverte y A para disparar", 
                       DialogLayout.BOTTOM)
        info.start_countdown(180)
    elif _123ETS_XD == 2:
        # El resto queda igual...
```

## 5. Actualización del tilemap level1

Dentro de tilemap.g.ts, buscar la definición del nivel 1 y modificarla para incluir posiciones estratégicas para los enemigos Chrome básicos. Buscar:

```typescript
case "level1":
case "level1":return tiles.createTilemap(hex`...
```

Y modificar los valores para que incluyan tiles de tipo 5 en ubicaciones estratégicas para los enemigos Chrome básicos.

---

## Instrucciones para sincronizar los cambios:

1. Sube estos cambios a tu repositorio de GitHub
2. Abre el proyecto en MakeCode Arcade usando la URL de GitHub
3. MakeCode Arcade automáticamente sincronizará los archivos de código con la representación en bloques
4. Si hay algún problema con la sincronización, puedes usar la vista JavaScript y copiar/pegar los cambios directamente

## Características del nuevo nivel:

- **Instrucciones claras**: Mensajes de bienvenida y explicaciones para jugadores nuevos
- **Tiempo más generoso**: 3 minutos para completar el nivel
- **Enemigos adaptados**: Chrome básicos con menos vida (10 en lugar del valor predeterminado)
- **Diseño accesible**: Plataformas y enemigos ubicados estratégicamente para una curva de dificultad adecuada
