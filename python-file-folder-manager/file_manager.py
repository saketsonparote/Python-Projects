"""
📂 Python File & Folder Manager

A CLI-based file and folder management system built using pathlib and shutil.

Features:
- Create, read, update, delete folders
- Create, read, update, delete files
- Safe checks and validation
- Clean structured code

Author: Saket Sonparote
"""

from pathlib import Path
import shutil

def create_folder():
    """Create a new folder."""
    try:
        name = input("please tell your folder name :-")
        p = Path(name)
        p.mkdir()  #make directory
        print("folder created successfully")
    except Exception as err:
        print(f"sorry an error occured as {err}")


def read_file_folder():
    """
    List all files and/or folders in the current directory.

    """
    p = Path("")
    items = list(p.rglob('*')) #recursive global
    for i,v in enumerate(items):
        print(f"{i+1}:{v}")

def update_folder():
    """Rename an existing folder."""
    try:
        read_file_folder()
        old_name = input("please tell which folder you want to update :- ")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("please tell your new folder name:- ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("your folder name is updated successfully")
        else:
            print("sorry no such folder exist")
    
    except Exception as err:
        print(f"An error occured as{err}")


def delete_folder():
    """Delete an existing folder."""
    try:
        read_file_folder()
        name = input("please tell which folder you want to delete :- ")
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)   #remove directory
            print("folder deleted successfully")
        else:
            print("no such folder exist")
    except Exception as err:
        print(f"An error occured as{err}")


def create_file():
    """Create a new file."""
    try:
        read_file_folder()
        name = input("please tell your file name:- ")
        p = Path(name)
        if not p.exists():
            with open(name, 'w') as fs: #file system
                data = input("Write what you want in this file:- ")
                fs.write(data)
                print("file created successfully")
        else:
            print("sorry this name file already exists")
    except Exception as err:
        print(f"an error occured as {err}")

        

def read_file() :
    """Read and display file content."""
    try:
        read_file_folder()  
        name = input("please tell your file name :-")  
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name,'r') as fs:
                content = fs.read()
                print("your file content is:- ")
                print(content)
        else:
            print("sorry no such file exists")
    except Exception as err:
        print(f"an error occured as {err}")


def update_file():
    """Rename, append, or overwrite a file."""
    try:
        read_file_folder()
        name = input("please tell your file name : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Option")
            print("1. for renaming the file ")
            print("2. for appending something in the file ")
            print("3. for overwriting the file content ")
            choice = int(input("tell your choice:- "))
            
            if choice == 1:
                new_name = input("tell your new name with extension:- ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("your file name is changed successfully ")
                else:
                    print("sorry this name already exist")
            
            elif choice == 2:
                with open(name, 'a') as fs:
                    data = input("what you want to append:- ")
                    fs.write(" "+ data)
                print("Data appended successfully ")

            elif choice == 3:
                with open(name, 'w') as fs:
                    data = input("what you want to overwrite:- ")
                    fs.write(" "+ data)
                print("Data changed successfully ")
            
            else:
                print("Invalid choice")
    except Exception as err:
        print(f" an error occured as {err}")


def delete_file():
    """Delete an existing file."""
    try:
        read_file_folder()
        name = input("tell your file name with extension: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deleted successfully")
        else:
            print("sorry no such file exist")
    except Exception as err:
        print(f"an error occured as {err}")



while True:
    print(" Options: -")

    print("1. Create a folder")
    print ("2. Read files and folders")
    print("3. Update the folder")
    print("4. Delete the folder")

    print("5. Create a file")
    print("6. Read a file")
    print("7. Update a file")
    print("8. Delete a file")
    print("0. Exit the program")

    try:
        choice = int(input("please choose your options "))
    except ValueError:
        print("Invalid choice, please enter a number only")
        continue

    if choice == 0:
        print("Goodbye!")
        break

    elif choice == 1:
        create_folder()

    elif choice == 2:
        read_file_folder()
        
    elif choice == 3:
        update_folder()

    elif choice == 4:
        delete_folder()

    elif choice == 5:
        create_file()

    elif choice == 6:
        read_file()

    elif choice == 7:
        update_file()

    elif choice == 8:
        delete_file()
    
    else:
        print("Invalid choice, please try again")


