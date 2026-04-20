import os
import sys

# This script looks at a folder containing renders to check for gaps
# Used in pipelines to detect missing frames in a render sequence
# Completed by Alex Anderson April 2026

# Converts the contents of the folder into a sorted list of integers
folder = sys.argv[1]
filenames = os.listdir(folder)
frames = sorted([int(filename.split(".")[1]) for filename in filenames])

# Compares each item with the following item, and if the gap is larger than 1 it detects an error
missing_count = 0
for i in range(len(frames)-1):
    if (frames[i+1] - frames[i]) > 1:
        for x in range(frames[i]+1, frames[i+1]):
            print(f"Missing frame: {x}")
            missing_count += 1

# Prints the total number of missing frames in the folder.
if missing_count > 0:
    print(f"Scan Complete. {missing_count} missing frames found.")
else:
    print("No missing frames found")
