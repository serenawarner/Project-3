import sys
import os
from datetime import datetime

# Add backend directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))


from notebook_interface import store_note_db

file_path = "notes.txt"
''' 
def create_note():
    note = input("Enter your note:")
    print (f"Your note is: {note}")
    with open(file_path, "a") as file:
        file.write(note + "\n")
    print("note has been created")
'''
def create_note():
    folder_tag = input("Enter folder tag: ")
    user = input("Enter your name: ")
    title = input("Enter the note title: ")
    content = input("Enter your note:\n")
    creation_time = datetime.now()

    full_note = f"{title}\n{content}\n{creation_time}"

    # Save the title + content to a temp .txt file
    file_path = "notes.txt"
    with open(file_path, "w") as file:
        file.write(full_note)

    store_note_db(folder_tag=folder_tag, filepath=file_path, user=user)
    print("Note saved to database and JSON.")

def read_notes():
    with open(file_path, "r") as file:
        notes = file.readlines()
    for note in notes:
        print(note.strip())

def delete_note():
    note_to_delete = input("Enter the note you want to delete:")
    with open(file_path, "r") as file:
        notes = file.readlines()
    with open(file_path, "w") as file:
        for note in notes:
            if note.strip() != note_to_delete:
                file.write(note)
    print("Note has been deleted.")

if __name__ == "__main__":
    create_note()

