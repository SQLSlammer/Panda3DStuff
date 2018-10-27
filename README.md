# Panda 3D Stuff
This repository is for my python scripts for rooms and other things that i will maybe use for animations.

Appropriate credits are given in the .py scripts themselves.

# Requirements (in order to run the scripts)
- [Panda3D 1.10.0](https://www.panda3d.org/download.php?platform=lenny&version=devel&sdk)
- [toontown.py](https://github.com/QED1224/Toontown-Resources/tree/master/panda3d)
- Toontown Phase Files in the Panda3D /models/ directory and the root directory (the same directory where you place the .py files in). 

You can get the phase files from either:

[Toontown Rewritten](https://www.toontownrewritten.com/play)

or

[Toontown Offline](https://ttoffline.com/download)

Both will work the same.

# Stuff i want to make clear right off the bat

1: The phase files MUST be unpacked for them to work properly.

You can unpack them by opening Command Prompt, cd'ing to the directory where your phase files are in and type:

multify.exe -x -f phase_x.mf

(replace phase_x.mf with the name of the phase file you want to unpack, like phase_3.mf)

And then do the procedure described in Requirements (i.e placing the UNPACKED phase files both in the root directory and the Panda3D /models/ directory).

2: toontown.py MUST be placed in the same directory as the .py scripts you have downloaded from this repository.

# How to run the script

1. Open Command Prompt and cd to the directory with the .py script.

2. type `ppython.exe room.py` (if you changed the name of the .py file, replace room.py with the new name of the script)

You're good to go.
