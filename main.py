def on_button_pressed_a():
    SHIP.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global SHOOT
    SHOOT = game.create_sprite(SHIP.get(LedSpriteProperty.X), SHIP.get(LedSpriteProperty.Y))
    SHOOT.change(LedSpriteProperty.BRIGHTNESS, 88)
    for index in range(4):
        SHOOT.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if SHOOT.is_touching(ENEMY):
            game.add_score(1)
            SHOOT.delete()
            ENEMY.delete()
    if SHOOT.get(LedSpriteProperty.Y) <= 0:
        SHOOT.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    SHIP.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

ENEMY: game.LedSprite = None
SHOOT: game.LedSprite = None
SHIP: game.LedSprite = None
SHIP = game.create_sprite(2, 4)
game.set_score(0)

def on_forever():
    global ENEMY
    ENEMY = game.create_sprite(randint(0, 4), 0)
    ENEMY.set(LedSpriteProperty.BRIGHTNESS, 150)
    basic.pause(100)
    ENEMY.turn(Direction.RIGHT, 90)
    for index2 in range(4):
        ENEMY.move(1)
        basic.pause(500)
        if ENEMY.is_touching(SHIP):
            game.game_over()
    if ENEMY.is_touching_edge():
        ENEMY.delete()
basic.forever(on_forever)
