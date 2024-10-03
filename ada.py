# ---------Importing Libraries-------------
from app2 import model
from kivy.app import App # Create an app instance to build the window
from kivy.uix.widget import Widget # Is all the features that are placed on the app
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty # Are made to keep the compatibility between the laguages
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
# ---------Importing Libraries-------------
class Mensaje(BoxLayout):
    texto_pregunta = ObjectProperty(None)
    texto_respuesta = ObjectProperty(None)

class Interface(Widget):
    prompt_input = ObjectProperty(None)
    carousel = ObjectProperty(None)
    send = ObjectProperty(None)
    respose = ObjectProperty(None)
    space = StringProperty('250dp')
    def __init__(self, **kwargs):
        super(Interface,self).__init__(**kwargs)
        Window.bind(on_resize=self.on_window_resize)

    def ask(self):
        text = self.prompt_input.text
        mensaje = Mensaje()
        answer = model.generate_content([text,"contesta lo más corto posible sin extenderte"])
        mensaje.texto_pregunta.text = text
        mensaje.texto_respuesta.text = answer.text
        self.carousel.add_widget((mensaje))
    
    def on_window_resize(self, window, height, width):
        if Window.size[0] != 400:
            self.space = '120dp'
        else:
            self.space = '250dp'

Window.size = (400, 600)
Window.borderLess = False 
Window.fullscreen = False
class AdaApp(App):
    def build(self):
        
        return Interface()

AdaApp().run()