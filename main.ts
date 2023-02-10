sprites.onOverlap(SpriteKind.Guard, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    Namor.setPosition(148, 2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    info.changeLifeBy(-1)
    Namor.setPosition(148, 2)
})
info.onScore(20, function () {
    Namor.destroy()
    scene.setBackgroundImage(assets.image`boston-bridge`)
    effects.confetti.startScreenEffect()
    Riri.sayText("Wakanda Forever!", 2000, false)
})
let Riri: Sprite = null
let Namor: Sprite = null
scene.setBackgroundImage(assets.image`wakanda`)
let Shuri = sprites.create(assets.image`shuri`, SpriteKind.Player)
controller.moveSprite(Shuri)
game.showLongText("When game begins, press the ARROW KEYS to move Shuri, Okoye and Riri. If Namor catches you, you will lose points! ", DialogLayout.Full)
Shuri.setStayInScreen(true)
Namor = sprites.create(assets.image`namor`, SpriteKind.Enemy)
Namor.setPosition(148, 2)
Namor.follow(Shuri, 30)
Riri = sprites.create(assets.image`riri`, SpriteKind.Guard)
let Okeye = sprites.create(assets.image`okoye`, SpriteKind.Guard)
controller.moveSprite(Riri, 34, -53)
controller.moveSprite(Okeye, 68, -58)
