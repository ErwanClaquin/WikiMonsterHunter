from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from Monster import *


class MenuWindow(Screen):

    def build(self):
        self.name = "Menu"
        # On joue un son pour l'écran principale:
        # TODO : soundMenu.play()

        # Image de l'écran principal :
        self.Img = Image(source='MHW_picture_FirstWindow.jpg', allow_stretch=True, keep_ratio=False)
        # On ajoute l'image
        self.add_widget(self.Img)

        # On cree un bouton:
        self.buttonNextPage = Button(text='Enter in Monster Hunter World!', background_color=(0, 0, 0, 0),
                                     color=(1, 1, 1, 1), font_size='30sp')
        self.buttonNextPage.bind(on_press=self.nextPage)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.buttonNextPage)

        # On ajoute l'ecran menu dans le ScreenManager:
        sm.add_widget(self)

    def nextPage(self, instance):
        # TODO : soundMenu.stop()
        sm.current = "Choice Level Monsters"
        sm.transition.direction = "left"


class ChoiceLevelMonsters(Screen):
    def build(self):
        self.name = "Choice Level Monsters"
        # On charge un son pour l'écran principal:

        # On cree une disposition pour l'affichage permettant de choisir le niveau des monstres:
        monsterLevelFloatLayout = FloatLayout()

        self.buttonToMH3 = Button(text="MH3")
        self.buttonToMH3.pos_hint = {"x": 0.25, "y": 0.6}
        self.buttonToMH3.size_hint = (0.5, 0.2)
        self.buttonToMH3.bind(on_press=self.pageToMH3)
        monsterLevelFloatLayout.add_widget(self.buttonToMH3)

        self.buttonToMHW = Button(text="MHW")
        self.buttonToMHW.pos_hint = {"x": 0.25, "y": 0.4}
        self.buttonToMHW.size_hint = (0.5, 0.2)
        self.buttonToMHW.bind(on_press=self.pageToMHW)
        monsterLevelFloatLayout.add_widget(self.buttonToMHW)

        self.buttonToMHWIceborn = Button(text="MHWIceborn")
        self.buttonToMHWIceborn.pos_hint = {"x": 0.25, "y": 0.2}
        self.buttonToMHWIceborn.size_hint = (0.5, 0.2)
        self.buttonToMHWIceborn.bind(on_press=self.pageToMHWIceborn)
        monsterLevelFloatLayout.add_widget(self.buttonToMHWIceborn)

        self.add_widget(monsterLevelFloatLayout)

        # On cree un bouton:
        self.buttonPreviousPage = Button(text='Go Back', font_size='30sp')
        self.buttonPreviousPage.pos_hint = {"x": 0.0, "y": 0.0}
        self.buttonPreviousPage.size_hint = (0.2, 0.1)
        self.buttonPreviousPage.bind(on_press=self.previousPage)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.buttonPreviousPage)
        # On ajoute l'ecran menu dans le ScreenManager:
        sm.add_widget(self)

    def previousPage(self, instance):
        sm.current = "Menu"
        sm.transition.direction = "right"
        # TODO : soundMenu.play()

    def pageToMH3(self, instance):
        sm.current = "MH3"
        sm.transition.direction = "left"

    def pageToMHW(self, instance):
        sm.current = "MHW"
        sm.transition.direction = "left"

    def pageToMHWIceborn(self, instance):
        sm.current = "MHWIceborn"
        sm.transition.direction = "left"


