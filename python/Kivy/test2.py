from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class Sprite(Image):
	def __init__(self, **kwargs):
			super(Sprite, self).__init__(**kwargs)
			self.size = self.texture_size
	

class Game(Widget):
	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		self.background = Sprite(source = 'images/background.png')
		self.size = self.background.size
		self.add_widget(self.background)
		self.add_widget(Sprite(source = 'images/bird.png'))
		
class GameApp(App):
	def build(self):
		game = Game()
		Window.size = game.size
		return game
		
if __name__ == "__main__":
	GameApp().run()