# README: String Replacement Script

## Introduction

This Python script allows you to:
1. Replace strings (case insensitive) in a file or across multiple files in a folder.
2. Display occurrences of a string within a file or folder before making replacements.
3. Ensure the replacement is done with user confirmation.

The script uses ANSI escape sequences to display colored output in the terminal, enhancing the user experience with colored messages for success, errors, and information.

## Prerequisites

To use this script on your local machine, you need:
- **Python 3.x** installed. You can download it from [python.org](https://www.python.org/downloads/).
- Optionally, you can run this script on an online compiler that supports Python. Recommended online compilers:
  - [Replit](https://replit.com/)
  - [Google Colab](https://colab.research.google.com/)
  - [PythonAnywhere](https://www.pythonanywhere.com/)

## Installation

### For Local Usage:
1. Ensure Python 3.x is installed on your machine.
2. Download or clone the script to your machine.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the script using `cd` command.

### For Online Compiler Usage:
1. Open your preferred online Python compiler.
2. Copy and paste the entire script into the compiler's code editor.
3. Run the script within the compiler.

## Usage

### Local Machine:
1. In the terminal, navigate to the folder where you have saved the script.
2. Run the script by typing:
   ```bash
   python <script_name>.py
   ```
   Replace `<script_name>` with the actual name of your script file.

3. Follow the on-screen menu to choose an action:
   - **Option 1**: Replace a string across all files in a folder.
   - **Option 2**: Replace a string in a specific file.
   - **Option 3**: Show occurrences of a string in a specific file.
   - **Option 4**: Show occurrences of a string across all files in a folder.
   - **Option 5**: Exit the program.

### Online Compiler:
1. Paste the script into the code editor.
2. Run the script.
3. The same menu will appear, and you can follow the same steps to perform replacements or search for string occurrences.

## Script Details

- **replace_in_file**: Replaces a string in a single file.
- **replace_in_folder**: Replaces a string in all files in a folder.
- **show_occurrences**: Shows occurrences of a string in a file.
- **show_occurrences_in_folder**: Shows occurrences of a string in all files in a folder.

### Example Usage:
1. To replace "old_text" with "new_text" in a file:
   ```python
   python <script_name>.py
   ```
   Select option `2`, provide the file path and the strings to replace.

2. To count occurrences of "text" in a folder:
   Run the script and select option `4`, then provide the folder path and the string to search for.

## Notes
- Ensure you have permissions to read and write to the files you are modifying.
- Make a backup of your files before running the script in production environments to prevent unintended data loss.

