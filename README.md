# GcUtils

This is a repository whose aim is produce programs to manipulate and edit gcode files.

## Programas

**gcode-translate.py**

This program can translate by x, y and z coordinates described in file by a value.

**Usage**

- Initially, you must edit program code to insert the xyz values to deslocate.
- To do this, you must search the line with code `translate = [0.000000, 0.000000, 0.000000]`
- and you must insert in apropriate locals the values of x, y and z to deslocate.

[!WARNING] You must insert values with same units (metric or inches). The program don't convert them.

- Save file and execute it with `python3 file.ngc > output.ngc`

