# John Dunham
# Defines the core of the view component for this application.

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

import os


import control.c_core as control


# Controller.
class DatabaseApp(App):
     def build(self):
          # controller keeps track of the root view and communicates with it.
          self.controller = control.Controller(DatabaseRoot())          
          return self.controller.view


# View
######################################################
class DatabaseRoot(Widget):
     pass


class RootRibbon(BoxLayout):
     pass
     
class FileDropDown(DropDown):
     def build(self):
          pass

     def open_database(self):
          print("opening")
          file_opener = LoadDialog(close=self.dismiss_popup,load=self.open_file)
          self._popup = Popup(title="Open file", content=file_opener,
                            size_hint=(.9, .9))
          self._popup.open()
     
     def dismiss_popup(self):
          self._popup.dismiss()
          
     def open_file(self, path, file_name):
         controller = App.get_running_app().controller
         controller.open_db(os.path.join(path,file_name[0]))
         
         self.dismiss_popup()
         
class LoadDialog(Widget):
     load  = ObjectProperty(None)
     close = ObjectProperty(None)
     

# Register the appropriate classes.
Factory.register('LoadDialog',cls=LoadDialog)
################################################################
