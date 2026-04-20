# Missing Render Frame Detector

A Python script that scans a render output folder and reports any missing frames 
in the sequence. Built for VFX pipeline use.

## What It Does
This script verifies that the renders in a selected folder are complete. It checks 
for gaps in the frame sequence numbering and outputs a list of the missing frames, 
if it detects any.

## Pipeline Context
A sequence with missing frames cannot be sent to comp. It is impractical to 
manually review all frames when a render farm produces thousands, so this script 
automates the process.

## How To Use
Run the script via the terminal and pass in the folder you want to analyze:

```python3 render_frame_detector.py /path/to/render/folder```

## Requirements
Python 3.6 or higher. No external libraries required.

## Sample Output
```
Missing frame: 4
Missing frame: 7
Missing frame: 8
Scan Complete. 3 missing frames found.
