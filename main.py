from riot_api import get_data
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from getsumm import get_spell
from kivy.uix.image import Image


# player_one_champion = data[0][0]
# player_one_d = data[0][1]
# player_one_f = data[0][2]

# player_two_champion = data[1][0]
# player_two_d = data[1][1]
# player_two_f = data[1][2]

# player_three_champion = data[2][0]
# player_three_d = data[2][1]
# player_three_f = data[2][2]

# player_four_champion = data[3][0]
# player_four_d = data[3][1]
# player_four_f = data[3][2]

# player_five_champion = data[4][0]
# player_five_d = data[4][1]
# player_five_f = data[4][2]


class WelcomeWindow(Screen):
    summoner = ObjectProperty(None)
    server = ObjectProperty(None)

    def getStartedBtn(self):
        self.reset()
        sm.current = "game"

    def get_user_info(self):
        GameWindow.data = get_data(self.server.text, self.summoner.text)
        GameWindow.player_one_d = "spells/" + get_spell(GameWindow.data[0][1])
        GameWindow.image.source = GameWindow.player_one_d

    def reset(self):
        self.summoner.text = ""


class GameWindow(Screen):
    data = []
    player_one_d = ""
    image = Image(source="")

    def get_image_1(self):
        print(self.player_one_d)
        return self.player_one_d

    def test_print(self):
        print("Button Pressed")

    def on_enter(self, *args):
        print(self.data)
        print(self.player_one_d)

    def exitBtn(self):
        sm.current = "welcome"


class WindowManagaer(ScreenManager):
    pass


kv = Builder.load_file("summonertimer.kv")
sm = WindowManagaer()
screens = [WelcomeWindow(name="welcome"), GameWindow(name='game')]

for screen in screens:
    sm.add_widget(screen)

sm.current = "welcome"


class SummonerTimerApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    SummonerTimerApp().run()
