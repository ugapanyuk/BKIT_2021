import sys, module_2

print("Currently defined names")
print(dir())
print()

print("Names from module_2")
print(dir(module_2))
print()

print("Built-in functions and variables")
import builtins
print(dir(builtins))
