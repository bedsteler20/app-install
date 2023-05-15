from gi.repository import Gtk


@Gtk.Template(resource_path='/dev/bedsteler20/AppInstall/window.ui')
class AppInstallWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'AppInstallWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_menubutton_activate():
        print("Hello World!")
