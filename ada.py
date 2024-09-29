# ---------Importing Libraries-------------
#from app2 import model
from kivy.app import App # Create an app instance to build the window
from kivy.uix.widget import Widget # Is all the features that are placed on the app
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty # Are made to keep the compatibility between the laguages
from kivy.core.window import Window
from kivy.uix.label import Label
# ---------Importing Libraries-------------
class Mensaje(Widget):
    texto = StringProperty("")
    pass
class Interface(Widget):
    prompt_input = ObjectProperty(None)
    carousel = ObjectProperty(None)
    send = ObjectProperty(None)
    respose = ObjectProperty(None)
    
    def ask(self):
        text = self.prompt_input.text
        # answer = model.generate_content(text)
        # self.carousel.add_widget((Label(text = answer.text)))
        # self.carousel.load_next()
Window.size = (400, 600) 
class AdaApp(App):
    def build(self):
        
        return Interface()

AdaApp().run()