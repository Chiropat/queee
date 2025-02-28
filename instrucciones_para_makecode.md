# Instrucciones para implementar el nuevo nivel en MakeCode Arcade

Para que nuestras modificaciones funcionen correctamente en la plataforma web de MakeCode Arcade, necesitas hacer los siguientes cambios una vez que hayas abierto el proyecto:

## Paso 1: Añadir la función chrome_basico()

1. En la plataforma web de MakeCode Arcade, cambia a la vista JavaScript (botón de "JavaScript" en la parte superior).
2. Copia y pega esta función en el código (busca un lugar adecuado, por ejemplo, después de otras funciones de enemigos):

```typescript
function chrome_basico () {
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
        statusbar.max = 10  // Vida reducida para el nivel introductorio
        statusbar.value = 10
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
```

## Paso 2: Modificar la función nivel_actual_

1. Busca la función `nivel_actual_` en el código.
2. Modifica la parte del nivel 1 para que quede así:

```typescript
function nivel_actual_ (_123ETS_XD: number) {
    if (_123ETS_XD == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        pez_espada()  // Añadir peces básicos
        chrome_basico()  // Añadir enemigos Chrome
        
        // Mensajes de bienvenida 
        game.splash("¡Bienvenido a ¿queee?.....")
        game.showLongText("Usa las flechas para moverte y A para disparar", DialogLayout.Bottom)
        info.startCountdown(180)  // 3 minutos para el nivel
    } else if (_123ETS_XD == 2) {
        // El resto de la función queda igual
```

## Paso 3: Modificar el tilemap del Nivel 1

1. Haz clic en la pestaña "Tilemaps" (icono de cuadrícula) en la barra lateral.
2. Selecciona el tilemap "level1".
3. Edita el tilemap para incluir:
   - Plataformas más accesibles para un nivel introductorio
   - Coloca algunos tiles `myTile5` en lugares estratégicos para los enemigos Chrome básicos
   - Asegúrate de tener también los tiles para los enemigos pez

## Paso 4: Guardar y Probar

1. Haz clic en el botón "Guardar" para guardar todos los cambios.
2. Prueba el juego para asegurarte de que el nivel 1 funciona como se espera:
   - Debería mostrar los mensajes de bienvenida
   - Debería tener un temporizador de 3 minutos
   - Deberías ver enemigos Chrome con menor vida
   - La dificultad debería ser adecuada para un nivel introductorio

## Características principales del nuevo nivel:

- **Mensaje de bienvenida**: Añade contexto e instrucciones para el jugador
- **Temporizador más generoso**: 3 minutos en lugar del temporizador predeterminado
- **Enemigos con menos vida**: Chrome básicos con 10 de vida en lugar del valor predeterminado
- **Diseño de nivel más accesible**: Plataformas y enemigos colocados estratégicamente

Estos cambios harán que el nivel 1 sea más acogedor para los jugadores nuevos mientras mantiene la esencia y el tono del juego.

¡Disfruta probando el nuevo nivel!
