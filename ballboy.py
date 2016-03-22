from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.properties import ObjectProperty
from random import randint
import math

class GameWidget(FloatLayout):
    
    # ob1 = ObjectProperty(None)
    
    
    def _generate_obstacles(self, vel=(0,4)):
        num_obstacles = int(math.floor(1/(self.ball.size_hint[1]*3)) + 1)
        for i in xrange(num_obstacles):
            # generate all obstacles above screen
            space = randint(self.ball.width,self.ball.width*8.5)
            height = 600 - (i * self.ball.height * 1.5)
            
            self.ob1 = Obstacle(pos=(space,height))
            ob2 = Obstacle(pos=(self.ball.width*-9.3+space,height))
            self.add_widget(self.ob1)
            self.add_widget(ob2)
            
            # self.append(ob1)
    
    def __init__(self, **kwargs):
        super (GameWidget, self).__init__(**kwargs)
        self.ball = Ball()
        self.add_widget(self.ball)
        self.obR = []
        self.obL = []
        self._generate_obstacles()
        Clock.schedule_interval(self.update, 1.0/60.0)
        
    def on_touch_move(self, touch):
        self.ball.center_x = touch.x
        self.ball.center_y = touch.y
        
    #def move(self):
    #    self.pos = Vector(*self.velocity) + self.pos
        
    def update(self, dt):
        num_obstacles = int(math.floor(1/(self.ball.size_hint[1]*3)) + 1)
        for i in xrange(num_obstacles):
            self.obR
            self.ob1.move(dt)
        
    #def serve_ball(self, vel=(0,4)):
     #   self.ob1.velocity = Vector(0,4).rotate(randint(0,360))
    
class Obstacle(Widget):
    def move(self, dt):
        self.center_y += 0.01 * dt
    pass

class Ball(Widget):
    pass


class BallGame(App):
    def build(self):
        game = GameWidget()
        #game.serve_ball()
        #Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    
    
if __name__ == "__main__":
    BallGame().run()