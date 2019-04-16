# GPL v3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk, Gedit, Gio

class SaveAsRootAppActivatable(GObject.Object, Gedit.AppActivatable):
	app = GObject.property(type=Gedit.App)
	__gtype_name__ = "SaveAsRootAppActivatable"
	
	def __init__(self):
		GObject.Object.__init__(self)
	
	def do_activate(self):
		self.menu_ext = self.extend_menu('file-section')
		self.menu_item = Gio.MenuItem.new(_("Edit as administrator…"), 'win.open_as_root')
		self.menu_ext.append_menu_item(self.menu_item)
	
	def do_deactivate(self):
		self.menu_item = None
		self.menu_ext = None

class OpenAsRootWindowActivatable(GObject.Object, Gedit.WindowActivatable):
	window = GObject.property(type=Gedit.Window)
	__gtype_name__ = "OpenAsRootWindowActivatable"
	
	def __init__(self):
		GObject.Object.__init__(self)
	
	def do_activate(self):
		# Defining the action which was set earlier in AppActivatable.
		action = Gio.SimpleAction(name='open_as_root')
		action.connect('activate', self.action_cb)
		self.window.add_action(action)
		
		self.window.connect('active-tab-changed', self.update_item_state)
		self.window.connect('active-tab-state-changed', self.update_item_state)
	
	def do_deactivate(self):
		pass
	
	def do_update_state(self):
		pass
	
	def update_item_state(self, *args):
		if self.window.get_active_document() is None or self.window.get_active_document().get_location() is None:
			# if there is no document, we disable the action, so we don't get NoneException
			self.window.lookup_action('open_as_root').set_enabled(False)
		elif 'admin' in self.window.get_active_document().get_location().get_uri_scheme():
			# if the document is already opened as root, we disable the action too
			self.window.lookup_action('open_as_root').set_enabled(False)
		else:
			self.window.lookup_action('open_as_root').set_enabled(True)
	
	def action_cb(self, action, data):
		doc = self.window.get_active_document()
		my_uri = 'admin://' + doc.get_uri_for_display()
		self.window.create_tab_from_location(Gio.File.new_for_uri(my_uri), None, 0, 0, False, True)


