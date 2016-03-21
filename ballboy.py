from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock
from random import randint

class GameWidget(FloatLayout):
    
    def __init__(self, **kwargs):
        super (GameWidget, self).__init__(**kwargs)
        self.ball = Ball()
        self.add_widget(self.ball)
        self.obstacles = []
        Clock.schedule_interval(self.update, 1.0/60.0)
        
    def on_touch_move(self, touch):
        self.ball.center_x = touch.x
        self.ball.center_y = touch.y
        
    def update(self, dt):
        #check if collision happened
        #check if finger came off screen
        #move blocks down
    
    
class Obstacle(Widget):
    pass

class Ball(Widget):
    pass


class BallGame(App):
    def build(self):
        return GameWidget()
    
    
if __name__ == "__main__":
    BallGame().run()