from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class Game(Widget):
	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		with self.canvas:
			Color(.5, .5, 1.0)
			Rectangle(pos=(0, 0), size = self.size)
	
class GameApp(App):
	def build(self):
		return Game(size=Window.size)
		
if __name__ == "__main__":
	GameApp().run()