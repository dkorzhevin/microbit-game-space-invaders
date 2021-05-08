input.onButtonPressed(Button.A, function () {
    SHIP.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    SHOOT = game.createSprite(SHIP.get(LedSpriteProperty.X), SHIP.get(LedSpriteProperty.Y))
    SHOOT.change(LedSpriteProperty.Brightness, 88)
    for (let index = 0; index < 4; index++) {
        SHOOT.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if (SHOOT.isTouching(ENEMY)) {
            game.addScore(1)
            SHOOT.delete()
            ENEMY.delete()
        }
    }
    if (SHOOT.get(LedSpriteProperty.Y) <= 0) {
        SHOOT.delete()
    }
})
input.onButtonPressed(Button.B, function () {
    SHIP.move(1)
})
let ENEMY: game.LedSprite = null
let SHOOT: game.LedSprite = null
let SHIP: game.LedSprite = null
SHIP = game.createSprite(2, 4)
game.setScore(0)
basic.forever(function () {
    ENEMY = game.createSprite(randint(0, 4), 0)
    ENEMY.set(LedSpriteProperty.Brightness, 150)
    basic.pause(100)
    ENEMY.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        ENEMY.move(1)
        basic.pause(500)
        if (ENEMY.isTouching(SHIP)) {
            game.gameOver()
        }
    }
    if (ENEMY.isTouchingEdge()) {
        ENEMY.delete()
    }
})
