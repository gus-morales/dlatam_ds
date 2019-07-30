"""
mayor.py
"""

from os import sys

nums = []
for i in range(len(sys.argv)):
    if i == 0:
        continue
    nums.append(int(sys.argv[i]))

print(sorted(nums, reverse=True)[0])
