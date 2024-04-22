"""
Slide and Catch Game Pt I
Evan Carpenter
"""



import pygame, random, simpleGE

class EasterEgg(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("EasterEgg.png")
        self.setSize(50, 50)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class EasterBunny(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("EasterBunny.png")
        self.setSize(100, 100)
        self.position = (320, 400)
        self.moveSpeed = 7
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("FieldOfGrass.png")
        
        self.EasterBunny = EasterBunny(self)
        self.EasterEgg = []
        for i in range(2):
            self.EasterEgg.append(EasterEgg(self))
        
        self.sprites = [self.EasterBunny,
                        self.EasterEgg]
        
    def process(self):
        for EasterEgg in self.EasterEgg:
            if self.EasterBunny.collidesWith(EasterEgg):
                EasterEgg.reset()
    
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()