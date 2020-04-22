from kivy.app import App
from kivy.lang import Builder

from screen.base import BaseScreen


KV = Builder.load_file("templates.kv")


class CourseApp(App):
    def build(self):
        return KV