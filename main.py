def on_button_pressed_a():
    if sprite.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
    else:
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    led.unplot(2, 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
sprite = game.create_sprite(2, 2)

def on_forever():
    sprite.move(1)
    basic.pause(100)
    sprite.if_on_edge_bounce()
basic.forever(on_forever)
