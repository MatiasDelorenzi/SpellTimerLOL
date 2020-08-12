from riot_api import get_data
from gameinfo import get_server, get_spell_image, get_champion_image, get_cd
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class WelcomeWindow(Screen):
    summoner = ObjectProperty(None)
    server = ObjectProperty(None)

    def get_started(self):
        LoadingWindow.sv = self.server
        LoadingWindow.summ = self.summoner
        sm.current = 'loading'


class GameWindow(Screen):
    data = []
    player_one_d = ""
    player_one_f = ""
    player_one_champion = ""
    player_two_d = ""
    player_two_f = ""
    player_two_champion = ""
    player_three_d = ""
    player_three_f = ""
    player_three_champion = ""
    player_four_d = ""
    player_four_f = ""
    player_four_champion = ""
    player_five_d = ""
    player_five_f = ""
    player_five_champion = ""
    started1 = False
    started1_1 = False
    started2 = False
    started2_1 = False
    started3 = False
    started3_1 = False
    started4 = False
    started4_1 = False
    started5 = False
    started5_1 = False

    def on_enter(self, *args):
        self.player_one_champion = self.data[0][0]
        self.player_one_d = self.data[0][1]
        self.player_one_f = self.data[0][2]

        self.player_two_champion = self.data[1][0]
        self.player_two_d = self.data[1][1]
        self.player_two_f = self.data[1][2]

        self.player_three_champion = self.data[2][0]
        self.player_three_d = self.data[2][1]
        self.player_three_f = self.data[2][2]

        self.player_four_champion = self.data[3][0]
        self.player_four_d = self.data[3][1]
        self.player_four_f = self.data[3][2]

        self.player_five_champion = self.data[4][0]
        self.player_five_d = self.data[4][1]
        self.player_five_f = self.data[4][2]

        self.ids.enemy_1_spell_1.background_normal = get_spell_image(self.player_one_d)
        self.ids.enemy_1_spell_2.background_normal = get_spell_image(self.player_one_f)
        self.ids.enemy_1_champion.source = get_champion_image(self.player_one_champion)

        self.ids.enemy_2_spell_1.background_normal = get_spell_image(self.player_two_d)
        self.ids.enemy_2_spell_2.background_normal = get_spell_image(self.player_two_f)
        self.ids.enemy_2_champion.source = get_champion_image(self.player_two_champion)

        self.ids.enemy_3_spell_1.background_normal = get_spell_image(self.player_three_d)
        self.ids.enemy_3_spell_2.background_normal = get_spell_image(self.player_three_f)
        self.ids.enemy_3_champion.source = get_champion_image(self.player_three_champion)

        self.ids.enemy_4_spell_1.background_normal = get_spell_image(self.player_four_d)
        self.ids.enemy_4_spell_2.background_normal = get_spell_image(self.player_four_f)
        self.ids.enemy_4_champion.source = get_champion_image(self.player_four_champion)

        self.ids.enemy_5_spell_1.background_normal = get_spell_image(self.player_five_d)
        self.ids.enemy_5_spell_2.background_normal = get_spell_image(self.player_five_f)
        self.ids.enemy_5_champion.source = get_champion_image(self.player_five_champion)

    def start_enemy1_spell1(self):
        if self.started1:
            self.started1 = False
            self.stop_enemy1_spell1()
        else:
            self.started1 = True
            self.ids.enemy_1_spell_1.text = get_cd(self.player_one_d)
            self.timer_enemy1_spell1 = Clock.schedule_interval(self.update_enemy1_spell1, 1)
            self.ids.enemy_1_spell_1.background_normal = "./spells/" + self.player_one_d + "Dark.png"

    def update_enemy1_spell1(self, *args):
        if int(self.ids.enemy_1_spell_1.text) > 0:
            self.ids.enemy_1_spell_1.text = str(int(self.ids.enemy_1_spell_1.text) - 1)
        else:
            self.stop_enemy1_spell1()
            self.started1 = False

    def stop_enemy1_spell1(self, *args):
        self.timer_enemy1_spell1.cancel()
        self.ids.enemy_1_spell_1.text = ""
        self.ids.enemy_1_spell_1.background_normal = get_spell_image(self.player_one_d)

########################################################################

    def start_enemy1_spell2(self):
        if self.started1_1:
            self.started1_1 = False
            self.stop_enemy1_spell2()
        else:
            self.started1_1 = True
            self.ids.enemy_1_spell_2.text = get_cd(self.player_one_f)
            self.timer_enemy1_spell2 = Clock.schedule_interval(self.update_enemy1_spell2, 1)
            self.ids.enemy_1_spell_2.background_normal = "./spells/" + self.player_one_f + "Dark.png"

    def update_enemy1_spell2(self, *args):
        if int(self.ids.enemy_1_spell_2.text) > 0:
            self.ids.enemy_1_spell_2.text = str(int(self.ids.enemy_1_spell_2.text) - 1)
        else:
            self.stop_enemy1_spell2()
            self.started1_1 = False

    def stop_enemy1_spell2(self, *args):
        self.timer_enemy1_spell2.cancel()
        self.ids.enemy_1_spell_2.text = ""
        self.ids.enemy_1_spell_2.background_normal = get_spell_image(self.player_one_f)

