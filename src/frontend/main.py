from kivy.app import App
from kivy.uix.widget import Widget
import kivy

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()
    
if __name__ == 'frontend.main':
    print(kivy.__version__)
    PongApp().run()