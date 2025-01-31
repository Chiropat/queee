namespace SpriteKind {
    export const pez = SpriteKind.create()
    export const chrome = SpriteKind.create()
    export const Enemy_2 = SpriteKind.create()
    export const pez_dsef = SpriteKind.create()
    export const pomelo = SpriteKind.create()
}
namespace StatusBarKind {
    export const vida_pez = StatusBarKind.create()
    export const vida_chrome = StatusBarKind.create()
    export const vida_dem_sef = StatusBarKind.create()
    export const pez_par = StatusBarKind.create()
    export const vida_pomel = StatusBarKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile21`, function (sprite11, location8) {
    game.gameOver(false)
})
function gato_pared_demente_colosal () {
    for (let value of tiles.getTilesByType(assets.tile`myTile20`)) {
        demente_pared = sprites.create(img`
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
            `, SpriteKind.Enemy)
        tiles.placeOnTile(demente_pared, value)
        tiles.setTileAt(value, assets.tile`myTile22`)
        statusbar = statusbars.create(40, 4, StatusBarKind.EnemyHealth)
        statusbar.attachToSprite(demente_pared, 5, 0)
        statusbar.setColor(15, 1, 2)
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.pomelo, function (sprite, otherSprite) {
    sprites.destroy(sprite, effects.fire, 500)
    statusbars.getStatusBarAttachedTo(StatusBarKind.vida_pomel, otherSprite).value += -3
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile62`, function (sprite18, location15) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite17, location14) {
    game.gameOver(false)
})
function pared_demente_secret () {
    for (let value3 of tiles.getTilesByType(assets.tile`myTile20`)) {
        demen_sec = sprites.create(img`
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
            `, SpriteKind.Enemy_2)
        tiles.placeOnTile(demen_sec, value3)
        tiles.setTileAt(value3, assets.tile`myTile22`)
        statusbar2 = statusbars.create(40, 4, StatusBarKind.vida_dem_sef)
        statusbar2.attachToSprite(demen_sec, 5, 0)
        statusbar2.setColor(15, 1, 2)
        statusbar2.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
function pez_espada () {
    for (let value4 of tiles.getTilesByType(assets.tile`myTile30`)) {
        pez2 = sprites.create(img`
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
            `, SpriteKind.pez)
        tiles.placeOnTile(pez2, value4)
        tiles.setTileAt(value4, assets.tile`myTile29`)
        statusbar = statusbars.create(60, 4, StatusBarKind.vida_pez)
        statusbar.attachToSprite(pez2, 5, 0)
        statusbar.setColor(8, 5, 2)
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile40`, function (sprite13, location10) {
    game.gameOver(false)
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status3) {
    sprites.destroy(statusbar.spriteAttachedTo(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
})
statusbars.onZero(StatusBarKind.vida_pez, function (status) {
    sprites.destroy(statusbar.spriteAttachedTo(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
})
function chromeeeeeeeeee () {
    for (let value2 of tiles.getTilesByType(assets.tile`myTile35`)) {
        chrome2 = sprites.create(img`
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
            `, SpriteKind.chrome)
        tiles.placeOnTile(chrome2, value2)
        tiles.setTileAt(value2, assets.tile`myTile36`)
        statusbar = statusbars.create(80, 4, StatusBarKind.vida_chrome)
        statusbar.attachToSprite(chrome2, 5, 0)
        statusbar.setColor(5, 7, 8)
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
function easter_egg (número: number) {
    if (número == 1) {
        tiles.setCurrentTilemap(tilemap`nivel4`)
    } else if (false) {
    	
    }
    tiles.placeOnRandomTile(mySprite, assets.tile`transparency16`)
}
function bulling_a_pomelo_colosal () {
    for (let valor_80 of tiles.getTilesByType(assets.tile`myTile47`)) {
        bulling_a_pomelo = sprites.create(img`
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
            `, SpriteKind.pomelo)
        tiles.placeOnTile(bulling_a_pomelo, valor_80)
        tiles.setTileAt(valor_80, assets.tile`myTile48`)
        statusbar3 = statusbars.create(140, 4, StatusBarKind.vida_pomel)
        statusbar3.attachToSprite(bulling_a_pomelo, 5, 0)
        statusbar3.setColor(4, 5, 6)
        statusbar3.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.chrome, function (sprite20, otherSprite4) {
    sprites.destroy(sprite20, effects.fire, 500)
    statusbars.getStatusBarAttachedTo(StatusBarKind.vida_chrome, otherSprite4).value += -3
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 50, 50)
    music.play(music.createSoundEffect(WaveShape.Sine, 5000, 1, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
info.onCountdownEnd(function () {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile42`, function (sprite7, location5) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile44`, function (sprite14, location11) {
    game.gameOver(false)
})
statusbars.onZero(StatusBarKind.vida_chrome, function (status2) {
    sprites.destroy(statusbar.spriteAttachedTo(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
})
statusbars.onZero(StatusBarKind.pez_par, function (status4) {
    sprites.destroy(statusbar.spriteAttachedTo(), effects.rings, 500)
    CURRENT_LEVEL_SECRET += 1
    secreto_1(CURRENT_LEVEL_SECRET)
})
function secreto_1 (intelilli_JAVA: number) {
    if (intelilli_JAVA == 1) {
        tiles.setCurrentTilemap(tilemap`level16`)
        pared_demente_secret()
        game.splash("demencia")
        info.startCountdown(120)
    } else if (intelilli_JAVA == 2) {
        tiles.setCurrentTilemap(tilemap`level17`)
        game.splash("cieguitud 4")
    } else if (intelilli_JAVA == 3) {
        tiles.setCurrentTilemap(tilemap`level18`)
        game.splash("pense que gane")
    } else if (intelilli_JAVA == 3) {
        tiles.setCurrentTilemap(tilemap`level19`)
        game.splash("primate")
    } else if (intelilli_JAVA == 4) {
        tiles.setCurrentTilemap(tilemap`level20`)
        game.splash("¡La edad de oro!")
    } else if (intelilli_JAVA == 5) {
        tiles.setCurrentTilemap(tilemap`level21`)
        game.splash("Traje de prcionero")
    } else if (intelilli_JAVA == 6) {
        tiles.setCurrentTilemap(tilemap`level22`)
        game.splash("pato mecanico")
    } else if (intelilli_JAVA == 7) {
        tiles.setCurrentTilemap(tilemap`level23`)
        pez_espada()
        game.splash("¡A la pesca!")
    } else if (intelilli_JAVA == 8) {
        tiles.setCurrentTilemap(tilemap`level24`)
        game.splash("caracolessss")
    } else if (intelilli_JAVA == 9) {
        tiles.setCurrentTilemap(tilemap`level26`)
        game.splash("cables de colores")
    } else if (intelilli_JAVA == 10) {
        tiles.setCurrentTilemap(tilemap`level27`)
        game.splash("¡Abajo!")
    } else if (intelilli_JAVA == 11) {
        tiles.setCurrentTilemap(tilemap`level28`)
        game.splash("\"¿Cuantos arcoriris hay?\"")
    } else if (intelilli_JAVA == 12) {
        tiles.setCurrentTilemap(tilemap`level29`)
        game.splash("copa de vino")
    } else if (intelilli_JAVA == 13) {
        tiles.setCurrentTilemap(tilemap`level30`)
        game.splash("bosque de la muerte")
    } else if (intelilli_JAVA == 14) {
        tiles.setCurrentTilemap(tilemap`level31`)
        game.splash("computadores")
    }
    tiles.placeOnRandomTile(mySprite, assets.tile`transparency16`)
}
statusbars.onZero(StatusBarKind.vida_pomel, function (status5) {
    sprites.destroy(statusbar3.spriteAttachedTo(), effects.rings, 500)
    currentlevel += 1
    nivel_actual_(currentlevel)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`silla matadora`, function (sprite16, location13) {
    game.gameOver(false)
})
function pez_sef () {
    for (let value5 of tiles.getTilesByType(assets.tile`myTile30`)) {
        pez_ssef = sprites.create(img`
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
            `, SpriteKind.pez_dsef)
        tiles.placeOnTile(mySprite, value5)
        tiles.setTileAt(value5, assets.tile`myTile29`)
        statusbar = statusbars.create(60, 4, StatusBarKind.pez_par)
        statusbar.attachToSprite(pez_ssef, 5, 0)
        statusbar.setColor(15, 1, 2)
        statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile15`, function (sprite6, location4) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile64`, function (sprite19, location16) {
	
})
function nivel_actual_ (_123ETS_XD: number) {
    if (_123ETS_XD == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
        game.splash("nivel 1")
    } else if (_123ETS_XD == 2) {
        tiles.setCurrentTilemap(tilemap`level5`)
        game.splash("patito,patito")
    } else if (_123ETS_XD == 3) {
        tiles.setCurrentTilemap(tilemap`level6`)
        game.splash("de locos")
    } else if (_123ETS_XD == 4) {
        tiles.setCurrentTilemap(tilemap`level10`)
        game.splash("confia en nada")
    } else if (_123ETS_XD == 5) {
        tiles.setCurrentTilemap(tilemap`nivel1`)
        game.splash("X")
    } else if (_123ETS_XD == 6) {
        tiles.setCurrentTilemap(tilemap`level15`)
        game.splash("paredes")
    } else if (_123ETS_XD == 7) {
        tiles.setCurrentTilemap(tilemap`level16`)
        gato_pared_demente_colosal()
        game.splash("demencia")
    } else if (_123ETS_XD == 8) {
        tiles.setCurrentTilemap(tilemap`level17`)
        game.splash("cieguitud 4")
    } else if (_123ETS_XD == 9) {
        tiles.setCurrentTilemap(tilemap`level18`)
        game.splash("pense que gane")
    } else if (_123ETS_XD == 10) {
        tiles.setCurrentTilemap(tilemap`level19`)
        game.splash("primate")
    } else if (_123ETS_XD == 11) {
        tiles.setCurrentTilemap(tilemap`level20`)
        game.splash("¡La edad de oro!")
    } else if (_123ETS_XD == 12) {
        tiles.setCurrentTilemap(tilemap`level21`)
        game.splash("Traje de pricionero")
    } else if (_123ETS_XD == 13) {
        tiles.setCurrentTilemap(tilemap`level22`)
        game.splash("pato mecanico")
    } else if (_123ETS_XD == 14) {
        tiles.setCurrentTilemap(tilemap`level23`)
        pez_espada()
        game.splash("¡A la pesca!")
    } else if (_123ETS_XD == 15) {
        tiles.setCurrentTilemap(tilemap`level24`)
        game.splash("caracolessss")
    } else if (_123ETS_XD == 16) {
        tiles.setCurrentTilemap(tilemap`level26`)
        game.splash("cables de colores")
    } else if (_123ETS_XD == 17) {
        tiles.setCurrentTilemap(tilemap`level27`)
        game.splash("¡Abajo!")
    } else if (_123ETS_XD == 18) {
        tiles.setCurrentTilemap(tilemap`level28`)
        game.splash("\"¿Cuantos arcoriris hay?\"")
    } else if (_123ETS_XD == 19) {
        tiles.setCurrentTilemap(tilemap`level29`)
        game.splash("copa de vino")
    } else if (_123ETS_XD == 20) {
        tiles.setCurrentTilemap(tilemap`level30`)
        game.splash("bosque de la muerte")
    } else if (_123ETS_XD == 21) {
        tiles.setCurrentTilemap(tilemap`level31`)
        game.splash("computadores")
        chromeeeeeeeeee()
    } else if (_123ETS_XD == 22) {
        tiles.setCurrentTilemap(tilemap`level60`)
        game.splash("cigarrillo cayendo al agua")
    } else if (_123ETS_XD == 23) {
        tiles.setCurrentTilemap(tilemap`level63`)
        game.splash("\"El gran pincho\"")
    } else if (_123ETS_XD == 24) {
        tiles.setCurrentTilemap(tilemap`level64`)
        game.splash("2,3,4 y algo raro")
    } else if (_123ETS_XD == 25) {
        tiles.setCurrentTilemap(tilemap`level65`)
        game.splash("titeres e isleños")
    } else if (_123ETS_XD == 26) {
        tiles.setCurrentTilemap(tilemap`level66`)
        game.splash("caracol pinchudo")
    } else if (_123ETS_XD == 27) {
        tiles.setCurrentTilemap(tilemap`level67`)
        game.splash("desfile de paredes")
    } else if (_123ETS_XD == 28) {
        tiles.setCurrentTilemap(tilemap`nivel2`)
        game.splash("mate con pomelo")
        bulling_a_pomelo_colosal()
    } else if (_123ETS_XD == 29) {
        tiles.setCurrentTilemap(tilemap`nivel3`)
        game.splash("laberinto de muros")
    } else if (_123ETS_XD == 30) {
        tiles.setCurrentTilemap(tilemap`nivel5`)
        game.splash("barco")
    } else if (_123ETS_XD == 31) {
        tiles.setCurrentTilemap(tilemap`nivel7`)
        game.splash("cinquito")
    }
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile4`)
}
scene.onOverlapTile(SpriteKind.Player, sprites.swamp.swampTile13, function (sprite9, location7) {
    CURRENT_LEVEL_SECRET += 1
    secreto_1(CURRENT_LEVEL_SECRET)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy_2, function (sprite3, otherSprite2) {
    sprites.destroy(sprite3, effects.fire, 500)
    statusbars.getStatusBarAttachedTo(StatusBarKind.vida_dem_sef, otherSprite2).value += -5
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile43`, function (sprite15, location12) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile19`, function (sprite2, location) {
    game.gameOver(true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile65`, function (sprite4, location2) {
	
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.pez, function (sprite10, otherSprite3) {
    sprites.destroy(sprite10, effects.fire, 500)
    statusbars.getStatusBarAttachedTo(StatusBarKind.vida_pez, otherSprite3).value += -3
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile16`, function (sprite12, location9) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile3`, function (sprite8, location6) {
    currentlevel += 1
    nivel_actual_(currentlevel)
})
statusbars.onZero(StatusBarKind.vida_dem_sef, function (status6) {
    sprites.destroy(statusbar2.spriteAttachedTo(), effects.rings, 500)
    CURRENT_LEVEL_SECRET += 1
    secreto_1(CURRENT_LEVEL_SECRET)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite22, otherSprite6) {
    sprites.destroy(sprite22, effects.fire, 500)
    statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite6).value += -5
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.pez_dsef, function (sprite21, otherSprite5) {
    sprites.destroy(sprite21, effects.fire, 500)
    statusbars.getStatusBarAttachedTo(StatusBarKind.pez_par, mySprite).value += -5
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile63`, function (sprite5, location3) {
    game.gameOver(false)
})
let pez_ssef: Sprite = null
let CURRENT_LEVEL_SECRET = 0
let projectile: Sprite = null
let statusbar3: StatusBarSprite = null
let bulling_a_pomelo: Sprite = null
let chrome2: Sprite = null
let pez2: Sprite = null
let statusbar2: StatusBarSprite = null
let demen_sec: Sprite = null
let statusbar: StatusBarSprite = null
let demente_pared: Sprite = null
let currentlevel = 0
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 70, 98)
scene.setBackgroundImage(img`
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
    `)
scene.cameraFollowSprite(mySprite)
currentlevel = 1
nivel_actual_(1)
forever(function () {
    music.play(music.createSong(hex`00780004080200`), music.PlaybackMode.UntilDone)
})
