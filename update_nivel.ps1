# Script PowerShell para implementar los cambios del nuevo nivel

# 1. Actualización de main.ts - Añadir la función chrome_basico()
$mainTsContent = Get-Content -Path "main.ts" -Raw
$functionDefinition = @"
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
        statusbar.max = 10
        statusbar.value = 10
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
"@

# Buscar la posición adecuada para insertar la función
$pezEspadaPattern = "function pez_espada \(\)"
$pezEspadaMatch = [regex]::Match($mainTsContent, $pezEspadaPattern)
if ($pezEspadaMatch.Success) {
    # Encontrar el final de la función pez_espada
    $pezEspadaFunctionEndPos = $mainTsContent.IndexOf("}", $pezEspadaMatch.Index)
    # Insertar la nueva función después del cierre de pez_espada
    $updatedMainTs = $mainTsContent.Substring(0, $pezEspadaFunctionEndPos + 1) + "`n" + $functionDefinition + $mainTsContent.Substring($pezEspadaFunctionEndPos + 1)
    Set-Content -Path "main.ts" -Value $updatedMainTs
    Write-Host "Función chrome_basico() añadida a main.ts"
}

# 2. Actualizar la función nivel_actual_ en main.ts
$nivelActualPattern = "function nivel_actual_ \(_123ETS_XD: number\)"
$nivelActualMatch = [regex]::Match($mainTsContent, $nivelActualPattern)
if ($nivelActualMatch.Success) {
    $nivel1Pattern = "if \(_123ETS_XD == 1\) \{[^}]*\}"
    $nivel1Match = [regex]::Match($mainTsContent, $nivel1Pattern)
    if ($nivel1Match.Success) {
        $newNivel1Code = @"
if (_123ETS_XD == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        pez_espada()
        chrome_basico()
        game.splash("¡Bienvenido a ¿queee?.....")
        game.showLongText("Usa las flechas para moverte y A para disparar", DialogLayout.Bottom)
        info.startCountdown(180)
    }
"@
        $updatedMainTs = $mainTsContent.Replace($nivel1Match.Value, $newNivel1Code)
        Set-Content -Path "main.ts" -Value $updatedMainTs
        Write-Host "Función nivel_actual_ modificada en main.ts"
    }
}

# 3. Actualización de main.py - Añadir la función chrome_basico()
$mainPyContent = Get-Content -Path "main.py" -Raw
$pythonFunctionDefinition = @"
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
"@

# Buscar la posición adecuada para insertar la función en Python
$pezEspadaPyPattern = "def pez_espada\(\)"
$pezEspadaMatchPy = [regex]::Match($mainPyContent, $pezEspadaPyPattern)
if ($pezEspadaMatchPy.Success) {
    # Encontrar el final de la función pez_espada en Python
    $pezEspadaPyEndPos = $mainPyContent.IndexOf("def ", $pezEspadaMatchPy.Index + 1)
    if ($pezEspadaPyEndPos -eq -1) {
        $pezEspadaPyEndPos = $mainPyContent.Length
    }
    # Insertar la nueva función después de pez_espada
    $updatedMainPy = $mainPyContent.Substring(0, $pezEspadaPyEndPos) + $pythonFunctionDefinition + "`n" + $mainPyContent.Substring($pezEspadaPyEndPos)
    Set-Content -Path "main.py" -Value $updatedMainPy
    Write-Host "Función chrome_basico() añadida a main.py"
}

# 4. Actualizar la función nivel_actual_ en main.py
$nivelActualPyPattern = "def nivel_actual_\(_123ETS_XD: number\)"
$nivelActualPyMatch = [regex]::Match($mainPyContent, $nivelActualPyPattern)
if ($nivelActualPyMatch.Success) {
    $nivel1PyPattern = "if _123ETS_XD == 1:[^e]*elif"
    $nivel1PyMatch = [regex]::Match($mainPyContent, $nivel1PyPattern)
    if ($nivel1PyMatch.Success) {
        $newNivel1PyCode = @"
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
    elif
"@
        $updatedMainPy = $mainPyContent.Replace($nivel1PyMatch.Value, $newNivel1PyCode)
        Set-Content -Path "main.py" -Value $updatedMainPy
        Write-Host "Función nivel_actual_ modificada en main.py"
    }
}

# 5. Actualización del tilemap level1
$tilemapContent = Get-Content -Path "tilemap.g.ts" -Raw
$level1Pattern = 'case "level1":.*?return tiles\.createTilemap\(hex`[^`]*`'
$level1Match = [regex]::Match($tilemapContent, $level1Pattern)
if ($level1Match.Success) {
    $newTilemapDef = 'case "level1":
            return tiles.createTilemap(hex`1000100000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000030300030300030300030300000005000102040102040102040102040404040000000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000303000000000000000000000000050000000500000000000000000000000000000000030000000000000000050000000000000300000000000000000000000000000000030000000000000000000000`'
    $updatedTilemap = $tilemapContent.Replace($level1Match.Value, $newTilemapDef)
    Set-Content -Path "tilemap.g.ts" -Value $updatedTilemap
    Write-Host "Tilemap level1 modificado en tilemap.g.ts"
}

Write-Host "¡Cambios aplicados con éxito! Ahora puedes subir estos cambios a tu repositorio de GitHub."
