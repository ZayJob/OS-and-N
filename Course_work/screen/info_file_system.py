import os
import sys
import json

from kivy.uix.screenmanager import Screen


class InfoFileSystemScreen(Screen):

    def select(self, *args): 
        try: self.label.text = args[1][0] 
        except: pass
    
    def get_info_about_file_system(self):
        path = sys.executable
        while os.path.split(path)[1]:
            path = os.path.split(path)[0]

        folder = []
        for i in os.walk(os.path.curdir):
            folder.append(i[0])
                
        json_string = json.dumps(folder[:10], ensure_ascii=True, indent=4)

        print(json_string)

        self.answer.text = json_string
