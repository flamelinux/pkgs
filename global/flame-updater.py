#! /usr/bin/python3
import os
import sys

if sys.argv[1] == "install":
 print("Done :D")
  
if sys.argv[1] == "remove":
 os.system("rm flame-updater.py")
 print("Done :D")
