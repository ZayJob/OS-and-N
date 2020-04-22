import platform

from kivy.uix.screenmanager import Screen
from kivy.utils import platform as pl


class InfoDeviceScreen(Screen):

    def get_info_about_device(self):
        self.property_1.text = platform.machine()
        self.property_2.text = " ".join(platform.version().split()[:2])
        self.property_3.text = " ".join(platform.version().split()[4:])
        self.property_4.text = platform.architecture()[0]
        if pl != 'android':
            if platform.architecture()[1] == "":
                self.property_5.text = "None"
            else:
                self.property_5.text = platform.architecture()[1]
            if " ".join(platform.linux_distribution()) == "":
                self.property_6.text = "None"
            else:
                self.property_6.text = " ".join(platform.linux_distribution())
            if platform.java_ver()[0] == "":
                self.property_7.text = "None"
            else:
                self.property_7.text = platform.java_ver()[0]
            if platform.libc_ver()[0] == "":
                self.property_8.text = "None"
            else:
                self.property_8.text = platform.libc_ver()[0]
        else:
            self.property_5.text = "None"
            self.property_6.text = "None"
            self.property_7.text = "None"
            self.property_8.text = "None"

        self.property_9.text = platform.node()

        if pl != 'android':
            self.property_10.text = platform.system()
            self.property_11.text = platform.processor()
        else:
            self.property_10.text = 'android'
            self.property_11.text = 'None'
