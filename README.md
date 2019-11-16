# QuickColor
Enables the user to swap between predefined colors by using hotkeys

In order to use the plugin, copy and paste the files in the actions folder to your own actions folder, and the files in the pykrita folder to your own pykrita folder. If you can not find these folders on your system, this guide contains (among other things) instructions for where to find (or create) them: https://docs.krita.org/en/user_manual/python_scripting/krita_python_plugin_howto.html

Additionally, you will need to create a palette named "Teaching" (will change this name in a later version), in which you place the colors you would like to hot-swap between.

Finally, you need to go to  settings > configure krita > keyboard shortcuts and set your desired shortcuts for the actions QuickRed, QuickBlue, QuickWhite, and QuickYellow. (Will change these names in a later version).  

Due to a quirk of my particular circumstance, the four colors must be placed in slot 0, 4, 5, and 6, of your palette, respectively. I will fix this in a later version.