########################################################################

    def start_enemy2_spell1(self):
        if self.started2:
            self.started2 = False
            self.stop_enemy2_spell1()
        else:
            self.started2 = True
            self.ids.enemy_2_spell_1.text = get_cd(self.player_two_d)
            self.timer_enemy2_spell1 = Clock.schedule_interval(self.update_enemy2_spell1, 1)
            self.ids.enemy_2_spell_1.background_normal = "./spells/" + self.player_two_d + "Dark.png"

    def update_enemy2_spell1(self, *args):
        if int(self.ids.enemy_2_spell_1.text) > 0:
            self.ids.enemy_2_spell_1.text = str(int(self.ids.enemy_2_spell_1.text) - 1)
        else:
            self.stop_enemy2_spell1()
            self.started2 = False

    def stop_enemy2_spell1(self, *args):
        self.timer_enemy2_spell1.cancel()
        self.ids.enemy_2_spell_1.text = ""
        self.ids.enemy_2_spell_1.background_normal = get_spell_image(self.player_two_d)

########################################################################

    def start_enemy2_spell2(self):
        if self.started2_1:
            self.started2_1 = False
            self.stop_enemy2_spell2()
        else:
            self.started2_1 = True
            self.ids.enemy_2_spell_2.text = get_cd(self.player_two_f)
            self.timer_enemy2_spell2 = Clock.schedule_interval(self.update_enemy2_spell2, 1)
            self.ids.enemy_2_spell_2.background_normal = "./spells/" + self.player_two_f + "Dark.png"

    def update_enemy2_spell2(self, *args):
        if int(self.ids.enemy_2_spell_2.text) > 0:
            self.ids.enemy_2_spell_2.text = str(int(self.ids.enemy_2_spell_2.text) - 1)
        else:
            self.stop_enemy2_spell2()
            self.started2_1 = False

    def stop_enemy2_spell2(self, *args):
        self.timer_enemy2_spell2.cancel()
        self.ids.enemy_2_spell_2.text = ""
        self.ids.enemy_2_spell_2.background_normal = get_spell_image(self.player_two_f)

########################################################################

    def start_enemy3_spell1(self):
        if self.started3:
            self.started3 = False
            self.stop_enemy3_spell1()
        else:
            self.started3 = True
            self.ids.enemy_3_spell_1.text = get_cd(self.player_three_d)
            self.timer_enemy3_spell1 = Clock.schedule_interval(self.update_enemy3_spell1, 1)
            self.ids.enemy_3_spell_1.background_normal = "./spells/" + self.player_three_d + "Dark.png"

    def update_enemy3_spell1(self, *args):
        if int(self.ids.enemy_3_spell_1.text) > 0:
            self.ids.enemy_3_spell_1.text = str(int(self.ids.enemy_3_spell_1.text) - 1)
        else:
            self.stop_enemy3_spell1()
            self.started3 = False

    def stop_enemy3_spell1(self, *args):
        self.timer_enemy3_spell1.cancel()
        self.ids.enemy_3_spell_1.text = ""
        self.ids.enemy_3_spell_1.background_normal = get_spell_image(self.player_three_d)

########################################################################

    def start_enemy3_spell2(self):
        if self.started3_1:
            self.started3_1 = False
            self.stop_enemy3_spell2()
        else:
            self.started3_1 = True
            self.ids.enemy_3_spell_2.text = get_cd(self.player_three_f)
            self.timer_enemy3_spell2 = Clock.schedule_interval(self.update_enemy3_spell2, 1)
            self.ids.enemy_3_spell_2.background_normal = "./spells/" + self.player_three_f + "Dark.png"

    def update_enemy3_spell2(self, *args):
        if int(self.ids.enemy_3_spell_2.text) > 0:
            self.ids.enemy_3_spell_2.text = str(int(self.ids.enemy_3_spell_2.text) - 1)
        else:
            self.stop_enemy3_spell2()
            self.started3_1 = False

    def stop_enemy3_spell2(self, *args):
        self.timer_enemy3_spell2.cancel()
        self.ids.enemy_3_spell_2.text = ""
        self.ids.enemy_3_spell_2.background_normal = get_spell_image(self.player_three_f)

