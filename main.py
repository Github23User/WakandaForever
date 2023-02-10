def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    Namor.set_position(148, 2)
sprites.on_overlap(SpriteKind.guard, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    Namor.set_position(148, 2)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_on_score():
    Namor.destroy()
    scene.set_background_image(assets.image("""
        boston-bridge
    """))
    effects.confetti.start_screen_effect()
    Riri.say_text("Wakanda Forever!", 2000, False)
info.on_score(20, on_on_score)

Riri: Sprite = None
Namor: Sprite = None
scene.set_background_image(assets.image("""
    wakanda
"""))
Shuri = sprites.create(assets.image("""
    shuri
"""), SpriteKind.player)
controller.move_sprite(Shuri)
game.show_long_text("When game begins, press the ARROW KEYS to move Shuri, Okoye and Riri. If Namor catches you, you will lose points! ",
    DialogLayout.FULL)
Shuri.set_stay_in_screen(True)
Namor = sprites.create(assets.image("""
    namor
"""), SpriteKind.enemy)
Namor.set_position(148, 2)
Namor.follow(Shuri, 30)
Riri = sprites.create(assets.image("""
    riri
"""), SpriteKind.guard)
Okeye = sprites.create(assets.image("""
    okoye
"""), SpriteKind.guard)
controller.move_sprite(Riri, 34, -53)
controller.move_sprite(Okeye, 68, -58)