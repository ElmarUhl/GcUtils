# GcUtils

This is a repository whose aim is produce programs to manipulate and edit gcode files.

## GCode
Think of G-code as a set of instructions for a machine. It tells the machine exactly where to move, how fast to go, and when to extrude material (like plastic filament in a 3D printer).  These instructions are written in a series of letters and numbers, with common commands like G01 for moving in a straight line and G02 for creating circular paths.

By following this code, the machine can translate a complex 3D model into precise movements, building the object layer by layer.  G-code is not just for 3D printers, it's actually used for many computer controlled machines, like CNC machines and robots.  So next time you see something being created with amazing precision, there's a good chance G-code is behind the scenes making it happen.

## Programas

**gcode-translate.py**

This program can translate by x, y and z coordinates described in file by a value.

**Usage**

- Initially, you must edit program code to insert the xyz values to deslocate.
- To do this, you must search the line with code `translate = [0.000000, 0.000000, 0.000000]`
- and you must insert in apropriate locals the values of x, y and z to deslocate.

**⚠️ Warning!** You must insert values with same units (metric or inches). The program don't convert them.

- Save file and execute it with `python3 file.ngc > output.ngc`

## Useful Links

### Controlers

[Marlin Homepage](https://marlinfw.org/)
[GitHub GBRL](https://github.com/grbl/grbl)
[GitHub GBRL 5X](https://github.com/fra589/grbl-Mega-5X)
[LinuxCNC Homepage](http://linuxcnc.org/)

### GCode Converters
[SVG2GCode](https://pypi.org/project/svg-to-gcode/)
[GBR2NGC](https://github.com/abetusk/gbr2ngc/)
[DRL2GCode](https://github.com/jes/drl2gcode)
[FlatCAM Homepage](http://flatcam.org/)
[Dmap2GCode](https://www.scorchworks.com/Dmap2gcode/dmap2gcode.html)

### GCodeer Viewers
[OpenBuilds](https://cam.openbuilds.com/)
[NC Viewer](https://ncviewer.com/)
[JSCut](https://jscut.org/jscut.html#)
[SVGNest](https://svgnest.com/)
