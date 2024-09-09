import os
import re

# ANSI escape sequences for colors
RED = '\033[91m'
PINK = '\033[95m'
GREEN = '\033[92m'
END = '\033[0m'

# Function to replace in file, case insensitive
def replace_in_file(file_path, old_string, new_string):
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read()
            print(f'{PINK}File: {file_path} {END}')
        
        # Check if the string exists (case insensitive)
        if re.search(old_string, content, re.IGNORECASE) is None:
            print(f'{RED}"{old_string}" not found{END}')
            return

        # Replace the old string with the new one (case insensitive)
        updated_content = re.sub(old_string, new_string, content, flags=re.IGNORECASE)
        
        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)
        
        # Count occurrences using re.findall()
        print(f'{GREEN}{len(re.findall(old_string, content, re.IGNORECASE))} occurrences of "{old_string}" replaced with "{new_string}"{END}')
    except FileNotFoundError:
        print(f'{RED}File not found: {file_path}{END}')
    except Exception as e:
        print(f'{RED}An error occurred: {e}{END}')

# Function to replace in all files within a folder, case insensitive
def replace_in_folder(folder_path, old_string, new_string):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_in_file(file_path, old_string, new_string)

# Function to show occurrences of a string in a file, case insensitive
def show_occurrences(file_path, string):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Count occurrences using re.findall() (case insensitive)
        occurrences = len(re.findall(string, content, re.IGNORECASE))
        
        if occurrences == 0:
            print(f'{RED}"{string}" not found in {file_path}{END}')
        return occurrences
    except FileNotFoundError:
        print(f'{RED}File not found: {file_path}{END}')
    except Exception as e:
        print(f'{RED}An error occurred: {e}{END}')
        return 0
        
# Function to show occurrences of a string in all files within a folder, case insensitive
def show_occurrences_in_folder(folder_path, string):
    total_occurrences = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            occurrences = show_occurrences(file_path, string)
            if occurrences:
                total_occurrences += occurrences
    print(f'{GREEN}Total occurrences of "{string}" in folder: {total_occurrences}{END}')

# Function to ask for confirmation before replacing
def confirmation(old_string, new_string):
    confirm = input(f'Are you sure you want to replace "{old_string}" with "{new_string}" ? (y/n): ')
    if confirm.lower() != 'y':
        print(f'{RED}Operation cancelled{END}')
        return False
    return True

# Main menu for user interaction
def menu():
    print(f'''{PINK}
______ _       _        _ _    
|  ___(_)     | |      | | |   
| |_   _ _ __ | |_ __ _| | | __
|  _| | | '_ \| __/ _` | | |/ /
| |   | | | | | || (_| | |   < 
\_|   |_|_| |_|\__\__,_|_|_|\_\                                                              
{END}''')
    print('[1] Replace in folder')
    print('[2] Replace in file')
    print('[3] Show all occurrences of a string in a file')
    print('[4] Show all occurrences of a string in a folder')
    print('[5] Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        folder_path = input('Enter the folder path: ')
        old_string = input('Enter the text to replace: ')
        new_string = input('Enter the new text: ')
        
        if not confirmation(old_string, new_string):
            return
        replace_in_folder(folder_path, old_string, new_string)
    elif choice == '2':
        file_path = input('Enter the file path: ')
        old_string = input('Enter the text to replace: ')
        new_string = input('Enter the new text: ')
        
        if not confirmation(old_string, new_string):
            return
        replace_in_file(file_path, old_string, new_string)
    elif choice == '3':
        file_path = input('Enter the file path: ')
        string = input('Enter the string to search: ')
        
        occurrences = show_occurrences(file_path, string)
        if occurrences:
            print(f'{GREEN}Occurrences of "{string}": {occurrences}{END}')
    elif choice == '4':
        folder_path = input('Enter the folder path: ')
        string = input('Enter the string to search: ')
        
        show_occurrences_in_folder(folder_path, string)
    elif choice == '5':
        exit()

while True:
    menu()
