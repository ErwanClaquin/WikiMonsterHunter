"""from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello World")


myapp = MyApp()
myapp.run()"""
from Monster import *


m1 = Monster("Rathian")
print(m1.desciption)
m1.updateAllMonster(language="FR")
print(m1.desciption)
m1.updateAllMonster(language="AEFAEF")
print(m1.desciption)
