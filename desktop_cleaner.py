#---- Automatic Desktop cleaner script ----

# Keep checking the files in the desktop
# Move certain files (that match a certain criteria) into folders
# Run the script in the background?

import os
import shutil
import tkinter as tk
from tkinter import messagebox


def Message():
    """
    Creates a message pop up to prompt the user about the success of the cleaning.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messagebox.showinfo("Done", "Enjoy your brand new clean desktop environment!")
    exit()


def Parser(path):
    """
    Takes the file path WITHOUT the file extension (or format) as a string and returns a count of the number of copies.
    If there is only one copy, it returns 1.
    :param path:
    :return: tuple: (copy_count, fixed_path_to_folder)
    """
    if path[-1] != ")":
        return (1, path)
    new_path = ""
    num = ""
    for i in range(len(path)-2,0, -1):
        if path[i] == "(":
            new_path = path[0:i]
            break
        else:
            num = path[i] + num

    return (int(num), new_path)


def Automatic_Desktop_Cleaner():
    """
    Checks all the files on the desktop, and organizes them into folders in the desktop based on their type.

    **DISCLAIMER**: It does NOT work on every file type, file types will be stored in a "Uncategorized" folder.
    """


    # Extentions that are most used
    text_document_files = {".txt", ".docx", ".pdf", ".html", ".pptx", ".xls", ".xlsx", ".doc", ".odt", ".rtf", ".odp", ".ods", ".pages"}

    programming_languages_extensions = {
        '.c', '.h',  # C
        '.cpp', '.hpp', '.hxx',  # C++
        '.java',  # Java
        '.py',  # Python
        '.js',  # JavaScript
        '.html', '.htm',  # HTML
        '.css',  # CSS
        '.php',  # PHP
        '.rb',  # Ruby
        '.swift',  # Swift
    }

    # Image Files
    image_files = {".jpg", ".png", ".gif", ".jpeg"}

    # Multimedia Files
    multimedia_files = {".mp3", ".mp4", ".wav", ".mov", ".mkv"}

    # Compressed Files
    compressed_files = {".zip", ".rar",".7z",".tar",".iso"}

    # E-book Formats
    ebook_formats = {".epub", ".djvu", ".fb2", ".mobi", ".azw", ".xps"}

    # Get the files on the desktop
    desktop_path = os.path.expanduser("~/Desktop")

    # Extract files
    files = os.listdir(desktop_path)

    # Get the file path for each indivisual file path and put it in a dictionary
    file_extension_paths_dic = {}


    # For each file, create a its path
    for filename in files:
        file_path = os.path.join(desktop_path,filename)

        # Make sure that is a file (not a directory)
        if os.path.isfile(file_path):

            # Get the file extension
            file_ext = os.path.splitext(filename)[1]

            # Ignore EXE files
            if file_ext != ".exe":

                # Make a new key with an empty list for each extention
                if file_ext not in file_extension_paths_dic:
                    file_extension_paths_dic[file_ext] = []

                file_extension_paths_dic[file_ext].append(file_path)


    # Move files to appropreiate folder based on its type
    for file_extention, file_paths in file_extension_paths_dic.items():

        # Text and documents
        if file_extention in text_document_files:
            the_path = os.path.join(desktop_path, "Documents")

            if not os.path.exists(the_path):
                os.makedirs(the_path)


        # Images
        elif file_extention in image_files:
            the_path = os.path.join(desktop_path, "Images")

            if not os.path.exists(the_path):
                os.makedirs(the_path)


        # Multimedia
        elif file_extention in multimedia_files:
            the_path = os.path.join(desktop_path, "Multimedia")

            if not os.path.exists(the_path):
                os.makedirs(the_path)


        # Compressed
        elif file_extention in compressed_files:
            the_path = os.path.join(desktop_path, "Compressed")

            if not os.path.exists(the_path):
                os.makedirs(the_path)

        # Ebook
        elif file_extention in ebook_formats:
            the_path = os.path.join(desktop_path, "Ebooks")

            if not os.path.exists(the_path):
                os.makedirs(the_path)

        # Programming Languages
        elif file_extention in programming_languages_extensions:
            the_path = os.path.join(desktop_path, "Program Source Code")

            if not os.path.exists(the_path):
                os.makedirs(the_path)


        # In case it was not found in the most common lists of extentions
        else:
            the_path = os.path.join(desktop_path,"Uncategorized")
            if not os.path.exists(the_path):
                os.makedirs(the_path)


        # Move the file
        for file_origin in file_paths:
            try:
                shutil.move(file_origin, the_path)

            # In the case that the file already exists
            except:
                base_name = os.path.basename(file_origin)
                desired_path_to_folder = os.path.join(the_path,base_name)
                new_file_path, ext= os.path.splitext(desired_path_to_folder)
                count, path_to_increment = Parser(new_file_path)  # Returns (current_count, fixed_path)

                incremented_path_to_folder = desired_path_to_folder
                while os.path.exists(incremented_path_to_folder):
                    incremented_path_to_folder = f"{path_to_increment}({count}){ext}"
                    count += 1

                name_without_ext = os.path.basename(path_to_increment) # Get the path to desktop with the desktop
                look_for_in_desktop = os.path.join(desktop_path,f"{name_without_ext}({count-1}){ext}") # Look for the incremented copy if it is in the desktop


                # In case the incremented file already exists in the desktop
                if os.path.exists(look_for_in_desktop):

                    temp = os.path.splitext(name_without_ext)[0]+ "~ã~$@$%24*õñ♜♟@45♧♡" # Create a temporary name
                    temp_path = os.path.join(desktop_path, f"{temp}({count}){ext}") # Connect it to make the temporary path
                    os.rename(look_for_in_desktop,temp_path) # Change the name of the already existing incremented file on the desktop to the temporary path
                    os.rename(file_origin, look_for_in_desktop) # Change the file name to the incremented version
                    shutil.move(look_for_in_desktop, the_path) # Move it to the respective folder
                    os.rename(temp_path, look_for_in_desktop) # Change the temporary path back to original

                else:
                    os.rename(file_origin,look_for_in_desktop)
                    shutil.move(look_for_in_desktop, the_path) # Move it to the respective folder

    Message() # Inform user


if __name__ == "__main__":
    Automatic_Desktop_Cleaner()
