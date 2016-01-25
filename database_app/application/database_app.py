# John Dunham
# Defines the core of the view component for this application.

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.widget import Widget

class DatabaseApp(App):
	def build(self):
		return DatabaseRoot()


class DatabaseRoot(Widget):
	pass


class RootRibbon(BoxLayout):
     pass
