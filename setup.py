import os
from setuptools import setup

setup(
	name         = "A Collector's DB",
	version      = "0.0.1",
	author       = "John Dunham",
	author_email = "john@johndunhamgames.com",
	description  = ("An app for maintaining my collection."),
	packages     = ['database_app'],
	entry_points = {
		'gui_scripts': [
			'database_app = database_app.__main__:main' #"name_of_executable = module.with:function_to_execute"
		]
	}
)