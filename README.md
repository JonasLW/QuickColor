# QuickColor
Enables the user to swap between predefined colors by using hotkeys

In order to use the plugin, copy and paste the files in the actions folder to your own actions folder, and the files in the pykrita folder to your own pykrita folder. If you can not find these folders on your system, this guide contains (among other things) instructions for where to find (or create) them: https://docs.krita.org/en/user_manual/python_scripting/krita_python_plugin_howto.html

You may also attempt to install the plugin by opening Krita and going to tools > scripts > import python plugins, and selecting the .zip archive you've downloaded from here. Note: Krita's importer will not import the .action files. You will still need to do that manually.

Remember to enable the plugin.  Go to settings > configure krita... > python plugin manager, and check the box to the left of QuickColor0, QuickColor1, etc.

Additionally, you will need to create a palette named "QuickColor", in which you place the colors you would like to hot-swap between.

Finally, you need to go to  settings > configure krita... > keyboard shortcuts and set your desired shortcuts for the actions QuickColor0, QuickColor1, etc. (I personally use ASDF as hotkeys).  

This repository currently enables hotkeys for five colors (the five first colors, by index, in the palette you named "QuickColor").
If you want to extend this functionality, it is fairly simple to just make your own action "QuickColor5", by copying one of the present actions, renaming it, and changing the palette index to 5.
