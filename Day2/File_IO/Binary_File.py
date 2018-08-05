# Example of Binary File:
#https://www.devdungeon.com/content/working-binary-data-python
import os

print(os.curdir)

f = open("myfile.bin", "rb")

print(f.read(10))