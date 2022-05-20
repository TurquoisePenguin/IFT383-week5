#!/usr/bin/python
import random

balance = float(random.randint(1,10000))
#balance = 100.00
month=1

#month1
print(f"Balance at beginning of month {month}: ${balance:.2f}")

#month2
balance += random.randint(100,500)
balance = balance*1.03
month += 1
print(f"Balance at beginning of month {month}: ${balance:.2f}")

#month3
balance += random.randint(100,500)
balance = balance*1.03
month += 1
print(f"Balance at beginning of month {month}: ${balance:.2f}")
