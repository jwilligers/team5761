from kivy.app import App
from kivy.uix.widget import Widget

class Game(Widget):
	pass
	
class GameApp(App):
	def build(self):
		return Game()
		
if __name__ == "__main__":
	GameApp().run()