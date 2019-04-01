from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, NumericProperty, ReferenceListProperty, ObjectProperty

class AnalogStick(Widget):
    x = NumericProperty(0)
    y = NumericProperty(0)
    pos = ReferenceListProperty(x, y)

class DPad(Widget):
    up = BooleanProperty(False)
    right = BooleanProperty(False)
    down = BooleanProperty(False)
    left = BooleanProperty(False)

class GameController(Widget):
    left_stick = ObjectProperty(None)
    right_stick = ObjectProperty(None)
    d_pad = ObjectProperty(None)

class GameControllerApp(App):
    def build(self):
        return GameController()

if __name__ == '__main__':
    GameControllerApp().run()
