<h1>GcUtils</h1>

<p> This is a repository whose aim is produce programs to manipulate and edit gcode files (and may be visualize them in future).

<h2>Programas</h2>

<h3>gcode-translate.py</h3>
<p>This program can translate by x, y and z coordinates described in file by a value.</p>

<b>Usage</b>
<p>Initially, you must edit program code to insert the xyz values to deslocate.</p>

<p>To do this, you must search the line with code</p>

<code>translate = [0.000000, 0.000000, 0.000000]</code>

<p>and you must insert in apropriate locals the values of x, y and z to deslocate.</p>

<p><em>Pay attention!</em> 
You must insert values with same units (metric or inches). The program don't convert them.</p>

<p>Save file and execute it with</p>

<code>python3 file.ngc > output.ngc</code>