# Faut-il faire 9 classes ? Ou alors envoyer une liste de monstres present en parametre ainsi que le nom
class MonsterHunterGame(Screen):
    def build(self, name, listGameMonsters):
        self.name = name
        self.listMonsters = listMonsters

        s = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        s.do_scroll_y = True
        s.do_scroll_x = False
        l = GridLayout(cols=4, spacing=[10, 5], size_hint_y=None, padding=[175, 100, 0, 0])
        l.bind(minimum_height=l.setter('height'))

        i = 0.9
        for monster in listGameMonsters:
            self.Img = Image(source='MHW_picture_FirstWindow.jpg', allow_stretch=True, keep_ratio=False)
            self.text = Label(text=monster.name)
            self.buttonToMonster = Button(text="", font_size='30sp', width=150, height=150, size_hint_y=None,
                                          background_normal='MHW_picture_FirstWindow.jpg')
            self.buttonToMonster.bind(on_press=self.pageToMonster)
            # On ajoute le bouton dans l'affichage:
            l.add_widget(self.text)
            l.add_widget(self.buttonToMonster)
            i -= 0.1
        s.add_widget(l)
        self.add_widget(s)
        # On cree un bouton:
        self.buttonPreviousPage = Button(text='Go Back', font_size='30sp')
        self.buttonPreviousPage.pos_hint = {"x": 0.0, "y": 0.0}
        self.buttonPreviousPage.size_hint = (0.2, 0.1)
        self.buttonPreviousPage.bind(on_press=self.previousPage)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.buttonPreviousPage)

        sm.add_widget(self)

    def previousPage(self, instance):
        sm.current = "Choice Level Monsters"
        sm.transition.direction = "right"

    def pageToMonster(self, instance):
        sm.current = instance.text
        sm.transition.direction = "left"


class MonstersWindow(Screen):
    def build(self, name, nbListMonsters, namePreviousPage):
        self.namePreviousPage = namePreviousPage
        for monster in nbListMonsters:
            if monster.name == name:
                self.name = name
                layout = BoxLayout(orientation='vertical')
                text1 = Label(text=monster.displayName)
                text2 = Label(text=monster.description)
                layout.add_widget(text1)
                layout.add_widget(text2)

                self.add_widget(layout)

        # On cree un bouton:
        self.buttonPreviousPage = Button(text='Go Back', font_size='30sp')
        self.buttonPreviousPage.pos_hint = {"x": 0.0, "y": 0.0}
        self.buttonPreviousPage.size_hint = (0.2, 0.1)
        self.buttonPreviousPage.bind(on_press=self.previousPage)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.buttonPreviousPage)

        sm.add_widget(self)

    def previousPage(self, instance):
        sm.current = self.namePreviousPage
        sm.transition.direction = "right"


class MonsterApp(App):
    def build(self):
        menu = MenuWindow()  # On definit l'ecran menu
        menu.build()  # On le construit
        choiceLevelMonster = ChoiceLevelMonsters()
        choiceLevelMonster.build()
        mh3 = MonsterHunterGame()
        mh3.build("MH3", listMonsterHunter3)

        mhw = MonsterHunterGame()
        mhw.build("MHW", listMonsterHunterWorld)

        mhwiceborn = MonsterHunterGame()
        mhwiceborn.build("MHWIceborn", listMonsterHunterWorldIceborn)

        for monster in listMonsterHunter3:
            MonstersWindow.build(MonstersWindow(), monster.name, listMonsterHunter3, "MH3")

        for monster in listMonsterHunterWorld:
            MonstersWindow.build(MonstersWindow(), monster.name, listMonsterHunterWorld, "MHW")

        for monster in listMonsterHunterWorldIceborn:
            MonstersWindow.build(MonstersWindow(), monster.name, listMonsterHunterWorldIceborn, "MHWIceborn")

        sm.current = "Menu"  # On envoie en premier l'ecran du menu grace a son nom
        return sm


# importations des sons:
# TODO : soundMenu = SoundLoader.load("nergigante-roar.mp3")


langue = "EN"
listMonsters = createMonster()
listMonsterHunter3 = []
listMonsterHunterWorld = []
listMonsterHunterWorldIceborn = []
for i in range(0, len(listMonsters)):
    if listMonsters[i].game == "Monster Hunter 3":
        listMonsterHunter3.append(listMonsters[i])
    elif listMonsters[i].game == "Monster Hunter World":
        listMonsterHunterWorld.append(listMonsters[i])
    elif listMonsters[i].game == "Monster Hunter World Iceborn":
        listMonsterHunterWorldIceborn.append(listMonsters[i])

sm = ScreenManager()  # Create the screen manager, il est forcement global
MonsterApp().run()
