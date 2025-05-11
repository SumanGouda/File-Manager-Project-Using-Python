# File Organizer using Python

This is a simple Python script that organizes files in a specified folder by their file extensions. It's useful for keeping your directories clean and easy to navigate.

## What It Does

The script scans all the files in a given directory and moves them into subfolders based on their file types (e.g., `.jpg` files into a folder named `jpg`, `.pdf` into `pdf`, etc.).

## How It Works

1. Lists all items in the source directory.
2. Ignores any subdirectories (works only on files).
3. Extracts the file extension of each file.
4. Creates a new folder for each extension (if not already present).
5. Moves the file into the corresponding folder.

## Example

If your folder contains:
snackBOT/
├── image1.png
├── doc1.pdf
├── music.mp3
├── archive.zip


After running the script, it becomes:
snackBOT/
├── png/
│ └── image1.png
├── pdf/
│ └── doc1.pdf
├── mp3/
│ └── music.mp3
├── zip/
│ └── archive.zip


## How to Use

1. Change the `source_file` path in the script to your folder path:
   ```python
   source_file = "D:\\PROJECTS\\LOGO\\snackBOT"

2. Run the script: python file_organizer.py

## Requirements
Python 3.x

No external libraries needed (uses os and shutil)

## Disclaimer
Make sure to backup your files before running the script, especially if the folder contains important or system files.

## Author
Made by Suman Gouda as a part of learning Python and automating basic file tasks.




