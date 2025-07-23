import gi
import os, sys
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("hyprconfig.glade")

        builder.connect_signals(self)

        # Get all input widgets
        self.schemecombobox = builder.get_object("schemeComboBox")
        self.wallpaperchoose = builder.get_object("wallpaperChooser")
        self.modeswitch = builder.get_object("darkModeSwitch")

        self.differentSchemes = ["scheme-neutral",
                            "scheme-content",
                            "scheme-expressive",
                            "scheme-fidelity",
                            "scheme-fruit-salad",
                            "scheme-monochrome",
                            "scheme-rainbow",
                            "scheme-tonal-spot",
                            "scheme-vibrant"]

        self.scheme = self.differentSchemes[int(self.schemecombobox.get_active_id())]
        self.wallpaperMode = "dark"

        self.window = builder.get_object("mainWindow")
        self.window.show_all()

        homeDirectory = os.environ['HOME']
        self.configPath = f"{homeDirectory}/.config/hyprconfig.py"

        if os.path.exists(self.configPath):
            sys.path.append(f"{homeDirectory}/.config/")
            import hyprconfig

            # Set all widgets to old config
            self.wallpaperchoose.set_filename(hyprconfig.oldWallpaper)
            self.wallpaper = hyprconfig.oldWallpaper

            self.schemecombobox.set_active(self.differentSchemes.index(hyprconfig.oldScheme))
            self.scheme = hyprconfig.oldScheme

            self.modeswitch.set_active(True) if hyprconfig.oldWallpaperMode == "dark" else self.modeswitch.set_active(False)
            if hyprconfig.oldWallpaperMode == "dark":
                self.wallpaperMode = "dark"
            else:
                self.wallpaperMode = "light"
        else:
            with open(self.configPath, 'w'): # Creates an empty file
                pass

#####################################
#####################################


    def onWallpaperSelected(self, wallpaperChooser):
        self.wallpaper = wallpaperChooser.get_filename()
        print(self.wallpaper)

    def onSchemeChange(self, schemeComboBox):
        self.scheme = self.differentSchemes[int(schemeComboBox.get_active_id())]
        print(self.scheme)

    def onModeSwitchChange(self, darkModeSwitch, state):
        if state:
            self.wallpaperMode = "dark"
        else:
            self.wallpaperMode = "light"

    def onWallpaperApply(self, applyWallpaperButton):

        ###### SAVE CONFIG ######

        self.currentConfig = {
            "oldWallpaper": self.wallpaper,
            "oldScheme": self.scheme,
            "oldWallpaperMode": self.wallpaperMode
        }

        with open(self.configPath, 'w') as configFile:
            configFile.write("#######################\n#AUTO-GENERATED CONFIG#\n#######################\n\n")
            for variable, value in self.currentConfig.items():
                configFile.write(f"{variable} = {repr(value)}\n") # repr is used so the python syntax is correct


        os.system(f"matugen image {self.wallpaper} -t {self.scheme} -m {self.wallpaperMode} &")


#######################################
#######################################

    def onDisplayButtonClick(self, displayButton):
        os.system("nwg-displays &")
    
    def onGtkButtonClick(self, gtkButton):
        os.system("nwg-look &")

#######################################
#######################################


    def on_main_window_destroy(self, *args):
        Gtk.main_quit()


# Run the app
win = MyWindow()
Gtk.main()

