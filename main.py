import spritePro as s

class GameScene(s.Scene):
    def __init__(self):
        super().__init__()
        self.bg = s.Sprite("images (1).jfif", pos=(200, 300), size=(400, 600), scene=self)
        self.player = s.Sprite("flappy-bird-original.webp", pos=(100, 300), size=(50, 50), scene=self)
        self.player_body = s.add_physics(self.player, s.PhysicsConfig(bounce=0.8))
        s.physics.set_gravity(980)
        s.physics.set_bounds(s.pygame.Rect(0, 0, 400, 600))

if __name__ == '__main__':
    s.run(scene=GameScene, size=(400, 600), title="Flappy Bird")
