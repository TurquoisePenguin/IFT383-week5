#!/usr/bin/python

seconds = eval(input("Please enter some number of seconds: "))
hours = int(seconds/3600)
minutes = int((seconds/60)-(hours*60))
print(f"{seconds} seconds is equivalent to {hours} hour(s) and {minutes} minute(s).")
