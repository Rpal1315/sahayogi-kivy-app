from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import command_helper
import base


class AssistantApp(MDApp):
    def build(self):
        screen = Screen()
        self.command_box = Builder.load_string(command_helper)
        screen.add_widget(self.command_box)
        button = MDFillRoundFlatButton(text='RUN',pos_hint={"center_x": 0.5, "center_y": 0.7}, on_release=self.send_command, md_bg_color = [0.627, 0.125, 0.941, 1])
        screen.add_widget(button)
        return screen

    def send_command(self, obj):
        close_buttons = MDRaisedButton(text='Close', md_bg_color = [0.627, 0.125, 0.941, 1], on_release=self.close_dialog)
        base.main(self.command_box.text)
        out = base.main.respn
        self.dialog = MDDialog(title='Output',
                          text=out,
                          size_hint=(0.8, 0.8),
                          buttons=[close_buttons])
        self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()



AssistantApp().run()
