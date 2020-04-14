from kivy.app import App
from kivy.uix.label import Label

import platform

class CourseApp(App):
    def build(self):
        return Label(text='{0}'.format(platform.machine()))


CourseApp().run()