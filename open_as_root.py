
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk, Gedit, Gio

class SaveAsRootAppActivatable(GObject.Object, Gedit.AppActivatable):
	app = GObject.property(type=Gedit.App)
	__gtype_name__ = "SaveAsRootAppActivatable"

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		self._build_menu()

	def do_deactivate(self):
		self._remove_menu()

	#call me in do_activate
	def _build_menu(self):
		# Get the extension from file menu		
		self.menu_ext = self.extend_menu("file-section")
#		self.menu_ext = self.extend_menu("file-section-1")
		my_menu_item = Gio.MenuItem.new("Open as root", 'win.open_as_root')
		self.menu_ext.append_menu_item(my_menu_item)
		# Setting accelerators, now our action is called when Ctrl+Alt+1 is pressed.
		self.app.set_accels_for_action("win.open_as_root", ("<Primary>r", None))

	#call me in do_deactivate
	def _remove_menu(self):
		# removing accelerator and destroying menu items
		self.app.set_accels_for_action("win.open_as_root", ())
		self.menu_ext = None
		self.menu_item = None


class OpenAsRootWindowActivatable(GObject.Object, Gedit.WindowActivatable):
	window = GObject.property(type=Gedit.Window)
	__gtype_name__ = "OpenAsRootWindowActivatable"

	def __init__(self):
		GObject.Object.__init__(self)
		# This is the attachment we will make to bottom panel.
		self.bottom_bar = Gtk.Box()
	
	#this is called every time the gui is updated
	def do_update_state(self):
		# if there is no document in sight, we disable the action, so we don't get NoneException
		if self.window.get_active_view() is not None:
			self.window.lookup_action('open_as_root').set_enabled(True)

	def do_activate(self):
		# Defining the action which was set earlier in AppActivatable.
		self._connect_menu()

	def _connect_menu(self):
		action = Gio.SimpleAction(name='open_as_root')
		action.connect('activate', self.action_cb)
		self.window.add_action(action)

	def action_cb(self, action, data):
		# On action clear the document.
		doc = self.window.get_active_document()
		my_uri = "admin://"+doc.get_uri_for_display()
		self.window.create_tab_from_location(Gio.File.new_for_uri(my_uri), None, 0, 0, False, True)

	def do_deactivate(self):
		pass


