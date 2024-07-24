from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from normal_input import NormalInput
from text_input_kuze import KuTextInput

class Layout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(NormalInput())
        self.add_widget(MyTextInput())
        self.add_widget(Widget(size_hint=(1, .5)))

class MainApp(App):
    def build(self):
        return Layout()

MainApp().run()