########################################################################

    def start_enemy4_spell1(self):
        if self.started4:
            self.started4 = False
            self.stop_enemy4_spell1()
        else:
            self.started4 = True
            self.ids.enemy_4_spell_1.text = get_cd(self.player_four_d)
            self.timer_enemy4_spell1 = Clock.schedule_interval(self.update_enemy4_spell1, 1)
            self.ids.enemy_4_spell_1.background_normal = "./spells/" + self.player_four_d + "Dark.png"

    def update_enemy4_spell1(self, *args):
        if int(self.ids.enemy_4_spell_1.text) > 0:
            self.ids.enemy_4_spell_1.text = str(int(self.ids.enemy_4_spell_1.text) - 1)
        else:
            self.stop_enemy4_spell1()
            self.started4 = False

    def stop_enemy4_spell1(self, *args):
        self.timer_enemy4_spell1.cancel()
        self.ids.enemy_4_spell_1.text = ""
        self.ids.enemy_4_spell_1.background_normal = get_spell_image(self.player_four_d)

########################################################################

    def start_enemy4_spell2(self):
        if self.started4_1:
            self.started4_1 = False
            self.stop_enemy4_spell2()
        else:
            self.started4_1 = True
            self.ids.enemy_4_spell_2.text = get_cd(self.player_four_f)
            self.timer_enemy4_spell2 = Clock.schedule_interval(self.update_enemy4_spell2, 1)
            self.ids.enemy_4_spell_2.background_normal = "./spells/" + self.player_four_f + "Dark.png"

    def update_enemy4_spell2(self, *args):
        if int(self.ids.enemy_4_spell_2.text) > 0:
            self.ids.enemy_4_spell_2.text = str(int(self.ids.enemy_4_spell_2.text) - 1)
        else:
            self.stop_enemy4_spell2()
            self.started4_1 = False

    def stop_enemy4_spell2(self, *args):
        self.timer_enemy4_spell2.cancel()
        self.ids.enemy_4_spell_2.text = ""
        self.ids.enemy_4_spell_2.background_normal = get_spell_image(self.player_four_f)

########################################################################

    def start_enemy5_spell1(self):
        if self.started5:
            self.started5 = False
            self.stop_enemy5_spell1()
        else:
            self.started5 = True
            self.ids.enemy_5_spell_1.text = get_cd(self.player_five_d)
            self.timer_enemy5_spell1 = Clock.schedule_interval(self.update_enemy5_spell1, 1)
            self.ids.enemy_5_spell_1.background_normal = "./spells/" + self.player_five_d + "Dark.png"

    def update_enemy5_spell1(self, *args):
        if int(self.ids.enemy_5_spell_1.text) > 0:
            self.ids.enemy_5_spell_1.text = str(int(self.ids.enemy_5_spell_1.text) - 1)
        else:
            self.stop_enemy5_spell1()
            self.started5 = False

    def stop_enemy5_spell1(self, *args):
        self.timer_enemy5_spell1.cancel()
        self.ids.enemy_5_spell_1.text = ""
        self.ids.enemy_5_spell_1.background_normal = get_spell_image(self.player_five_d)

########################################################################

    def start_enemy5_spell2(self):
        if self.started5_1:
            self.started5_1 = False
            self.stop_enemy5_spell2()
        else:
            self.started5_1 = True
            self.ids.enemy_5_spell_2.text = get_cd(self.player_five_f)
            self.timer_enemy5_spell2 = Clock.schedule_interval(self.update_enemy5_spell2, 1)
            self.ids.enemy_5_spell_2.background_normal = "./spells/" + self.player_five_f + "Dark.png"

    def update_enemy5_spell2(self, *args):
        if int(self.ids.enemy_5_spell_2.text) > 0:
            self.ids.enemy_5_spell_2.text = str(int(self.ids.enemy_5_spell_2.text) - 1)
        else:
            self.stop_enemy5_spell2()
            self.started5_1 = False

    def stop_enemy5_spell2(self, *args):
        self.timer_enemy5_spell2.cancel()
        self.ids.enemy_5_spell_2.text = ""
        self.ids.enemy_5_spell_2.background_normal = get_spell_image(self.player_five_f)

    def exit_btn(self):
        sm.current = "welcome"


class ErrorWindow(Screen):
    def try_again(self):
        sm.current = "welcome"


class LoadingWindow(Screen):
    sv = ObjectProperty(None)
    summ = ObjectProperty(None)

    def on_enter(self, *args):
        server_key = get_server(self.sv.text)
        try:
            get_data(server_key, self.summ.text)
        except:
            sm.current = 'error'
        else:
            GameWindow.data = get_data(server_key, self.summ.text)
            sm.current = 'game'


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("summonertimer.kv")
sm = WindowManager()
screens = [WelcomeWindow(name="welcome"), GameWindow(name='game'), ErrorWindow(name='error'),
           LoadingWindow(name='loading')]

for screen in screens:
    sm.add_widget(screen)

sm.current = "welcome"


class SummonerTimerApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    SummonerTimerApp().run()
