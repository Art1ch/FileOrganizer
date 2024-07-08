import os
import tkinter as tk
from tkinter import *
import shutil

root = tk.Tk()
root.title("File organizer")
root.configure(width=500, height=300, background="gray")


def organize_files() -> None:
    source_folder: str = enter_folder_entry.get()
    create_destination_folders(source_folder)
    move_files_to_folders(source_folder)


def create_destination_folders(source_folder: str) -> None:
    if os.path.isdir(source_folder):
        for folder in destination_folders.keys():
            os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
        os.makedirs(os.path.join(source_folder, "Others"), exist_ok=True)
    else:
        raise Exception("Folder wasn't found!")


def move_files_to_folders(source_folder: str) -> None:
    for filename in os.listdir(source_folder):

        file_path = os.path.join(source_folder, filename)

        if not is_valid_file(filename, file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()

        if not is_valid_extension(file_extension):
            continue

        moved: bool = False

        for folder, extensions in destination_folders.items():

            if file_extension in extensions:
                shutil.move(file_path, os.path.join(source_folder, folder, filename))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(source_folder, "Others", filename))


def is_valid_file(filename: str, file_path: str) -> bool:
    return not (os.path.isdir(file_path) or filename.startswith("."))


def is_valid_extension(file_extension: str) -> bool:
    return file_extension not in exceptional_extensions


destination_folders: dict = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.txt', '.pdf', '.docx', '.doc'],
    'Data': ['.csv', '.xlsx'],
    'Audio': ['.mp3', '.wav'],
    'Video': ['.mp4', '.mov', '.avi', '.fiv', '.wmv'],
    'Archives': ['.zip', '.rar', '.tar'],
    'Executables': ['.exe'],
}

exceptional_extensions: tuple = ('.py',)

enter_folder_label = Label(root, text="Enter folder path\nto organize", font="Arial 12", background="gray")
enter_folder_label.place(x=25, y=25)

enter_folder_entry = Entry(root, width=55)
enter_folder_entry.place(x=150, y=30)

organize_button = Button(root, text="Organize", font="Arial 12", command=organize_files)
organize_button.place(x=200, y=150)


def main() -> None:
    root.mainloop()


if __name__ == "__main__":
    main()


#test
