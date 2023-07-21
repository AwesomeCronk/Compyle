# Notes

* Iterate through instructions
  * Adjust emulated stacks as instructions are processed
  * Generate variable names
* Iterate through instructions
  * Produce C code using variable names

For each instruction, you need to know these:

* Python names
* Constant values
* Stack positions
* Possible types
* Map between Python names and objects?

At any point during processing, an object can be considered a constant or a variable. For constants, you know the value, but for variables, you do not. For variables you may or may not know the type.