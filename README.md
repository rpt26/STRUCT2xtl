# STRUCT2xtl
Short python 3 script to convert the structural output of the SIESTA DFT software package to the simple text based xtl format readable by visualisation software such as VESTA.

To run the script simply run `"python3 STRUCT2xtl.py"`. Any files with the extension ".STRUCT_OUT" will be read and used to create a crystal data file with the ".xtl" extension. The original file(s) should not be altered.


The script uses the module glob to read files, mendeleev to look up element data, and numpy to convert basis vectors define in a cartesian space to a more conventional crystallographic set of parameters: lengths _a_, _b_, _c_ and angles _alpha_, _beta_, _gamma_. Where _alpha_ is the angle between the unit cell vectors _b_ and _c_ etc.

This script __does not__ preserve symmetry and instead removes all symmetry information.

An example .STRUCT_OUT file is given along with an example output .xtl file. This has been tested and works correctly with VESTA 3.3.9 on 64 bit Ubuntu 16.04.

TODO

* Adjust the atomic coordinates block to align columns using whitespace.
* Check/add compatability for windows.
* Add options to run on a single file or many
