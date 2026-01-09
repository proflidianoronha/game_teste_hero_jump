# -*- coding: utf-8 -*-
# Run with: pgzrun game.py
import random

WIDTH = 800
HEIGHT = 450
TITLE = "Hero Jump"

GRAVITY = 0.6
JUMP_FORCE = -12
GROUND_Y = 330

game_state = "menu"
sound_enabled = True

MAX_LIVES = 3
lives = MAX_LIVES


class AnimatedActor:
    def __init__(self, idle_frames, move_frames, pos):
        self.idle_frames = idle_frames
        self.move_frames = move_frames
        self.actor = Actor(idle_frames[0], pos)

        self.frames = idle_frames
        self.frame = 0
        self.timer = 0
        self.moving = False

    def set_animation(self, frames):
        if self.frames != frames:
            self.frames = frames
            self.frame = 0
            self.timer = 0
            self.actor.image = frames[0]

    def update_animation(self):
        self.timer += 1
        if self.timer >= 8:
            self.timer = 0
            self.frame = (self.frame + 1) % len(self.frames)
            self.actor.image = self.frames[self.frame]


class Hero(AnimatedActor):
    def __init__(self):
        super().__init__(
            ["hero_idle_0", "hero_idle_0"],
            ["hero_run_0", "hero_run_1"],
            (100, 300)
        )

        self.run_right = ["hero_run_0", "hero_run_1"]
        self.run_left = ["hero_run_2", "hero_run_3"]

        self.idle_right = ["hero_idle_0", "hero_idle_0"]
        self.idle_left = ["hero_idle_1", "hero_idle_1"]

        self.direction = "right"
        self.vy = 0
        self.on_ground = False

    def update(self):
        self.moving = False

        if keyboard.left:
            self.actor.x -= 4
            self.direction = "left"
            self.moving = True
            self.set_animation(self.run_left)

        elif keyboard.right:
            self.actor.x += 4
            self.direction = "right"
            self.moving = True
            self.set_animation(self.run_right)

        else:
            if self.direction == "left":
                self.set_animation(self.idle_left)
            else:
                self.set_animation(self.idle_right)

        if keyboard.space and self.on_ground:
            self.vy = JUMP_FORCE
            self.on_ground = False
            if sound_enabled:
                sounds.jump.set_volume(0.2)
                sounds.jump.play()

        self.vy += GRAVITY
        self.actor.y += self.vy
        self.on_ground = False

        if self.actor.y >= GROUND_Y:
            self.actor.y = GROUND_Y
            self.vy = 0
            self.on_ground = True

        elif self.vy >= 0 and self.actor.colliderect(platform):
            self.actor.bottom = platform.top
            self.vy = 0
            self.on_ground = True

        self.update_animation()


class Enemy(AnimatedActor):
    def __init__(self, x, left_limit, right_limit):
        super().__init__(
            ["enemy_idle_0", "enemy_idle_0"],
            ["enemy_run_0", "enemy_run_1"],
            (x, GROUND_Y)
        )

        self.run_right = ["enemy_run_0", "enemy_run_1"]
        self.run_left = ["enemy_run_2", "enemy_run_3"]

        self.left_limit = left_limit
        self.right_limit = right_limit

        self.speed = random.choice([-2, 2])
        self.direction = "right" if self.speed > 0 else "left"

        # animação inicial
        if self.direction == "right":
            self.set_animation(self.run_right)
        else:
            self.set_animation(self.run_left)

    def update(self):
        self.actor.x += self.speed

        # muda direção ao bater no limite
        if self.actor.x < self.left_limit:
            self.speed = abs(self.speed)
            self.direction = "right"
            self.set_animation(self.run_right)

        elif self.actor.x > self.right_limit:
            self.speed = -abs(self.speed)
            self.direction = "left"
            self.set_animation(self.run_left)

        self.update_animation()


hero = Hero()

enemies = [
    Enemy(400, 350, 550),
    Enemy(650, 600, 750)
]

platform = Actor("platform", (400, 280))
goal = Actor("goal", (655, 282))
heart_icon = Actor("heart")

btn_start = Actor("button_start", (400, 180))
btn_sound = Actor("button_sound_off", (400, 240))
btn_exit = Actor("button_exit", (400, 320))
btn_restart = Actor("button_restart", (400, 320))

background = Actor("background", center=(WIDTH // 2, HEIGHT // 2))


def play_music():
    if sound_enabled:
        music.play("musica_aventura.wav")
        music.set_volume(0.1)
    else:
        music.stop()


def reset_game():
    global lives
    hero.actor.pos = (100, 300)
    hero.vy = 0
    hero.on_ground = False
    lives = MAX_LIVES


def draw():
    screen.clear()
    background.draw()

    if game_state == "menu":
        btn_start.draw()
        btn_sound.draw()
        btn_exit.draw()

    elif game_state == "game":
        platform.draw()
        goal.draw()
        hero.actor.draw()

        for enemy in enemies:
            enemy.actor.draw()

        for i in range(lives):
            heart_icon.pos = (30 + i * 35, 30)
            heart_icon.draw()

    elif game_state == "gameover":
        screen.draw.text("GAME OVER", center=(400, 180),
                         fontsize=70, color="red")
        btn_restart.draw()

    elif game_state == "win":
        screen.draw.text("VOCE GANHOU!", center=(400, 170),
                         fontsize=60, color="green")
        screen.draw.text("Parabens!", center=(400, 220), fontsize=30)
        btn_restart.draw()


def update():
    global lives, game_state

    if game_state == "game":
        hero.update()

        for enemy in enemies:
            enemy.update()
            if hero.actor.colliderect(enemy.actor):
                lives -= 1
                hero.actor.pos = (100, 300)
                hero.vy = 0

                if sound_enabled:
                    sounds.hit.play()
                    sounds.hit.set_volume(0.3)

                if lives <= 0:
                    game_state = "gameover"
                    sounds.gameover.play()
                    sounds.gameover.set_volume(0.3)

        if hero.actor.colliderect(goal):
            game_state = "win"
            sounds.win.play()
            sounds.win.set_volume(0.3)


def on_mouse_down(pos):
    global game_state, sound_enabled

    if game_state == "menu":
        if btn_start.collidepoint(pos):
            reset_game()
            game_state = "game"
            

        elif btn_sound.collidepoint(pos):
            sound_enabled = not sound_enabled
            btn_sound.image = (
                "button_sound_on" if sound_enabled else "button_sound_off"
            )
            play_music()

        elif btn_exit.collidepoint(pos):
            exit()

    elif game_state in ("gameover", "win"):
        if btn_restart.collidepoint(pos):
            game_state = "menu"